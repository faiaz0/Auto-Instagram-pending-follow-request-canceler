# Auto Instagram Pending Follow Request Canceler

Bulk-cancel all your pending Instagram follow requests using browser automation with human-like delays to avoid detection.

Instagram doesn't show a list of pending follow requests and gives you no way to cancel them in bulk. This tool reads your exported Instagram data, visits each pending profile automatically, and clicks **Cancel** — saving you hours of manual clicking.

## Features

- Reads your official Instagram data export (JSON) to find every pending request
- Automates cancellation with Playwright, using your existing logged-in Chrome session
- Randomized delays and periodic breaks to mimic human behavior
- Works across multiple Instagram interface languages (English, Turkish, French, Spanish, Italian, German)

## Prerequisites

- Python 3.8+
- Google Chrome (logged in to your Instagram account)
- Your Instagram data export (JSON)

## Installation

```bash
git clone https://github.com/faiaz0/Auto-Instagram-pending-follow-request-canceler.git
cd Auto-Instagram-pending-follow-request-canceler
```

```
pip install -r requirements.txt
playwright install chromium
```

## Getting Your Instagram Data

1. Go to Instagram **Settings** → **Accounts Center**
2. Click **Your information and permissions** → **Download your information**
3. Select your Instagram account
4. Choose **Download or transfer information** → **Some of your information**
5. Select **Followers, following and follow requests**
6. Set date range to **All time**, format to **JSON**, and submit
7. Wait for the download link (usually a few minutes)

Your file will be located at:
`connections/followers_and_following/pending_follow_requests.json`

## Usage

1. Open `launch_chrome.bat` and set your Chrome user agent (get one from [iplogger.org/useragents](https://iplogger.org/myuseragent/)):
   ```
   --user-agent="YOUR_USER_AGENT_HERE"
   ```
2. Launch Chrome in debug mode:
   ```bash
   launch_chrome.bat
   ```
3. Log in to Instagram in that Chrome window.
4. Run the script:
   ```bash
   python cancel_requests.py
   ```
5. Enter the path to your `pending_follow_requests.json` file when prompted.

## How It Works

For each pending request, the script:
- Opens the user's profile
- Detects and clicks the "Requested" button (any supported language)
- Confirms the cancellation
- Waits a randomized interval between actions
- Takes longer breaks every 20 and 50 users to avoid rate-limiting

## Safety Features

- 2–3 second delay between users
- 20–30 second break every 20 users
- 60–90 second break every 50 users
- Runs through your existing Chrome session, preserving cookies and login state

## Notes

- Keep the Chrome window visible while the script runs
- Don't interact with the browser during a run
- Roughly 20–25 minutes for 500 users

## Disclaimer

This tool is for **educational and personal use only**, intended to help you manage your own exported Instagram data. You are responsible for complying with Instagram's Terms of Service. Use at your own risk — the author is not liable for any consequences of use.

## Credits

Originally created by [mobilteknolojileri](https://github.com/mobilteknolojileri/instagram-pending-requests-canceler). This repository is a repaired and maintained fork.

## License

MIT License — see [LICENSE](LICENSE).

## Author

**Faiaz** ([@faiaz0](https://github.com/faiaz0))
