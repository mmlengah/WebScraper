from scraper.bright_data_scraper import AsyncBrightDataScraper

class AsyncExampleScraper(AsyncBrightDataScraper):
    async def process_page(self, url):
        await self.page.goto(url)
        # Use the querySelector to get the specific element and then extract its innerText
        text = await self.page.inner_text('body > div > h1')
        return text
