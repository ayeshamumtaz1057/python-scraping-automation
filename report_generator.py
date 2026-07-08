"""
report_generator.py
--------------------
Takes scraped data and turns it into a CSV file and a PDF report.
"""

import csv
from datetime import datetime
from fpdf import FPDF


def clean_text(text):
    """
    Replaces 'smart' typographic characters (curly quotes, em-dashes, etc.)
    with plain ASCII equivalents, since the default PDF font (Helvetica)
    does not support them.
    """
    replacements = {
        "\u2018": "'", "\u2019": "'",   # curly single quotes
        "\u201c": '"', "\u201d": '"',   # curly double quotes
        "\u2013": "-", "\u2014": "-",   # en-dash, em-dash
        "\u2026": "...",                # ellipsis
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text


def save_csv(data, filename="report.csv"):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV report saved as {filename}")


def save_pdf(data, filename="report.pdf", title="Scraped Data Report"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, title, ln=True, align="C")

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.cell(0, 8, f"Total records: {len(data)}", ln=True)
    pdf.ln(5)

    for i, item in enumerate(data, start=1):
        quote = clean_text(item["quote"])
        author = clean_text(item["author"])
        tags = clean_text(item["tags"])

        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "B", 11)
        pdf.multi_cell(0, 7, f'{i}. "{quote}"')

        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "I", 10)
        pdf.multi_cell(0, 6, f'   - {author}  (Tags: {tags})')
        pdf.ln(2)

    pdf.output(filename)
    print(f"PDF report saved as {filename}")
