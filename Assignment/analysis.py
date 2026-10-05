"""
analysis.py
Part D: Perform user and book analysis from the generated JSON files.
"""

import json
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_json(filename):
    with open(BASE_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_users(users):
    companies = [user["company"] for user in users]
    unique_companies = sorted(set(companies))

    # Top 5 companies alphabetically, as requested.
    top_5_companies = sorted(unique_companies)[:5]

    print("=== USER ANALYSIS ===")
    print(f"Total users: {len(users)}")
    print(f"Unique companies: {len(unique_companies)}")
    print("Top 5 companies (alphabetically):")
    for company in top_5_companies:
        print(f"- {company}")


def analyze_books(books):
    prices = [book["price_numeric"] for book in books]
    average_price = sum(prices) / len(prices) if prices else 0

    highest_rating = max(
        (book["rating_numeric"] for book in books),
        default=0,
    )
    highest_rated_books = [
        book["title"]
        for book in books
        if book["rating_numeric"] == highest_rating
    ]

    rating_counts = Counter(book["rating_numeric"] for book in books)

    print("\n=== BOOK ANALYSIS ===")
    print(f"Average price: £{average_price:.2f}")
    print(f"Highest rating: {highest_rating}")
    print("Highest-rated books:")
    for title in highest_rated_books:
        print(f"- {title}")

    print("\nNumber of books in each rating category:")
    for rating in range(1, 6):
        print(f"Rating {rating}: {rating_counts.get(rating, 0)} book(s)")


def main():
    users = load_json("users.json")
    books = load_json("books.json")

    analyze_users(users)
    analyze_books(books)


if __name__ == "__main__":
    main()
