#!/usr/bin/env python3
"""
Daily Log Comment Processor
Appends daily log entries to README.md in the format:
**DAY N**:
MESSAGE
"""

import sys
import re
from pathlib import Path

def extract_log_message(comment_body):
    """
    Extract the message after 'Daily Log:' from the comment
    """
    match = re.search(r'Daily Log:\s*(.+)', comment_body, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_next_day_number(readme_content):
    """
    Find the highest existing **DAY N**: and return N+1
    """
    pattern = re.compile(r'\*\*DAY\s+(\d+)\*\*:', re.MULTILINE)
    nums = [int(n) for n in pattern.findall(readme_content)]
    return (max(nums) + 1) if nums else 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python logday.py '<comment_body>' [username]")
        sys.exit(1)
    
    comment_body = sys.argv[1]
    username = sys.argv[2] if len(sys.argv) > 2 else 'user'
    
    # Extract the log message
    log_message = extract_log_message(comment_body)
    if not log_message:
        print("No 'Daily Log:' found in comment")
        sys.exit(0)
    
    readme_path = Path('README.md')
    if not readme_path.exists():
        print("README.md not found")
        sys.exit(1)
    
    # Read current README content
    readme_content = readme_path.read_text(encoding='utf-8')
    
    # Get next day number
    next_day = get_next_day_number(readme_content)
    
    # Format the new entry
    new_entry = f"**DAY {next_day}**:\n{log_message}"
    
    # Append to README
    if not readme_content.endswith('\n'):
        readme_content += '\n'
    
    updated_content = readme_content + '\n' + new_entry + '\n'
    
    # Write back to README
    readme_path.write_text(updated_content, encoding='utf-8')
    
    print(f"Added DAY {next_day} entry to README.md")

if __name__ == '__main__':
    main()
