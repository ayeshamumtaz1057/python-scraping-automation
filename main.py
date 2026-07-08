"""
main.py
-------
Poori automation pipeline:
1. Website se data scrape karna
2. CSV + PDF report banana
3. Report ko email se automatically bhejna
"""

from scraper import scrape_quotes
from report_generator import save_csv, save_pdf
from mailer import send_email_with_attachment
import config


def run_pipeline():
    print("Step 1: Scraping data...")
    data = scrape_quotes(pages=2)

    if not data:
        print("No data scraped. Stopping pipeline.")
        return

    print("\nStep 2: Generating reports...")
    save_csv(data, "report.csv")
    save_pdf(data, "report.pdf", title="Daily Quotes Report")

    print("\nStep 3: Sending email...")
    send_email_with_attachment(
        sender_email=config.SENDER_EMAIL,
        sender_password=config.SENDER_APP_PASSWORD,
        receiver_email=config.RECEIVER_EMAIL,
        subject="Automated Scraping Report",
        body=(
            "Assalam o Alaikum,\n\n"
            "Attached is the automatically generated report from today's "
            "web scraping run.\n\n"
            "Regards,\nPython Automation Bot"
        ),
        attachment_path="report.pdf"
    )

    print("\nPipeline finished successfully!")


if __name__ == "__main__":
    run_pipeline()
