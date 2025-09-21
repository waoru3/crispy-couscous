import importlib
import inspect
import pkgutil
import sys

def try_import_attr(module_name: str, attr_name: str):
    try:
        module = importlib.import_module(module_name)
        attr = getattr(module, attr_name)
        print(f"OK {module_name}.{attr_name}: {type(attr)}")
        return True
    except Exception as e:
        print(f"FAIL {module_name}.{attr_name}: {e}")
        return False

def main() -> None:
    try:
        import crawl4ai  # type: ignore
    except Exception as e:
        print(f"Unable to import crawl4ai: {e}")
        sys.exit(1)

    print(f"crawl4ai module path: {getattr(crawl4ai, '__file__', 'unknown')}")
    print("Top-level attributes:", sorted([n for n in dir(crawl4ai) if not n.startswith('_')]))

    # Probe common classes used in docs/examples
    candidates = [
        ("crawl4ai", "AsyncWebCrawler"),
        ("crawl4ai", "CrawlerRunConfig"),
        ("crawl4ai", "DefaultMarkdownProcessor"),
        ("crawl4ai", "CacheMode"),
        ("crawl4ai", "BrowserConfig"),
        ("crawl4ai", "WebCrawler"),
        ("crawl4ai", "MarkdownGenerationConfig"),
    ]

    for module_name, attr_name in candidates:
        try_import_attr(module_name, attr_name)

    # List submodules, if any
    if hasattr(crawl4ai, "__path__"):
        submods = [m.name for m in pkgutil.iter_modules(crawl4ai.__path__)]
        print("crawl4ai submodules:", submods)

if __name__ == "__main__":
    main()


