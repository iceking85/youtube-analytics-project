import os
from googleapiclient.discovery import build

api_key: str = os.getenv('API_KEY_YOUTUBE')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id):
        self.__video_id = video_id
        try:
            self.video_data = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
            self.title = self.video_data['items'][0]['snippet']['title']
            self.video_url = f'https://www.youtube.com/watch?v={self.__video_id}'
            self.views = self.video_data['items'][0]['statistics']['viewCount']
            self.like_count = self.video_data['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.video_url = None
            self.views = None
            self.like_count = None


    @property
    def video_id(self):
        return self.__video_id

    def __str__(self):
        return f"{self.title}"

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    @property
    def playlist_id(self):
        return self.__playlist_id