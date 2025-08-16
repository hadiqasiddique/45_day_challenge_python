Title: Simple Python Web Scraper – Extract Headings & Paragraphs into CSV

📌 Features

 - Fetches a webpage from the internet.

- Reads the main heading (<h1>) and all paragraph texts (<p>).

- Shows them neatly in your terminal.

- Saves them into a CSV file for later use.

- Error-handling so it won’t crash if the site is down.

🛠 Requirements

- Before running the script, install dependencies:

- pip install requests beautifulsoup4

▶ How to Run

- Save the script as data_scraper.py.

- Open your terminal in the script’s folder.

Run:
python data_scraper.py

The program will:
Show the heading & paragraphs in your terminal.
Save them into scraped_data.csv.

📂 Output Files

Terminal Output: Shows heading and paragraphs.

CSV File: scraped_data.csv contains all scraped data in a table format.

Example

Terminal Output:

✅ Page Heading: Herman Melville - Moby-Dick

📜 Paragraphs found:

- Availing himself of the mild, summer-cool weather...
💾 Data saved to 'scraped_data.csv' successfully!

