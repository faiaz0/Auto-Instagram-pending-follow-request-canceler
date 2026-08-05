# Instagram Pending Requests Canceler

Automatically cancel all your pending Instagram follow requests in bulk, using realistic human‑like interaction to stay under the radar.

## What does this tool do?

Over time, you may have sent follow requests that are still pending – some for weeks or even months. Instagram does **not** provide a native way to view or cancel these requests in bulk. You would have to manually visit each profile, one by one, to cancel them individually.

This tool automates that tedious process:
- It reads your exported Instagram data (specifically the `pending_follow_requests.json` file) to get a list of all pending requests.
- It then uses **Playwright** to launch a real browser, logs into Instagram, and navigates to each profile to click the “Cancel” button.
- All actions are delayed and randomized to mimic natural human behavior, reducing the risk of triggering anti‑bot measures.

## Why would you need this?

- **Clean up** old requests you no longer remember sending.
- **Start fresh** with a clean follow‑request list.
- **Remove requests** from inactive or private accounts that never accept.
- **Save hours** of manual clicking and scrolling.
- **See exactly** who you’ve sent requests to – Instagram doesn’t show you this list anywhere in the app.

## Prerequisites

- Python 3.8 or higher
- A modern web browser (Chrome, Edge, or Firefox) – Playwright will install its own browser binaries
- Your exported Instagram data (with `pending_follow_requests.json`)

## Installation

1. Clone this repository:
   ```bash
  
