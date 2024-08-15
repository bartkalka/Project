import tkinter as tk
from tkinter import simpledialog
from scraper import scrape_books
from utils import save_to_json

def main():
    # Create Tkinter dialog window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Get URL from user
    url = simpledialog.askstring("Input", "Enter the URL of the books page:")

    if url:
        try:
            print(f"Scraping URL: {url}")
            books = scrape_books(url)
            print(f"Books scraped: {books}")

            save_to_json(books, 'data/output.json')
            print(f"Data saved to 'data/output.json'")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No URL provided.")

if __name__ == "__main__":
    main()
