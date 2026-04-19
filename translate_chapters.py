#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
星际迷航：伟大的触碰 - 章节提取和翻译辅助脚本
"""

import os
import re

# 读取原文文件
with open('/workspace/Star-Trek-A-Touch-of-Greatness.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 查找所有章节的位置
chapter_pattern = r'^(Prologue|CHAPTER\s+(?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN|SIXTEEN|SEVENTEEN|EIGHTEEN|NINETEEN|TWENTY(?:-ONE|-TWO|-THREE|-FOUR|-FIVE|-SIX|-SEVEN|-EIGHT|-NINE)?|THIRTY(?:-ONE|-TWO)?)?)\s*$'
chapters = []

for match in re.finditer(chapter_pattern, content, re.MULTILINE):
    chapter_title = match.group(1)
    start_pos = match.start()
    chapters.append((chapter_title, start_pos))

print(f"找到 {len(chapters)} 个章节/部分:")
for i, (title, pos) in enumerate(chapters):
    end_pos = chapters[i+1][1] if i+1 < len(chapters) else len(content)
    chapter_content = content[pos:end_pos]
    line_count = chapter_content.count('\n')
    print(f"{i+1}. {title} - 起始位置: {pos}, 行数: {line_count}")

# 创建章节目录映射
chapter_map = {
    'Prologue': ('00-序章.md', 57, 114),
    'CHAPTER ONE': ('01-第一章.md', 115, 506),
    'CHAPTER TWO': ('02-第二章.md', 507, 1228),
    'CHAPTER THREE': ('03-第三章.md', 1229, 1772),
    'CHAPTER FOUR': ('04-第四章.md', 1773, 2212),
    'CHAPTER FIVE': ('05-第五章.md', 2213, 2442),
    'CHAPTER SIX': ('06-第六章.md', 2443, 2782),
    'CHAPTER SEVEN': ('07-第七章.md', 2783, 3322),
    'CHAPTER EIGHT': ('08-第八章.md', 3323, 3606),
    'CHAPTER NINE': ('09-第九章.md', 3607, 3999),
    'CHAPTER TEN': ('10-第十章.md', 4000, 4598),
    'CHAPTER ELEVEN': ('11-第十一章.md', 4599, 5018),
    'CHAPTER TWELVE': ('12-第十二章.md', 5019, 5382),
    'CHAPTER THIRTEEN': ('13-第十三章.md', 5383, 5840),
    'CHAPTER FOURTEEN': ('14-第十四章.md', 5841, 6104),
    'CHAPTER FIFTEEN': ('15-第十五章.md', 6105, 6634),
    'CHAPTER SIXTEEN': ('16-第十六章.md', 6635, 7078),
    'CHAPTER SEVENTEEN': ('17-第十七章.md', 7079, 7500),
    'CHAPTER EIGHTEEN': ('18-第十八章.md', 7501, 8312),
    'CHAPTER NINETEEN': ('19-第十九章.md', 8313, 8818),
    'CHAPTER TWENTY': ('20-第二十章.md', 8819, 9498),
    'CHAPTER TWENTYONE': ('21-第二十一章.md', 9499, 10530),
    'CHAPTER TWENTY TWO': ('22-第二十二章.md', 10531, 11418),
    'CHAPTER TWENTY THREE': ('23-第二十三章.md', 11419, 12864),
    'CHAPTER TWENTYFOUR': ('24-第二十四章.md', 12865, 13790),
    'CHAPTER TWENTYFIVE': ('25-第二十五章.md', 13791, 14160),
    'CHAPTER TWENTYSIX': ('26-第二十六章.md', 14161, 15252),
    'CHAPTER TWENTYSEVEN': ('27-第二十七章.md', 15253, 15556),
    'CHAPTER TWENTYEIGHT': ('28-第二十八章.md', 15557, 15960),
    'CHAPTER TWENTYNINE': ('29-第二十九章.md', 15961, 16692),
    'CHAPTER THIRTY': ('30-第三十章.md', 16693, 17012),
    'CHAPTER THIRTYONE': ('31-第三十一章.md', 17013, 17402),
    'CHAPTER THIRTYTWO': ('32-第三十二章.md', 17403, 17954),
}

print("\n\n章节文件映射:")
for eng, (filename, start, end) in chapter_map.items():
    print(f"{eng} -> {filename} (行 {start}-{end})")
