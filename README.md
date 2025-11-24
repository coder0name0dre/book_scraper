# Book Scraper

This is a small Python script example that scrapes book details from the example site **books.toscrape.com**. This repository contains a simple scraper (`book_scraper.py`) that fetches book title, price, availability, rating, and the product URL from a single catalogue page and saves the results to `books.csv` and `books.json`.

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
git clone https://github.com/coder0name0dre/book_scraper.git
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

## Usage

Run the script with Python:

``` 
python book_scraper.py
```

The script will:

1.  Visit the example catalogue page `catalogue/page-1.html` on `books.toscrape.com`.
2.  Extract links to each book on that page.
3.  Visit each book's detail page and extract title, price, availability, rating, and URL.
4.  Save the collected data to `books.csv` and `books.json` in the script's working directory.

You should see `Scraping: <book-url>` messages printed to your console as it runs.

---

## Script overview

The script is organised into small, single-purpose functions with a concise `__main__` runner:

-   `get_soup(url)` --- Fetches the HTML using `requests` and returns a BeautifulSoup object (parsed with `lxml`).
-   `get_book_links(page_url)` --- Parses a catalogue page for `<article class="product_pod">` elements and returns absolute book URLs.
-   `parse_book_page(book_url)` --- Visits an individual book page and extracts:
    -   `Title` --- from the `<h1>` element
    -   `Price` --- from `<p class="price_color">`
    -   `Availability` --- from `<p class="instock availability">`
    -   `Rating` --- parsed from the `class` attribute on `<p class="star-rating ...">`
-   Main runner --- builds the start page URL, collects book links, iterates through links, stores results in a list of dictionaries, and writes CSV/JSON files using `pandas`.

---

## Output files

-   `books.csv` --- CSV file with columns:
    `Title, Price, Availability, Rating, URL`.
-   `books.json` --- JSON array (records) with the same fields.

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/book_scraper/blob/main/LICENSE).

