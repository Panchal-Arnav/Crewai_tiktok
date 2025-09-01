# agents/search_agent.py
from TikTokApi import TikTokApi
from utils.logger import log

class SearchAgent:
    def __init__(self):
        self.client = TikTokApi()

    def run(self, subject):
        log.info(f"SearchAgent started for subject: {subject}")
        creators = self.client.search_creators(subject)
        return creators
