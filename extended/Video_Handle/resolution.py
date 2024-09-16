from moviepy.editor import VideoFileClip, concatenate_videoclips

def combine_videos(video_paths):
    clips = []
    total_duration = 0

    for path in video_paths:
        clip = VideoFileClip(path)
        clips.append(clip)
        total_duration += clip.duration
        
        if 40 <= total_duration <= 55:
            break
    
    final_clip = concatenate_videoclips(clips, method='compose')
    final_video_path = "combined_video.mp4"
    final_clip.write_videofile(final_video_path, codec='libx264', fps=24)
    
    return final_video_path

def resize_video(video_path):
    clip = VideoFileClip(video_path)
    
    # Resize to 1080x1920 for YouTube Shorts
    resized_clip = clip.resize(height=1920)
    resized_clip = resized_clip.crop(x_center=resized_clip.w / 2, width=1080)
    
    resized_video_path = "resized_video.mp4"
    resized_clip.write_videofile(resized_video_path, codec='libx264', fps=24)
    
    return resized_video_path

