# 🤖 Auto Scraper → Report → Email Automation

A Python automation pipeline that **scrapes live web data**, **generates polished PDF/CSV reports**, and **emails them automatically** — all through a clean, beginner-friendly Tkinter GUI.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📌 Overview

This project demonstrates a real-world automation workflow used in data collection, reporting, and notification systems — the same core pattern behind tools like scheduled analytics reports, price trackers, and monitoring bots.

**The pipeline does three things automatically:**

1. **Scrape** — pulls structured data (quotes, authors, tags) from a live website
2. **Generate** — converts that data into a clean CSV file and a formatted PDF report
3. **Deliver** — emails the finished report as an attachment, no manual steps required

---

## ✨ Features

- 🌐 Live web scraping with `requests` + `BeautifulSoup`
- 📄 Auto-generated CSV and PDF reports with `fpdf2`
- 📧 Automated email delivery via Gmail SMTP (`smtplib`)
- 🖥️ Interactive Tkinter GUI with live activity logging
- ⚡ Multi-threaded GUI — scraping/emailing never freezes the window
- 🔧 Easily adaptable to scrape any other website

---

## 🛠️ Tech Stack

| Purpose | Library |
|---|---|
| HTTP requests | `requests` |
| HTML parsing | `beautifulsoup4` |
| PDF/CSV generation | `fpdf2` |
| Email delivery | `smtplib` (built-in) |
| GUI | `tkinter` (built-in) |

---

## 🏗️ How It Works

```
 [ Website ]  --requests-->  [ scraper.py ]
                                    |
                                    v
                          [ report_generator.py ]
                            (creates .csv + .pdf)
                                    |
                                    v
                            [ mailer.py ]
                          (sends via Gmail SMTP)
                                    |
                                    v
                             📧 Inbox / Report
```

All three stages are wired together in `main.py` (CLI) or `gui.py` (interactive GUI).

---

## 📂 Project Structure

```
auto_report_project/
├── scraper.py            # Scrapes data from the target website
├── report_generator.py   # Builds the CSV and PDF report
├── mailer.py              # Sends the report via email
├── config.py               # Email credentials (kept out of version control)
├── main.py                 # Command-line pipeline
├── gui.py                    # Tkinter GUI version
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ayeshamumtaz1057/python-scraping-automation.git
cd python-scraping-automation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up a Gmail App Password
Gmail blocks plain-password logins for security, so a dedicated App Password is required:

1. Enable **2-Step Verification**: https://myaccount.google.com/security
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Copy the 16-character code generated

### 4. Add your credentials to `config.py`
```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_APP_PASSWORD = "your_16_char_app_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"
```

> ⚠️ **Security note:** Never commit real credentials. For production use, load these from environment variables instead of hardcoding them:
> ```python
> import os
> SENDER_EMAIL = os.getenv("SENDER_EMAIL")
> SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD")
> ```

---

## ▶️ Usage

**Option A — GUI (recommended for demos)**
```bash
python gui.py
```
Click through the three steps in order: **Scrape Now → Generate CSV + PDF → Send Email**, and watch progress in the live activity log.

**Option B — Command line**
```bash
python main.py
```
Runs the entire pipeline in one go: scrape → generate report → send email.

---

## 🎯 Customizing for Another Website

To point this at a different site, edit `scraper.py`:
1. Change `BASE_URL` to the target site
2. Inspect the page (`Ctrl+Shift+I`) to find the relevant HTML tag/class names
3. Update the `BeautifulSoup` selectors accordingly

---

## 📚 Key Concepts Demonstrated

- Web scraping & HTML parsing
- File I/O and structured data export (CSV/PDF)
- SMTP email automation
- GUI development with threading (non-blocking UI)
- Clean separation of concerns (scraper / report / mailer / interface)

---

## ⚖️ Note on Ethical Scraping

This project scrapes [quotes.toscrape.com](https://quotes.toscrape.com), a site built specifically for scraping practice. When adapting this for real-world websites, always check their `robots.txt` and Terms of Service before scraping.

---

## 👩‍💻 Author

**Ayesha Mumtaz**
[GitHub](https://github.com/ayeshamumtaz1057)

---

## 📄 License

This project is open-sourced for educational purposes under the MIT License.
