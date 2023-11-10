from playwright.async_api import async_playwright

class AsyncBrightDataScraper:
    def __init__(self, credentials, country="gb"):
        auth = f"{credentials['username']}-country-{country}:{credentials['password']}"
        self.sbr_ws_cdp = f"wss://{auth}@{credentials['host']}"
        self.browser = None
        self.page = None

    async def scrape(self, url):
        async with async_playwright() as pw:
            print('Connecting to Scraping Browser...')
            self.browser = await pw.chromium.connect_over_cdp(self.sbr_ws_cdp)
            self.page = await self.browser.new_page()
            try:
                print('Connected! Navigating...')
                return await self.process_page(url)
            finally:
                await self.browser.close()

    async def process_page(self, url):
        raise NotImplementedError("The process_page method must be overridden by a subclass.")