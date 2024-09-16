from extended.Instagram.instagram_login import extract_instagram_posts
from extended.Video_Handle.resolution import combine_videos, resize_video
from extended.YouTube.youtube_handle import upload_to_youtube
from extended.Instagram.instagram_handle import filter_and_download_videos
import argparse
from info import ig_search, ig_email_login, ig_password
from info import target_directory, max_videos



def main(hashtag):
    urls_videos = extract_instagram_posts(ig_email_login, ig_password, ig_search)
    downloaded_videos = filter_and_download_videos(urls_videos, target_directory, max_videos)

    if not downloaded_videos:
        print("No videos downloaded.")
        return

    combined_video_path = combine_videos(downloaded_videos)
    resized_video_path = resize_video(combined_video_path)
    
    upload_response = upload_to_youtube(
        video_path=resized_video_path,
        title="Funny Meme Compilation",
        description="A compilation of funny memes from Instagram.",
        tags=["funny", "memes", "compilation"]
    )
    
    print(f"Upload successful: {upload_response['id']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Instagram to YouTube Shorts Bot')
    parser.add_argument('command', type=str, help='The command to run: "start"')
    parser.add_argument('--hashtag', type=str, default='funny', help='Hashtag to search for Instagram videos')
    
    args = parser.parse_args()
    
    if args.command.lower() == 'start':
        main(args.hashtag)
    else:
        print("Unknown command. Use 'start' to run the bot.")
