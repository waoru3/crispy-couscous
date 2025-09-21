#!/usr/bin/env python3
"""
Script to clean up MEXC API documentation markdown files.
Removes navigation headers, anchor links, and other HTML artifacts from scraped content.
"""

import os
import re
import json
from pathlib import Path
from typing import List

def clean_markdown_content(content: str) -> str:
    """Clean markdown content by removing navigation and HTML artifacts."""
    lines = content.split('\n')

    # Find the start of actual content (first # heading)
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('# '):
            content_start = i
            break

    if content_start == 0:
        print("Warning: No main heading found, keeping original content")
        return content

    # Keep only content from the main heading onwards
    cleaned_lines = lines[content_start:]

    # Join back to string for regex processing
    cleaned_content = '\n'.join(cleaned_lines)

    # Remove anchor links with "Direct link to" pattern
    cleaned_content = re.sub(r'\[​\]\([^)]+\s+"Direct link to[^"]*"\)', '', cleaned_content)

    # Remove "Next" navigation links at the end
    cleaned_content = re.sub(r'\[Next [^\]]+\]\([^)]+\)', '', cleaned_content)

    # Remove table of contents links at the end (lines starting with "- [" that are navigation)
    lines = cleaned_content.split('\n')

    # Find where navigation links start at the end (after content)
    nav_start = len(lines)
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i].strip()
        if line.startswith('- [') and 'api-docs' in line:
            nav_start = i
        elif line and not line.startswith('- ['):
            break

    # Remove navigation links at the end
    if nav_start < len(lines):
        lines = lines[:nav_start]

    # Clean up any trailing empty lines
    while lines and not lines[-1].strip():
        lines.pop()

    # Fix JSON formatting in code blocks
    content_with_fixed_json = fix_json_in_code_blocks('\n'.join(lines))

    return content_with_fixed_json

def fix_json_in_code_blocks(content: str) -> str:
    """Fix JSON formatting inside code blocks."""
    # Pattern to match code blocks that contain JSON-like content
    code_block_pattern = r'```(?:json)?\s*\n(.*?)\n```'

    def format_json_block(match):
        json_content = match.group(1)

        # Check if this looks like JSON (contains braces and quotes)
        if '{' in json_content and '"' in json_content:
            try:
                # Clean up the malformed JSON first
                cleaned = json_content.strip()
                # Remove trailing spaces from each line
                lines = [line.rstrip() for line in cleaned.split('\n')]
                cleaned = '\n'.join(lines)

                # Fix common JSON formatting issues
                cleaned = re.sub(r'{\s*\n?', '{', cleaned)
                cleaned = re.sub(r'\n?\s*}', '}', cleaned)
                cleaned = re.sub(r'"\s*:', '": ', cleaned)
                cleaned = re.sub(r':\s*(["{])', r': \1', cleaned)
                cleaned = re.sub(r',\s*\n?', ', ', cleaned)
                cleaned = re.sub(r'}\s*,', '}, ', cleaned)

                # Try to parse as JSON
                parsed = json.loads(cleaned)
                formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
                return f'```json\n{formatted}\n```'
            except (json.JSONDecodeError, ValueError):
                # Return cleaned up version even if not valid JSON
                pass

        # Return original with basic cleanup
        return f'```\n{json_content}\n```'

    # Apply the JSON formatting to all code blocks
    return re.sub(code_block_pattern, format_json_block, content, flags=re.DOTALL)

def clean_markdown_file(file_path: Path) -> bool:
    """Clean a single markdown file."""
    try:
        # Read the original content
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Clean the content
        cleaned_content = clean_markdown_content(original_content)

        # Write back the cleaned content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"✓ Cleaned: {file_path}")
        return True

    except Exception as e:
        print(f"✗ Error cleaning {file_path}: {e}")
        return False

def clean_docs_folder(docs_path: str) -> None:
    """Clean all markdown files in the docs folder."""
    docs_dir = Path(docs_path)

    if not docs_dir.exists():
        print(f"Error: Directory {docs_path} does not exist")
        return

    # Find all markdown files
    md_files = []
    for subfolder in ['SpotV3', 'Futures']:
        subfolder_path = docs_dir / subfolder
        if subfolder_path.exists():
            md_files.extend(subfolder_path.glob('*.md'))

    if not md_files:
        print("No markdown files found to clean")
        return

    print(f"Found {len(md_files)} markdown files to clean")
    print("-" * 50)

    # Clean each file
    success_count = 0
    for md_file in sorted(md_files):
        if clean_markdown_file(md_file):
            success_count += 1

    print("-" * 50)
    print(f"Successfully cleaned {success_count}/{len(md_files)} files")

def main():
    """Main function."""
    # Get the docs directory relative to this script
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent / "docs"

    print("MEXC API Documentation Markdown Cleaner")
    print("=" * 50)
    print(f"Cleaning files in: {docs_dir}")

    clean_docs_folder(str(docs_dir))
    print("\nCleaning complete!")

if __name__ == "__main__":
    main()