# Python Web Scraping and API Integration Project (Tkinter GUI)

This project demonstrates how to scrape data from websites using BeautifulSoup4 and how to interact with APIs in Python. The example includes scraping job listings from a website (URL input via a Tkinter dialog) and fetching additional information about the companies from an external API.
## Project Structure
Create the following directory structure:
```
python-scraping-api/
│
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── main.py
│   ├── scraper.py
│   ├── api_client.py
│   └── utils.py
├── data/
│   └── output.json
└── tests/
    ├── test_scraper.py
    ├── test_api_client.py
    └── test_utils.py
```
## Requirements

- Python 3.7+
- Requests
- BeautifulSoup4
- Tkinter (included with Python)

## Installation

Clone the repository:

```bash
git clone https://github.com/bartkalka/WEB_scraper
cd WEB_scraper
```
### Install the dependencies:
```
pip install -r requirements.txt
```
## Usage
To run the project:
```
python src/main.py
```
## Project Structure:
```
/WEB_scraper
│
├── src/: Contains the source code.
├── data/: Directory where output data is stored.
├── tests/: Unit tests for the project.
```
## Files

### `requirements.txt`

In the `python-scraping-api` directory, create a `requirements.txt` file with the following content:
```
beautifulsoup4==4.12.2
requests==2.31.0
```


### `src/scraper.py`

In the `src` directory, create a `scraper.py` file with the following code:

```python
import requests
from bs4 import BeautifulSoup

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_elem in soup.find_all('div', class_='job-listing'):
        title = job_elem.find('h2').text.strip()
        company = job_elem.find('div', class_='company').text.strip()
        location = job_elem.find('div', class_='location').text.strip()
        jobs.append({'title': title, 'company': company, 'location': location})

    return jobs
```
### `src/api_client.py`

In the `src` directory, create an `api_client.py` file with the following code:

```python
import requests

def get_company_info(api_url, company_name):
    response = requests.get(f'{api_url}?query={company_name}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
```
### `src/utils.py`

In the `src` directory, create a `utils.py` file with the following code:

```python
import json

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
```
### `src/main.py`

In the `src` directory, create a `main.py` file with the following code:

```python
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
```
### `tests/test_scraper.py`

In the `test` directory, create a `test_scraper.py` file with the following code:

```python
import unittest
from scraper import scrape_jobs

class TestScraper(unittest.TestCase):
    def test_scrape_jobs(self):
        # Example test (adjust to your actual website)
        url = 'https://example.com/jobs'
        jobs = scrape_jobs(url)
        self.assertIsInstance(jobs, list)

if __name__ == '__main__':
    unittest.main()
```

### `.gitignore`

In the `python-scraping-api` directory, create a `.gitignore` file with the following content:

```bash
__pycache__/
*.pyc
data/output.json
```

## Install Required Libraries
Navigate to the project directory and install the required libraries:
```bash
cd E:\GIThub\Project\WEB_scraper\python-scraping-api.git
pip install -r requirements.txt
```




