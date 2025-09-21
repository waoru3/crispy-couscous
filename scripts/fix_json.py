#!/usr/bin/env python3
"""
Simple script to fix JSON formatting in markdown code blocks.
"""

import json
import re
from pathlib import Path

def fix_json_in_file(file_path: Path) -> bool:
    """Fix JSON formatting in a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all code blocks (with or without language specification)
        pattern = r'```(?:json)?\s*\n((?:[^`]|`(?!``))*?)\n```'

        def fix_json_block(match):
            block_content = match.group(1).strip()

            # Handle simple empty object case
            if block_content == '{}':
                return '```json\n{}\n```'

            # Only process if it looks like JSON (has braces)
            if '{' in block_content:
                try:
                    # Handle multi-line JSON with potential formatting issues
                    lines = block_content.split('\n')
                    cleaned_lines = []
                    for line in lines:
                        cleaned_line = line.strip()
                        if cleaned_line:
                            cleaned_lines.append(cleaned_line)

                    # Try different approaches to parse JSON
                    json_candidates = [
                        ''.join(cleaned_lines),  # No spaces
                        ' '.join(cleaned_lines), # With spaces
                        block_content.strip()     # Original content
                    ]

                    for candidate in json_candidates:
                        try:
                            parsed = json.loads(candidate)
                            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
                            return f'```json\n{formatted}\n```'
                        except (json.JSONDecodeError, ValueError):
                            continue

                    # If parsing fails but looks like JSON, at least format it nicely
                    if block_content.count('{') > 0 and ('"' in block_content or "'" in block_content):
                        # Basic formatting for JSON-like content
                        formatted_lines = []
                        indent_level = 0
                        for line in lines:
                            line = line.strip()
                            if line:
                                if line.endswith('{'):
                                    formatted_lines.append('  ' * indent_level + line)
                                    indent_level += 1
                                elif line.startswith('}'):
                                    indent_level = max(0, indent_level - 1)
                                    formatted_lines.append('  ' * indent_level + line)
                                else:
                                    formatted_lines.append('  ' * indent_level + line)

                        if formatted_lines:
                            return f'```json\n{chr(10).join(formatted_lines)}\n```'

                except Exception:
                    pass

            # Return original if not JSON or processing failed
            return match.group(0)

        # Apply the fix
        fixed_content = re.sub(pattern, fix_json_block, content, flags=re.DOTALL)

        # Write back if changed
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"✓ Fixed JSON in: {file_path}")
            return True
        else:
            print(f"- No changes needed: {file_path}")
            return True

    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """Main function."""
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent / "docs"

    print("JSON Formatter for Markdown Files")
    print("=" * 40)

    # Find all markdown files
    md_files = []
    for subfolder in ['SpotV3', 'Futures']:
        subfolder_path = docs_dir / subfolder
        if subfolder_path.exists():
            md_files.extend(subfolder_path.glob('*.md'))

    if not md_files:
        print("No markdown files found")
        return

    print(f"Processing {len(md_files)} files...")

    success_count = 0
    for md_file in sorted(md_files):
        if fix_json_in_file(md_file):
            success_count += 1

    print(f"\nProcessed {success_count}/{len(md_files)} files successfully")

if __name__ == "__main__":
    main()