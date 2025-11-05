# Book Scraper

This is a small Python script example that scrapes book details from the example site **books.toscrape.com**. This repository contains a simple scraper (`scrape_books.py`) that fetches book title, price, availability, rating, and the product URL from a single catalogue page and saves the results to `books.csv` and `books.json`.

---

## Prerequisites

-   Python 3.8+ recommended
-   A working internet connection (the example targets `http://books.toscrape.com/`)

Required Python packages:

    requests
    beautifulsoup4
    lxml
    pandas

---

## Installation

1. Clone this repository from your terminal:

```
git clone https://github.com/dre86dre/book_scraper.git
```

2. Navigate to the folder:

```
cd book_scraper
```

3. (Optional) Create and activate a virtual environment named **bs4_env**:

```
python -m venv bs4_env

# macOS / Linux
source bs4_env/bin/activate

# Windows (PowerShell)
bs4_env\Scripts\Activate.ps1
```

---



