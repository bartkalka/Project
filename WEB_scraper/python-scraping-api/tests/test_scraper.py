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
