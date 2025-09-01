# agents/analysis_agent.py
from utils.tiktok_client import TikTokClient
from utils.sentiment import analyze_sentiment
from utils.logger import log

class AnalysisAgent:
    def __init__(self):
        self.client = TikTokClient()

    def run(self, creators):
        log.info("AnalysisAgent started")
        viral_reports = []

        for creator in creators:
            # Note: now using creator['name'] (username) instead of id
            videos = self.client.get_creator_videos(creator['name'])
            for video in videos:
                sentiment_report = analyze_sentiment(video['description'])
                viral_reports.append({
                    "creator": creator['name'],
                    "video_id": video['id'],
                    "description": video['description'],
                    "sentiment_report": sentiment_report,
                    "likes": video.get('likes', 0),
                    "shares": video.get('shares', 0),
                    "comments": video.get('comments', 0)
                })
        return viral_reports
