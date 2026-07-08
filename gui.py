"""
gui.py
------
Tkinter GUI for the Scrape -> Report -> Email automation pipeline.

Run with:
    python gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os

from scraper import scrape_quotes
from report_generator import save_csv, save_pdf
from mailer import send_email_with_attachment
import config


class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Automation - Scrape, Report & Email")
        self.root.geometry("560x520")
        self.root.resizable(False, False)

        self.scraped_data = []

        self.build_ui()

    # ---------- UI Layout ----------
    def build_ui(self):
        title = tk.Label(
            self.root, text="Web Scraper -> Report -> Auto Email",
            font=("Helvetica", 15, "bold")
        )
        title.pack(pady=(15, 5))

        subtitle = tk.Label(
            self.root,
            text="quotes.toscrape.com se data scrape kar ke PDF/CSV report banata hai\naur email par bhejta hai.",
            font=("Helvetica", 9), fg="gray"
        )
        subtitle.pack(pady=(0, 15))

        # ---- Scraping settings ----
        scrape_frame = ttk.LabelFrame(self.root, text="Step 1: Scrape Data")
        scrape_frame.pack(fill="x", padx=20, pady=8)

        tk.Label(scrape_frame, text="Pages to scrape:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.pages_entry = ttk.Entry(scrape_frame, width=6)
        self.pages_entry.insert(0, "2")
        self.pages_entry.grid(row=0, column=1, padx=8, pady=8, sticky="w")

        self.scrape_btn = ttk.Button(scrape_frame, text="Scrape Now", command=self.start_scrape_thread)
        self.scrape_btn.grid(row=0, column=2, padx=8, pady=8)

        self.scrape_status = tk.Label(scrape_frame, text="Status: Not started", fg="gray")
        self.scrape_status.grid(row=1, column=0, columnspan=3, padx=8, pady=(0, 8), sticky="w")

        # ---- Report settings ----
        report_frame = ttk.LabelFrame(self.root, text="Step 2: Generate Report")
        report_frame.pack(fill="x", padx=20, pady=8)

        self.report_btn = ttk.Button(
            report_frame, text="Generate CSV + PDF",
            command=self.generate_reports, state="disabled"
        )
        self.report_btn.grid(row=0, column=0, padx=8, pady=8)

        self.report_status = tk.Label(report_frame, text="Status: Waiting for data", fg="gray")
        self.report_status.grid(row=0, column=1, padx=8, pady=8, sticky="w")

        # ---- Email settings ----
        email_frame = ttk.LabelFrame(self.root, text="Step 3: Send Email")
        email_frame.pack(fill="x", padx=20, pady=8)

        tk.Label(email_frame, text="Sender Email:").grid(row=0, column=0, padx=8, pady=4, sticky="w")
        self.sender_entry = ttk.Entry(email_frame, width=35)
        self.sender_entry.insert(0, config.SENDER_EMAIL)
        self.sender_entry.grid(row=0, column=1, padx=8, pady=4)

        tk.Label(email_frame, text="App Password:").grid(row=1, column=0, padx=8, pady=4, sticky="w")
        self.password_entry = ttk.Entry(email_frame, width=35, show="*")
        self.password_entry.insert(0, config.SENDER_APP_PASSWORD)
        self.password_entry.grid(row=1, column=1, padx=8, pady=4)

        tk.Label(email_frame, text="Receiver Email:").grid(row=2, column=0, padx=8, pady=4, sticky="w")
        self.receiver_entry = ttk.Entry(email_frame, width=35)
        self.receiver_entry.insert(0, config.RECEIVER_EMAIL)
        self.receiver_entry.grid(row=2, column=1, padx=8, pady=4)

        self.email_btn = ttk.Button(
            email_frame, text="Send Email", command=self.start_email_thread, state="disabled"
        )
        self.email_btn.grid(row=3, column=0, padx=8, pady=8)

        self.email_status = tk.Label(email_frame, text="Status: Waiting for report", fg="gray")
        self.email_status.grid(row=3, column=1, padx=8, pady=8, sticky="w")

        # ---- Log box ----
        log_frame = ttk.LabelFrame(self.root, text="Activity Log")
        log_frame.pack(fill="both", expand=True, padx=20, pady=(8, 15))

        self.log_box = tk.Text(log_frame, height=10, state="disabled", bg="#f5f5f5")
        self.log_box.pack(fill="both", expand=True, padx=5, pady=5)

    # ---------- Helpers ----------
    def log(self, message):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    # ---------- Step 1: Scrape ----------
    def start_scrape_thread(self):
        self.scrape_btn.config(state="disabled")
        self.scrape_status.config(text="Status: Scraping...", fg="orange")
        self.log("Scraping started...")
        threading.Thread(target=self.run_scrape, daemon=True).start()

    def run_scrape(self):
        try:
            pages = int(self.pages_entry.get())
            data = scrape_quotes(pages=pages)
            self.scraped_data = data

            if data:
                self.root.after(0, lambda: self.on_scrape_success(len(data)))
            else:
                self.root.after(0, lambda: self.on_scrape_failure("No data found."))
        except Exception as e:
            self.root.after(0, lambda: self.on_scrape_failure(str(e)))

    def on_scrape_success(self, count):
        self.scrape_status.config(text=f"Status: Done ({count} items)", fg="green")
        self.log(f"Scraping finished: {count} quotes collected.")
        self.scrape_btn.config(state="normal")
        self.report_btn.config(state="normal")

    def on_scrape_failure(self, error_msg):
        self.scrape_status.config(text="Status: Failed", fg="red")
        self.log(f"Scraping failed: {error_msg}")
        self.scrape_btn.config(state="normal")
        messagebox.showerror("Scraping Error", error_msg)

    # ---------- Step 2: Report ----------
    def generate_reports(self):
        try:
            save_csv(self.scraped_data, "report.csv")
            save_pdf(self.scraped_data, "report.pdf", title="Daily Quotes Report")
            self.report_status.config(text="Status: report.csv & report.pdf created", fg="green")
            self.log("CSV and PDF reports generated successfully.")
            self.email_btn.config(state="normal")
        except Exception as e:
            self.report_status.config(text="Status: Failed", fg="red")
            self.log(f"Report generation failed: {e}")
            messagebox.showerror("Report Error", str(e))

    # ---------- Step 3: Email ----------
    def start_email_thread(self):
        if not os.path.exists("report.pdf"):
            messagebox.showwarning("Missing Report", "Pehle report generate karein.")
            return

        self.email_btn.config(state="disabled")
        self.email_status.config(text="Status: Sending...", fg="orange")
        self.log("Sending email...")
        threading.Thread(target=self.run_email, daemon=True).start()

    def run_email(self):
        try:
            send_email_with_attachment(
                sender_email=self.sender_entry.get(),
                sender_password=self.password_entry.get(),
                receiver_email=self.receiver_entry.get(),
                subject="Automated Scraping Report",
                body=(
                    "Assalam o Alaikum,\n\n"
                    "Attached is the automatically generated report from today's "
                    "web scraping run.\n\nRegards,\nPython Automation Bot"
                ),
                attachment_path="report.pdf"
            )
            self.root.after(0, self.on_email_success)
        except Exception as e:
            self.root.after(0, lambda: self.on_email_failure(str(e)))

    def on_email_success(self):
        self.email_status.config(text="Status: Email sent!", fg="green")
        self.log("Email sent successfully.")
        self.email_btn.config(state="normal")
        messagebox.showinfo("Success", "Report emailed successfully!")

    def on_email_failure(self, error_msg):
        self.email_status.config(text="Status: Failed", fg="red")
        self.log(f"Email failed: {error_msg}")
        self.email_btn.config(state="normal")
        messagebox.showerror("Email Error", error_msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()
