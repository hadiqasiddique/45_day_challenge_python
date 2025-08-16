import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url):
    try:
        # Fetch webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises error if request failed

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract heading
        heading = soup.find("h1").get_text(strip=True) if soup.find("h1") else "No H1 found"

        # Extract all paragraphs
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        # Display in terminal
        print(f"\nPage Heading: {heading}\n")
        print("Paragraphs found:\n")
        for para in paragraphs:
            print("-", para)

        # Save to CSV
        with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Heading", "Paragraph"])
            for para in paragraphs:
                writer.writerow([heading, para])

        print("\nData saved to 'scraped_data.csv' successfully!")

    except requests.exceptions.RequestException as e:
        print(f" Error fetching data: {e}")

if __name__ == "__main__":
    scrape_data("https://httpbin.org/html")


