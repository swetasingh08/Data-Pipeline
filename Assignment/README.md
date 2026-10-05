# Data Collection and Processing Using JSON, APIs and Web Scraping

## Course
Python for Data Engineering

## Project Type
Individual Assignment

## Overview

This project implements a small data collection and processing pipeline for an EdTech company scenario.

The pipeline collects:

1. User information from a REST API.
2. Book information from a web page.
3. Stores processed data in JSON files.
4. Loads and processes the JSON data.
5. Performs basic data analysis.
6. Generates a combined JSON report.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- JSON
- Collections
- pathlib

## Data Sources

### API

JSONPlaceholder users endpoint:

`https://jsonplaceholder.typicode.com/users`

The API provides sample user records containing fields such as name, username, email, and company information.

### Website

Books to Scrape:

`https://books.toscrape.com`

The project extracts the first 20 book records from the website.

## Project Structure

```text
Assignment/
│
├── api_data.py
├── web_scraping.py
├── json_processing.py
├── analysis.py
├── main.py
│
├── users.json
├── books.json
├── report.json
│
└── README.md
```

## Installation

Open a terminal inside the Assignment directory.

Install the required packages:

```bash
pip install requests beautifulsoup4
```

## Part A - API Data Collection

Run:

```bash
python api_data.py
```

The program:

- Fetches all users.
- Displays name, email and company.
- Counts users.
- Extracts company names.
- Creates a processed dictionary for every user.
- Saves the result to `users.json`.

## Part B - Web Scraping

Run:

```bash
python web_scraping.py
```

The program:

- Requests the Books to Scrape website.
- Parses the HTML using BeautifulSoup.
- Extracts 20 book titles.
- Extracts prices.
- Extracts ratings.
- Converts rating words to numbers.
- Calculates the most expensive book.
- Calculates the least expensive book.
- Calculates the average price.
- Saves the result to `books.json`.

Rating conversion:

```text
One   -> 1
Two   -> 2
Three -> 3
Four  -> 4
Five  -> 5
```

## Part C - JSON Processing

Run:

```bash
python json_processing.py
```

The program:

- Loads `users.json`.
- Loads `books.json`.
- Counts records.
- Displays books with rating greater than 4.
- Finds users whose company name contains `Group`.
- Creates `report.json`.

Example report structure:

```json
{
    "total_users": 10,
    "total_books": 20,
    "average_price": 35.12
}
```

The exact average price depends on the data retrieved when the scraper is executed.

## Part D - Data Analysis

Run:

```bash
python analysis.py
```

The program displays:

### User Analysis

- Total users
- Number of unique companies
- Five company names in alphabetical order

### Book Analysis

- Average price
- Highest rating
- Highest-rated books
- Number of books for ratings 1 through 5

## Bonus - Menu Driven Program

Run:

```bash
python main.py
```

The menu contains:

```text
1. Fetch API Data
2. Scrape Book Data
3. Generate JSON Files
4. Analyze Data
5. Exit
```

This provides a simple end-to-end interface for running the pipeline.

## ETL Pipeline

The project follows a basic ETL pattern:

```text
Extract
   |
   +---- REST API
   |
   +---- Web Scraping
          |
          v
Transform
   |
   +---- Select required fields
   +---- Clean price values
   +---- Convert ratings to numbers
   |
   v
Load
   |
   +---- users.json
   +---- books.json
   +---- report.json
   |
   v
Analyze
   |
   +---- User analysis
   +---- Book analysis
```

## Error Handling

The scripts use:

- HTTP status validation with `raise_for_status()`
- Request timeouts
- Missing-data defaults
- Validation that at least 20 books were scraped
- Exception handling in the menu-driven program

## Sample Expected Results

The API is expected to return 10 users.

The scraper collects 20 books from the first page.

The exact book prices, ratings, and calculated average should be taken from the generated `books.json` file at execution time.

## Screenshots for Submission

Take screenshots of:

1. API output from `api_data.py`
2. Scraping output from `web_scraping.py`
3. JSON processing output from `json_processing.py`
4. Analysis output from `analysis.py`
5. Menu-driven program from `main.py`
6. Generated `users.json`, `books.json`, and `report.json`

## Learning Outcomes

This project demonstrates:

- REST API consumption
- JSON parsing and serialization
- Web scraping
- HTML parsing
- Data cleaning
- Structured data storage
- Filtering
- Aggregation
- Basic exploratory data analysis
- ETL pipeline design
- Python modular programming

## Notes

This assignment is designed for educational purposes. The Books to Scrape website is intended as a practice website for web scraping exercises.

Run the scripts while connected to the internet because the API and website are external data sources.
