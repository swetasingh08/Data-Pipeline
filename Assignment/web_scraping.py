"""
web_scraping.py
Part B: Scrape at least 20 books from Books to Scrape.
"""

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com"
OUTPUT_FILE = Path(__file__).with_name("books.json")

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def scrape_books(limit=20):
    """Scrape the first page and return the requested number of books."""
    response = requests.get(
        BASE_URL,
        headers={"User-Agent": "Python-Data-Engineering-Assignment/1.0"},
        timeout=15,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    book_cards = soup.select("article.product_pod")

    books = []

    for card in book_cards[:limit]:
        title_tag = card.select_one("h3 a")
        price_tag = card.select_one(".price_color")
        rating_tag = card.select_one("p.star-rating")

        title = title_tag.get("title", "").strip()
        price_text = price_tag.get_text(strip=True)
        rating_classes = rating_tag.get("class", [])
        rating_word = next(
            (item for item in rating_classes if item in RATING_MAP),
            "Unknown",
        )

        # Keep both the original price string and a numeric price.
        price = float(price_text.replace("£", "").strip())
        rating = RATING_MAP.get(rating_word, 0)

        books.append(
            {
                "title": title,
                "price": price_text,
                "rating": rating_word,
                "rating_numeric": rating,
                "price_numeric": price,
            }
        )

    if len(books) < limit:
        raise RuntimeError(
            f"Only {len(books)} books were found; expected at least {limit}."
        )

    return books


def save_json(data, filename):
    """Save scraped data to JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def analyze_books(books):
    """Print the required book price analysis."""
    prices = [book["price_numeric"] for book in books]

    most_expensive = max(books, key=lambda book: book["price_numeric"])
    least_expensive = min(books, key=lambda book: book["price_numeric"])
    average_price = sum(prices) / len(prices)

    print("\n=== BOOK ANALYSIS ===")
    print(f"Most expensive: {most_expensive['title']} (£{most_expensive['price_numeric']:.2f})")
    print(f"Least expensive: {least_expensive['title']} (£{least_expensive['price_numeric']:.2f})")
    print(f"Average price: £{average_price:.2f}")


def main():
    books = scrape_books(limit=20)

    print("=== WEB SCRAPING ===")
    print(f"Books scraped: {len(books)}")

    for number, book in enumerate(books, start=1):
        print(
            f"{number:02d}. {book['title']} | "
            f"{book['price']} | "
            f"Rating: {book['rating_numeric']}"
        )

    analyze_books(books)
    save_json(books, OUTPUT_FILE)
    print(f"\nSaved scraped data to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
