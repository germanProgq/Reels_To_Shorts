# Instagram to YouTube Shorts Downloader

This project allows you to download videos from Instagram based on a hashtag and re-upload them to YouTube Shorts. It uses the `selenium` lib to log onto the account and the `instaloader` library to download Instagram posts.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [License](#license)

## Project Overview

This script uses the said above Python libraries to:
1. Log in to Instagram using provided credentials.
2. Download videos from a specified hashtag.
3. Filter videos by duration (e.g., up to 20 seconds).
4. (Optional) Process and upload these videos to YouTube Shorts.

## Features

- Download videos from Instagram based on a hashtag.
- Automatically filters videos by duration (up to 20 seconds).
- Saves downloaded videos to a specified directory.

## Requirements

- Python 3.7+
- An Instagram account (username and password are required for login)
- `instaloader` for interacting with Instagram.
- `moviepy` for processing videos.
- `requests` and `beautifulsoup4` (if using HTML scraping).

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/germanProgq/reels_to_shorts.git
cd instagram-to-youtube-shorts
```

### 2. Create and Activate using scripts

```bash
./setup.bat
```
## Usage

### Run the Script

To start downloading Instagram videos:

Make sure to have replaced the [info](info_alike) with info.py file, where you set all the needed information (all of it is inside the info_alike file)

```bash
./start.bat
```

- The script will log in to Instagram, search for posts with the specified hashtag, and download videos that meet the filtering criteria.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes
- Ensure you use your Instagram credentials responsibly. Instagram may limit or block your account if it detects automated scraping.
- To avoid account bans, consider setting up delays between requests or using a proxy.
- This project assumes fair use of Instagram content. Make sure you comply with Instagram's terms of service and copyright policies.