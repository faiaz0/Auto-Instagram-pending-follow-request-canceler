# Auto Instagram Pending Requests Canceler

Bulk cancel all your pending Instagram follow requests using browser automation with human‑like delays to avoid detection.

---

## What it does

Instagram doesn’t show you a list of pending follow requests, and there’s no way to cancel them in bulk.  
This tool reads your exported Instagram data, visits every pending profile automatically, and clicks “Cancel” – saving you hours of manual clicking.

## Why use it

- Clean up old requests you forgot about  
- Remove pending requests to inactive or private accounts  
- See exactly who you’ve sent requests to (Instagram hides this)  
- Save time and start with a clean follow‑request list

---

## Prerequisites

- Python 3.8+
- Google Chrome (logged in to your Instagram account)
- Your Instagram data export (JSON)

---

## Installation

```bash
git clone https://github.com/faiaz0/Auto-Instagram-pending-follow-request-canceler.git
cd Auto-Instagram-pending-follow-request-canceler
```
```
pip install -r requirements.txt
playwright install chromium
```

---

## How to get your Instagram data

1. Go to Instagram **Settings** → **Accounts Center**
2. Click **Your information and permissions** → **Download your information**
3. Select your Instagram account
4. Choose **Download or transfer information** → **Some of your information**
5. Select **Followers, following and follow requests**
6. Set date range to **All time**, format **JSON**, and submit
7. Wait for the download link (usually a few minutes)

After extraction, your file will be at:  
`connections/followers_and_following/pending_follow_requests.json`

---

## Usage

1. **Get your Chrome user agent** from [https://iplogger.org/useragents/](https://iplogger.org/useragents/) and update it in `launch_chrome.bat`:
   ```batch
   --user-agent="YOUR_USER_AGENT_HERE"
   ```

2. **Launch Chrome in debug mode**:
   ```bash
   launch_chrome.bat
   ```

3. **Log in to Instagram** in that Chrome window.

4. **Run the script**:
   ```bash
   python cancel_requests.py
   ```

5. **Enter the path** to your `pending_follow_requests.json` file when prompted.

---

## How it works

For each pending request, the script:
- Goes to the user’s profile
- Clicks the “Requested” button (detects it in any language)
- Confirms the cancellation
- Waits randomly between actions to mimic human behaviour
- Takes breaks every 20 and 50 users to avoid rate‑limiting

---

## Safety features

- 2–3 sec delay between users  
- 20–30 sec break every 20 users  
- 60–90 sec break every 50 users  
- Uses your existing Chrome session (keeps cookies and login)

---

## Notes

- Keep Chrome visible during the process  
- Don’t interact with the browser while the script runs  
- ~20–25 minutes for 500 users  
- Works with English, Turkish, French, Spanish, Italian, and German Instagram interfaces

---

## ⚠️ Disclaimer

This tool is for **educational and research purposes only**.  
It is meant to help you manage your **own** exported Instagram data.  
You are responsible for complying with Instagram’s Terms of Service.  
Use at your own risk – the author is not liable for any consequences.

---

## License

MIT License – see the [LICENSE](LICENSE) file.

## Credit

[mobilteknolojileri](https://github.com/mobilteknolojileri)
