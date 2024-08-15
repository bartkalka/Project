import tkinter as tk
from tkinter import simpledialog
from scraper import scrape_jobs
from api_client import get_company_info
from utils import save_to_json

def main():
    # Create Tkinter dialog window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Get URL from user
    url = simpledialog.askstring("Input", "Enter the URL of the job listings page:")

    if url:
        jobs = scrape_jobs(url)

        api_url = 'https://api.example.com/company-info'  # Example API for fetching company info

        for job in jobs:
            company_info = get_company_info(api_url, job['company'])
            job['company_info'] = company_info

        save_to_json(jobs, 'data/output.json')

        print(f"Data saved to 'data/output.json'")
    else:
        print("No URL provided.")

if __name__ == "__main__":
    main()
