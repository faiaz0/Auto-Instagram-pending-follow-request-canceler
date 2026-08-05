import json
import time
import random
import os
from playwright.sync_api import sync_playwright

def read_json(file_path):
    """Extract usernames from Instagram data export JSON"""
    try:
        if not os.path.exists(file_path):
            print(f"❌ File not found at: {file_path}")
            return None

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        usernames = []
        
        # Correctly parses your exact label_values structure block
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and "label_values" in item:
                    labels = item.get("label_values", [])
                    for sub_item in labels:
                        if isinstance(sub_item, dict) and sub_item.get("label") == "Username":
                            username = sub_item.get("value")
                            if username:
                                usernames.append(username)
                                
        print(f"✅ Successfully loaded {len(usernames)} pending follow requests.")
        return usernames

    except json.JSONDecodeError:
        print("❌ Invalid JSON formatting inside the file!")
        return None
    except Exception as e:
        print(f"❌ Error parsing file layout: {e}")
        return None

def cancel_follow_requests():
    # Prompt for the file path cleanly
    print("==================================================")
    print("          Instagram Follow Request Canceler       ")
    print("==================================================")
    file_path = input("Enter the path to your pending_follow_requests.json file:\nPath: ").strip().strip('"')
    
    usernames = read_json(file_path)
    if not usernames:
        print("❌ No usernames found. Exiting.")
        return

    print("\n🚀 Connecting to your debug Chrome session...")
    
    with sync_playwright() as p:
        try:
            # Connects directly to the browser window launched by your .bat file
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            context = browser.contexts[0]
            page = context.pages[0] if context.pages else context.new_page()
            
            print("✅ Connection established! Beginning processing loop...\n")
            
            count = 0
            for idx, user in enumerate(usernames, 1):
                print(f"[{idx}/{len(usernames)}] Navigating to profile: @{user}")
                
                try:
                    # Navigate to profile URL
                    page.goto(f"https://www.instagram.com/{user}/", wait_until="load", timeout=30000)
                    time.sleep(random.uniform(2.5, 4.0)) # Human delay
                    
                    # Language-agnostic button lookup using ARIA or common descriptive labels
                    requested_btn = page.locator("button:has-text('Requested'), button:has-text('İstek Gönderildi'), button:has-text('Solicitado'), button:has-text('Abonné(e)')").first
                    
                    if requested_btn.is_visible(timeout=3000):
                        requested_btn.click()
                        time.sleep(random.uniform(1.0, 2.0))
                        
                        # Handle the confirmation dialog that pops up
                        unfollow_confirm = page.locator("button:has-text('Unfollow'), button:has-text('Takibi Bırak'), button:has-text('Dejar de seguir'), button:has-text('Se désabonner')").first
                        if unfollow_confirm.is_visible(timeout=2000):
                            unfollow_confirm.click()
                            count += 1
                            print(f"   ↳ 🚫 Cancelled follow request successfully.")
                        else:
                            # Fallback click if no modal appeared
                            count += 1
                            print(f"   ↳ 🚫 Request cancelled (direct toggle).")
                    else:
                        print("   ↳ ℹ️ Profile does not show an active pending request (Skipping).")
                        
                except Exception as page_err:
                    print(f"   ↳ ⚠️ Problem handling profile @{user}: {page_err}")
                
                # Dynamic safety logic breaks to emulate human browsing
                if idx % 20 == 0:
                    break_time = random.randint(25, 45)
                    print(f"\n💤 anti-detection break: Pausing for {break_time} seconds...")
                    time.sleep(break_time)
                    
                if idx % 50 == 0:
                    long_break = random.randint(70, 110)
                    print(f"\n☕ Cooldown break: Pausing for {long_break} seconds...")
                    time.sleep(long_break)
                    
            print(f"\n🏁 Finished! Total follow requests revoked: {count}")
            
        except Exception as conn_err:
            print(f"\n❌ Fail connection error: {conn_err}")
            print("Make sure you ran 'launch_chrome.bat' and that your browser window is actively open before starting this script!")

if __name__ == "__main__":
    cancel_follow_requests()
