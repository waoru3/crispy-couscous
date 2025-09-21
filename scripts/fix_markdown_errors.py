#!/usr/bin/env python3
"""
Script to fix common markdown syntax errors in MEXC API documentation files.
"""

import os
import re
from pathlib import Path

def fix_markdown_content(content):
    """Fix common markdown syntax errors."""
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        # Fix 1: Remove backslashes at the end of table rows (but keep legitimate line breaks)
        # Only remove trailing backslashes that are followed by table separators
        if '|' in line and line.strip().endswith('\\'):
            # Check if this looks like a table row (has pipes)
            line = line.rstrip('\\').rstrip()

        # Fix 2: Fix double backslashes at end of lines to single backslashes
        # Only if they're not part of escaped characters
        if line.endswith('\\\\'):
            line = line[:-2] + '\\'

        # Fix 3: Fix malformed links like [](url)<url> to [text](url)
        # Pattern: [](url)<url> -> [url](url)
        link_pattern = r'\[\]\(([^)]+)\)<([^>]+)>'
        def fix_link(match):
            url1, url2 = match.groups()
            # Use the URL as the link text, or extract domain name
            link_text = url1.split('/')[-1] or url2.split('/')[-1] or url1
            if link_text.startswith('http'):
                # Extract domain name for cleaner text
                domain = re.search(r'https?://([^/]+)', link_text)
                if domain:
                    link_text = domain.group(1)
            return f'[{link_text}]({url1})'

        line = re.sub(link_pattern, fix_link, line)

        # Fix 4: Add missing spaces in common patterns
        # Fix missing spaces after punctuation
        line = re.sub(r'\.([A-Z])', r'. \1', line)
        line = re.sub(r',([A-Z])', r', \1', line)
        line = re.sub(r';([A-Z])', r'; \1', line)
        line = re.sub(r':([A-Z])', r': \1', line)

        # Fix missing spaces around operators and brackets
        line = re.sub(r'(\w)\(', r'\1 (', line)
        line = re.sub(r'\)(\w)', r') \1', line)

        # Fix missing spaces in markdown headers
        if line.startswith('#') and not line.startswith('## ') and not line.startswith('# '):
            line = re.sub(r'^(#+)(\w)', r'\1 \2', line)

        # Fix 5: Other common markdown formatting issues

        # Fix table header separators (ensure proper format)
        if re.match(r'^[-|:\s]+$', line):
            # This is a table separator line
            line = re.sub(r'[-:]+', lambda m: '---' if ':' not in m.group() else ':---:', line)

        # Fix list items (ensure proper spacing)
        if re.match(r'^\s*[-*+]\s*\w', line):
            line = re.sub(r'^(\s*[-*+])(\w)', r'\1 \2', line)

        # Fix numbered lists
        if re.match(r'^\s*\d+\.\s*\w', line):
            line = re.sub(r'^(\s*\d+\.)(\w)', r'\1 \2', line)

        # Fix code blocks (ensure proper spacing around backticks)
        line = re.sub(r'`([^`]+)`', lambda m: f'`{m.group(1).strip()}`', line)

        # Fix bold and italic formatting
        line = re.sub(r'\*\*([^*]+)\*\*', lambda m: f'**{m.group(1).strip()}**', line)
        line = re.sub(r'\*([^*]+)\*', lambda m: f'*{m.group(1).strip()}*', line)

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_markdown_file(file_path):
    """Fix markdown errors in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        fixed_content = fix_markdown_content(content)

        # Only write if content changed
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

    return False

def main():
    """Main function to fix all markdown files."""
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / 'docs'

    files_to_fix = [
        # Futures folder
        'Futures/01_update_log.md',
        'Futures/02_integration_guide.md',
        'Futures/03_error_code.md',
        'Futures/04_market_endpoints.md',
        'Futures/05_account_trading_endpoints.md',
        'Futures/06_websocket_api.md',

        # SpotV3 folder
        'SpotV3/01_introduction.md',
        'SpotV3/02_change_log.md',
        'SpotV3/03_faqs.md',
        'SpotV3/04_general_info.md',
        'SpotV3/05_market_data_endpoints.md',
        'SpotV3/06_subaccount_endpoints.md',
        'SpotV3/07_spot_account_trade.md',
        'SpotV3/08_wallet_endpoints.md',
        'SpotV3/09_websocket_market_streams.md',
        'SpotV3/10_websocket_user_data_streams.md',
        'SpotV3/11_rebate_endpoints.md',
        'SpotV3/12_public_api_definitions.md',
    ]

    fixed_count = 0
    total_count = 0

    for file_path in files_to_fix:
        full_path = docs_dir / file_path
        if full_path.exists():
            total_count += 1
            if fix_markdown_file(full_path):
                fixed_count += 1
                print(f"Fixed: {file_path}")
            else:
                print(f"No changes needed: {file_path}")
        else:
            print(f"File not found: {file_path}")

    print(f"\nCompleted: {fixed_count}/{total_count} files were modified")

if __name__ == '__main__':
    main()