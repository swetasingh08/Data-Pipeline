"""
json_processing.py
Part C: Load users.json and books.json, filter records, and create report.json.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "users.json"
BOOKS_FILE = BASE_DIR / "books.json"
REPORT_FILE = BASE_DIR / "report.json"


def load_json(filename):
    """Load and return JSON data."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def create_report(users, books):
    """Create the combined JSON report required by the assignment."""
    prices = [book["price_numeric"] for book in books]

    return {
        "total_users": len(users),
        "total_books": len(books),
        "average_price": round(sum(prices) / len(prices), 2) if prices else 0,
    }


def main():
    users = load_json(USERS_FILE)
    books = load_json(BOOKS_FILE)

    print("=== JSON PROCESSING ===")
    print(f"Total records in users.json: {len(users)}")
    print(f"Total records in books.json: {len(books)}")

    print("\nBooks with rating greater than 4:")
    high_rated_books = [
        book for book in books if book["rating_numeric"] > 4
    ]
    if high_rated_books:
        for book in high_rated_books:
            print(f"- {book['title']} (Rating: {book['rating_numeric']})")
    else:
        print("No books with rating greater than 4.")

    print("\nUsers whose company name contains 'Group':")
    group_users = [
        user for user in users if "group" in user["company"].lower()
    ]
    if group_users:
        for user in group_users:
            print(f"- {user['name']} | {user['company']}")
    else:
        print("No matching users found.")

    report = create_report(users, books)

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("\nCombined report:")
    print(json.dumps(report, indent=4))
    print(f"\nSaved report to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
