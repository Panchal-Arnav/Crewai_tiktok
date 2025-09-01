# agents/report_agent.py
from utils.logger import log

class ReportAgent:
    def run(self, viral_reports):
        log.info("ReportAgent started")
        report = "Viral TikTok Content Report\n\n"
        for item in viral_reports:
            report += f"Creator: {item['creator']}\n"
            report += f"Video ID: {item['video_id']}\n"
            report += f"Description: {item['description']}\n"
            report += f"Likes: {item['likes']}, Shares: {item['shares']}, Comments: {item['comments']}\n"
            report += f"Sentiment Analysis:\n{item['sentiment_report']}\n"
            report += "-"*40 + "\n"
        return report
