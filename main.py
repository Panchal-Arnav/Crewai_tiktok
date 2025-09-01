# main.py
from agents.search_agent import SearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent
from utils.logger import log
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
def main():
    subject = input("Enter the subject to analyze on TikTok: ").strip()
    try:
        search_agent = SearchAgent()
        creators = search_agent.run(subject)

        if not creators:
            log.info("No creators found. Exiting.")
            return

        analysis_agent = AnalysisAgent()
        viral_reports = analysis_agent.run(creators)

        report_agent = ReportAgent()
        report = report_agent.run(viral_reports)

        print(report)

    except Exception as e:
        log.error(f"An error occurred in the main flow: {e}")

if __name__ == "__main__":
    main()