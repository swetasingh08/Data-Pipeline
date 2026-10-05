"""
api_data.py
Part A: Fetch users from JSONPlaceholder, process them, and save users.json.
"""

import json
from pathlib import Path

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = Path(__file__).with_name("users.json")


def fetch_users():
    """Fetch all users from the API."""
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    return response.json()


def process_users(users):
    """Keep only the fields required by the assignment."""
    return [
        {
            "name": user.get("name", ""),
            "email": user.get("email", ""),
            "company": user.get("company", {}).get("name", "")
        }
        for user in users
    ]


def save_json(data, filename):
    """Save Python data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    users = fetch_users()
    processed_users = process_users(users)

    print("=== API DATA COLLECTION ===")
    print(f"Total users: {len(processed_users)}")
    print("\nUsers:")
    for user in processed_users:
        print(
            f"Name: {user['name']} | "
            f"Email: {user['email']} | "
            f"Company: {user['company']}"
        )

    companies = [user["company"] for user in processed_users]
    print("\nCompany names:")
    for company in companies:
        print(f"- {company}")

    save_json(processed_users, OUTPUT_FILE)
    print(f"\nSaved processed data to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
