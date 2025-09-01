# utils/tiktok_client.py
from TikTokApi import TikTokApi
from utils.logger import log

class TikTokClient:
    def __init__(self):
        # TikTokApi should be used inside a context manager
        self.api = TikTokApi()

    def search_creators(self, subject, max_results=10):
        """
        TikTokApi does not provide direct 'search_creators'.
        Instead, we use search.users() to find creators by subject/keyword.
        """
        try:
            with self.api as api:
                users = api.search.users(subject, count=max_results)
                creators = []
                for u in users:
                    user_info = u.info()
                    creators.append({
                        "id": user_info.get("user", {}).get("id", ""),
                        "name": user_info.get("user", {}).get("uniqueId", ""),
                        "followerCount": user_info.get("stats", {}).get("followerCount", 0)
                    })
                log.info(f"Found {len(creators)} creators for subject '{subject}'")
                return creators
        except Exception as e:
            log.error(f"Error searching creators: {e}")
            return []

    def get_creator_videos(self, creator_username, max_videos=5):
        """
        Fetch recent videos from a creator (by username).
        """
        try:
            with self.api as api:
                user = api.user(username=creator_username)
                videos = []
                for v in user.videos(count=max_videos):
                    v_dict = v.as_dict
                    videos.append({
                        "id": v_dict.get("id"),
                        "description": v_dict.get("desc", ""),
                        "likes": v_dict.get("stats", {}).get("diggCount", 0),
                        "shares": v_dict.get("stats", {}).get("shareCount", 0),
                        "comments": v_dict.get("stats", {}).get("commentCount", 0)
                    })
                log.info(f"Retrieved {len(videos)} videos for creator {creator_username}")
                return videos
        except Exception as e:
            log.error(f"Error retrieving videos for creator {creator_username}: {e}")
            return []
