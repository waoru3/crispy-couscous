"""
Script to crawl MEXC API documentation pages and save them as markdown files.
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
            file_path = docs_dir / f"{filename}.md"
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
    """Main function to crawl all MEXC API documentation pages."""

    # Define all the pages to crawl
    pages = [
        ("https://www.mexc.com/api-docs/spot-v3/introduction", "01_introduction"),
        ("https://www.mexc.com/api-docs/spot-v3/change-log", "02_change_log"),
        ("https://www.mexc.com/api-docs/spot-v3/faqs", "03_faqs"),
        ("https://www.mexc.com/api-docs/spot-v3/general-info", "04_general_info"),
        ("https://www.mexc.com/api-docs/spot-v3/market-data-endpoints", "05_market_data_endpoints"),
        ("https://www.mexc.com/api-docs/spot-v3/subaccount-endpoints", "06_subaccount_endpoints"),
        ("https://www.mexc.com/api-docs/spot-v3/spot-account-trade", "07_spot_account_trade"),
        ("https://www.mexc.com/api-docs/spot-v3/wallet-endpoints", "08_wallet_endpoints"),
        ("https://www.mexc.com/api-docs/spot-v3/websocket-market-streams", "09_websocket_market_streams"),
        ("https://www.mexc.com/api-docs/spot-v3/websocket-user-data-streams", "10_websocket_user_data_streams"),
        ("https://www.mexc.com/api-docs/spot-v3/rebate-endpoints", "11_rebate_endpoints"),
        ("https://www.mexc.com/api-docs/spot-v3/public-api-definitions", "12_public_api_definitions")
    ]

    print("Starting MEXC API documentation crawling...")

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

        print(f"\nCrawling completed: {successful}/{total} pages successfully saved")


if __name__ == "__main__":
    asyncio.run(main())