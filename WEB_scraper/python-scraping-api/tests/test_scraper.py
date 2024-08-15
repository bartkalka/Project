import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraper import scrape_jobs

class TestScraper(unittest.TestCase):
    def test_scrape_jobs(self):
        # Example test (adjust to your actual website)
        url = 'https://example.com/jobs'
        jobs = scrape_jobs(url)
        self.assertIsInstance(jobs, list)

if __name__ == '__main__':
    unittest.main()
