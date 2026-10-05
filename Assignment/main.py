"""
main.py
Bonus: Menu-driven end-to-end data collection and analysis program.

Options:
1. Fetch API Data
2. Scrape Book Data
3. Generate JSON Files
4. Analyze Data
5. Exit
"""

import json
from pathlib import Path

from api_data import fetch_users, process_users, save_json
from web_scraping import scrape_books
from json_processing import create_report
from analysis import analyze_users, analyze_books

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "users.json"
BOOKS_FILE = BASE_DIR / "books.json"
REPORT_FILE = BASE_DIR / "report.json"


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def fetch_api_data():
    users = process_users(fetch_users())
    save_json(users, USERS_FILE)
    print(f"\nAPI data fetched successfully: {len(users)} users.")
    return users


def scrape_book_data():
    books = scrape_books(limit=20)
    save_json(books, BOOKS_FILE)
    print(f"\nBook data scraped successfully: {len(books)} books.")
    return books


def generate_json_files():
    if not USERS_FILE.exists():
        print("\nusers.json not found. Fetching API data first...")
        users = fetch_api_data()
    else:
        users = load_json(USERS_FILE)

    if not BOOKS_FILE.exists():
        print("\nbooks.json not found. Scraping books first...")
        books = scrape_book_data()
    else:
        books = load_json(BOOKS_FILE)

    report = create_report(users, books)
    save_json(report, REPORT_FILE)

    print("\nJSON files generated:")
    print(f"- {USERS_FILE.name}")
    print(f"- {BOOKS_FILE.name}")
    print(f"- {REPORT_FILE.name}")


def analyze_data():
    missing = [
        filename
        for filename in ("users.json", "books.json")
        if not (BASE_DIR / filename).exists()
    ]

    if missing:
        print(f"\nMissing file(s): {', '.join(missing)}")
        print("Please run options 1 and 2 first.")
        return

    users = load_json(USERS_FILE)
    books = load_json(BOOKS_FILE)

    analyze_users(users)
    analyze_books(books)


def main():
    while True:
        print("\n" + "=" * 45)
        print("DATA COLLECTION AND PROCESSING PIPELINE")
        print("=" * 45)
        print("1. Fetch API Data")
        print("2. Scrape Book Data")
        print("3. Generate JSON Files")
        print("4. Analyze Data")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        try:
            if choice == "1":
                fetch_api_data()
            elif choice == "2":
                scrape_book_data()
            elif choice == "3":
                generate_json_files()
            elif choice == "4":
                analyze_data()
            elif choice == "5":
                print("\nExiting program. Thank you!")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 5.")
        except Exception as error:
            print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()
