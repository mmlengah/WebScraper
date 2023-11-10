import asyncio
from credential_loader.credential_loader import CredentialLoader
from task_manager.task_manager import AsyncTaskManager
from scraper.example_scraper import AsyncExampleScraper

class WebScraper:
    def __init__(self):
        self.credentialLoader = CredentialLoader()   
        self.exampleScraper = AsyncExampleScraper(self.credentialLoader.load_credentials(), country="gb")
        self.taskManager = AsyncTaskManager(max_concurrent_tasks=10)
        # List of URLs to scrape
        self.urls = ["https://example.com"]

    # Method to determine the appropriate scraper function based on the URL
    def get_scraper_for_url(self, url):
        if "example.com" in url:
            return self.exampleScraper.scrape
        return None 
    
    # Asynchronous method to run the web scraping process
    async def run(self):
        for url in self.urls:
            scraper_function = self.get_scraper_for_url(url)
            if scraper_function:
                # If a scraper function is found, add the scraping task to the task manager
                await self.taskManager.add_task(scraper_function(url))
            else:
                # Print a message if no scraper is available for the current URL
                print(f"No scraper available for URL: {url}")
        
        # Await the completion of all tasks and retrieve results
        results = await self.taskManager.get_all_results()

        for result in results:
            print(result)

async def main():
    scraper = WebScraper()
    await scraper.run()

if __name__ == "__main__":
    # Run the asyncio event loop with the main function
    asyncio.run(main())
