import os
import requests
from moviepy.editor import VideoFileClip

def download_video(url, target_directory, filename):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    file_path = os.path.join(target_directory, filename)
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Video downloaded successfully: {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)

    return file_path
def filter_and_download_videos(video_urls, target_directory, max_videos):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    downloaded_videos = []
    
    for i, url in enumerate(video_urls):
        if i >= max_videos:
            break
        
        filename = f"video_{i + 1}.mp4"
        video_path = os.path.join(target_directory, filename)
        
        download_video(url, target_directory, filename)
        
        video_clip = VideoFileClip(video_path)
        duration = video_clip.duration
        
        if duration <= 20:
            downloaded_videos.append(video_path)
        else:
            os.remove(video_path)
    
    return downloaded_videos


    

