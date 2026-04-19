#!/usr/bin/env python3
import os
import re

# Read the original file
with open('Star-Trek-A-Touch-of-Greatness.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all chapter positions
chapter_pattern = r'^chapter\s+\d+'
chapters = []
for match in re.finditer(chapter_pattern, content, re.MULTILINE | re.IGNORECASE):
    chapters.append((match.start(), match.group()))

# Also find Prologue
prologue_match = re.search(r'^Prologue', content, re.MULTILINE | re.IGNORECASE)
if prologue_match:
    chapters.insert(0, (prologue_match.start(), 'Prologue'))

print(f"Found {len(chapters)} sections:")
for i, (pos, title) in enumerate(chapters):
    # Get end position
    end_pos = chapters[i+1][0] if i+1 < len(chapters) else len(content)
    section_text = content[pos:end_pos].strip()
    line_count = section_text.count('\n') + 1
    print(f"{i}: {title} (lines: ~{line_count}, pos: {pos}-{end_pos})")
