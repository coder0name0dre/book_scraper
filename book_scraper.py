import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

# Base URL of the website to scrape
BASE_URL = "http://books.toscrape.com/"

def get_soup(url):
    # Fetch a web page's HTML and return a BeautifulSoup object for parsing.

    response = requests.get(url, timeout=10)        # Fetch page with 10-second timeout
    response.raise_for_status()                     # Raise an exception for HTTP errors
    return BeautifulSoup(response.text, "lxml")     # Parse with fast lxml parser


def get_book_links(page_url):
    # Extract all book detail page URLs from a single catalogue page.

    soup = get_soup(page_url)
    links = []

    # Each book is inside an <article class="product_pod"> element
    for article in soup.find_all("article", class_="product_pod"):
        href = article.h3.a["href"]          # Extract relative link from the <a> tag
        abs_url = urljoin(page_url, href)    # Convert to absolute URL
        links.append(abs_url)                # Store the full book URL

    return links


def parse_book_page(book_url):
    # Extract book details from a book's individual page.

    soup = get_soup(book_url)

    # Extract book title
    title = soup.find("h1").text.strip()

    # Extract price (e.g., '£51.77')
    price = soup.find("p", class_="price_color").text.strip()

    # Extract availability text (e.g., 'In stock (20 available)')
    availability = soup.find("p", class_="instock availability").get_text(strip=True)

    # Extract rating from CSS class name (e.g., 'star-rating Three')
    rating_tag = soup.find("p", class_="star-rating")
    rating = rating_tag["class"][1] if rating_tag and len(rating_tag["class"]) > 1 else "Unknown"

    # Return structured data for one book
    return {
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating,
        "URL": book_url
    }


if __name__ == "__main__":
    # Starting URL for the first catalogue page
    start_page = urljoin(BASE_URL, "catalogue/page-1.html")

    # Get all book links from that page
    book_links = get_book_links(start_page)

    books = []

    # Iterate through each book link and scrape data
    for link in book_links:
        print("Scraping:", link)
        data = parse_book_page(link)
        books.append(data)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(books)

    # Save scraped data to CSV and JSON formats
    df.to_csv("books.csv", index=False)
    df.to_json("books.json", orient="records", indent=2)

    print("\nSaved to books.csv and books.json")
