from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_youtube(video_path, title, description, tags):
    youtube = build('youtube', 'v3', developerKey='YOUR_YOUTUBE_API_KEY')

    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '22',
        },
        'status': {
            'privacyStatus': 'public',
            'madeForKids': False,
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )
    response = request.execute()

    return response
