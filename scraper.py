"""
scraper.py
----------
Scrapes quotes from https://quotes.toscrape.com
(a website made specifically for practicing web scraping - safe & legal to scrape)
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes(pages=2):
    """
    Scrape quotes from the given number of pages.
    Returns a list of dictionaries: {quote, author, tags}
    """
    all_quotes = []

    for page in range(1, pages + 1):
        url = f"{BASE_URL}/page/{page}/"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Page {page} not found, stopping.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quote_blocks = soup.find_all("div", class_="quote")

        if not quote_blocks:
            break

        for block in quote_blocks:
            text = block.find("span", class_="text").get_text(strip=True)
            author = block.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in block.find_all("a", class_="tag")]

            all_quotes.append({
                "quote": text,
                "author": author,
                "tags": ", ".join(tags)
            })

        print(f"Page {page} scraped: {len(quote_blocks)} quotes found.")

    return all_quotes


if __name__ == "__main__":
    quotes = scrape_quotes(pages=2)
    for q in quotes:
        print(q)
