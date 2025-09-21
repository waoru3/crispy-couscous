"""
Script to crawl MEXC Futures API documentation pages and save them as markdown files.
"""
import asyncio
import os
from pathlib import Path
from crawl4ai import AsyncWebCrawler


async def crawl_and_save_page(crawler, url, filename):
    """Crawl a single page and save it as markdown."""
    try:
        print(f"Crawling: {url}")
        result = await crawler.arun(
            url=url,
            word_count_threshold=10,
            extraction_strategy="NoExtractionStrategy",
            chunking_strategy="NoClustering"
        )

        if result.success:
            # Create docs directory if it doesn't exist
            docs_dir = Path("docs")
            docs_dir.mkdir(exist_ok=True)

            # Save the markdown content
            file_path = docs_dir / f"futures_{filename}.md"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(result.markdown)

            print(f"✓ Saved: {file_path}")
            return True
        else:
            print(f"✗ Failed to crawl: {url}")
            return False

    except Exception as e:
        print(f"✗ Error crawling {url}: {str(e)}")
        return False


async def main():
    """Main function to crawl all MEXC Futures API documentation pages."""

    # Define all the futures pages to crawl
    pages = [
        ("https://www.mexc.com/api-docs/futures/update-log", "01_update_log"),
        ("https://www.mexc.com/api-docs/futures/integration-guide", "02_integration_guide"),
        ("https://www.mexc.com/api-docs/futures/error-code", "03_error_code"),
        ("https://www.mexc.com/api-docs/futures/market-endpoints", "04_market_endpoints"),
        ("https://www.mexc.com/api-docs/futures/account-and-trading-endpoints", "05_account_trading_endpoints"),
        ("https://www.mexc.com/api-docs/futures/websocket-api", "06_websocket_api")
    ]

    print("Starting MEXC Futures API documentation crawling...")

    async with AsyncWebCrawler(verbose=True) as crawler:
        tasks = []
        for url, filename in pages:
            task = crawl_and_save_page(crawler, url, filename)
            tasks.append(task)

        # Execute all crawling tasks concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Count successful crawls
        successful = sum(1 for result in results if result is True)
        total = len(pages)

        print(f"\nCrawling completed: {successful}/{total} futures pages successfully saved")


if __name__ == "__main__":
    asyncio.run(main())