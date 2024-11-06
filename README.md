# SoundCloud Bot Detector

This project identifies potential bot accounts in a SoundCloud user's followers. Using SoundCloud's API, it flags accounts that exhibit bot-like characteristics based on activity and follower count, helping users maintain a more authentic follower base.

## Features

- **Follower Analysis:** Scans a SoundCloud user's followers and identifies accounts with suspicious activity.
- **Public Track Information:** Retrieves and displays public track information of followers.
- **Track Like Analysis:** Lists users who liked specific tracks.
- **Bot Detection Logic:** Flags accounts based on activity length and follower count, with customizable thresholds and a whitelist to exclude known accounts.

## How It Works

The bot detector script authenticates a user with the SoundCloud API and gathers follower data, checking for specific criteria that indicate a bot:

1. **Activity Duration:** Flags accounts with unusually short or long periods of activity.
2. **Follower Count:** Flags accounts with low follower counts (default < 20).
3. **Whitelist Exclusion:** Excludes trusted accounts specified in a `whitelist` file.

The script returns a list of flagged accounts and optionally outputs information about each.

## Project Structure

- `SoundCloud Bot Detector.py`: Main script for authentication and bot detection.
- `constants.py`: Holds configuration constants, including `auth` (authentication token) and `whitelist`.
- `soundcloud.py`: SoundCloud API wrapper library.

## Getting Started

### Prerequisites

- Python 3.x
- soundcloud.py by 7x11x13 on github: https://github.com/7x11x13/soundcloud.py

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/soundcloud-bot-detector.git
   cd soundcloud-bot-detector
2. Install dependencies:
   ```bash
   pip install -r requirements
   ```

3. Configure `constants.py` with your SoundCloud `auth_token` and a list of trusted accounts (`whitelist`).

### Usage

Run the driver script with:
```bash
python driver.py
```

### Example Output

- **User Info:** Displays the authenticated user's ID and SoundCloud permalink.
- **Possible Bots in Following:** Lists flagged accounts with bot-like behavior.

## Functions

- **get_followers:** Retrieves all followers of the authenticated user.
- **get_public_tracks:** Lists public tracks of a specified user.
- **get_track_likes:** Shows users who liked a specific track.
- **detect_bots:** Flags bot-like accounts in the authenticated user's follower list.

## Future Improvements

- **Enhanced Bot Detection:** Add more criteria (e.g., suspicious engagement patterns).
- **Automated Reporting:** Integrate a way to notify SoundCloud about detected bots.
- **Improved Timeout Handling:** Optimize API calls to reduce rate-limiting issues.
