#!/usr/bin/env python3
"""Fix math formula rendering using balanced-brace parser for \frac."""

import re
from pathlib import Path

BASE_DIR = Path("/home/mark/Documents/Scientia-Omnibus/formal-sciences/Basic/Arithmetic & Algebra Basics")


def skip_ws(text, pos):
    """Advance position past whitespace."""
    while pos < len(text) and text[pos] in ' \t\n\r':
        pos += 1
    return pos


def find_matching_brace(text, start):
    """Find matching } for { at position start. Returns position of } or -1."""
    if start >= len(text) or text[start] != '{':
        return -1
    depth = 1
    i = start + 1
    while i < len(text) and depth > 0:
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
        i += 1
    return i - 1 if depth == 0 else -1


def convert_frac_balanced(text):
    """Convert ALL \frac{...}{...} using balanced brace matching.
    Handles whitespace between tokens and nested fractions correctly."""
    replacements = []
    i = 0
    while i < len(text):
        idx = text.find('\\frac', i)
        if idx == -1:
            break
        
        # Skip whitespace between \frac and {
        pos = idx + 5
        pos = skip_ws(text, pos)
        if pos >= len(text) or text[pos] != '{':
            i = pos
            continue
        
        # First argument
        end1 = find_matching_brace(text, pos)
        if end1 == -1:
            i = pos + 1
            continue
        
        # Skip whitespace between } and {
        pos2 = end1 + 1
        pos2 = skip_ws(text, pos2)
        if pos2 >= len(text) or text[pos2] != '{':
            i = pos2
            continue
        
        # Second argument
        end2 = find_matching_brace(text, pos2)
        if end2 == -1:
            i = pos2 + 1
            continue
        
        arg1 = text[pos + 1:end1]
        arg2 = text[pos2 + 1:end2]
        
        replacements.append((idx, end2 + 1, arg1, arg2))
        i = end2 + 1
    
    # Apply replacements right-to-left (preserves positions)
    for idx, end, arg1, arg2 in reversed(replacements):
        arg1 = convert_frac_balanced(arg1.strip())
        arg2 = convert_frac_balanced(arg2.strip())
        html = f'<sup>{arg1}</sup>⁄<sub>{arg2}</sub>'
        text = text[:idx] + html + text[end:]
    
    return text


def convert_symbols(text):
    """Convert LaTeX symbols to readable form."""
    rules = [
        (r'\\cdot', '·'), (r'\\ge', '≥'), (r'\\le', '≤'),
        (r'\\ne', '≠'), (r'\\neq', '≠'), (r'\\dots', '…'),
        (r'\\times', '×'), (r'\\div', '÷'), (r'\\to', '→'),
        (r'\\rightarrow', '→'), (r'\\leftarrow', '←'),
        (r'\\infty', '∞'), (r'\\pi', 'π'), (r'\\approx', '≈'),
        (r'\\gt', '>'), (r'\\lt', '<'), (r'\\prime', '′'),
        (r'\\angle', '∠'), (r'\\parallel', '∥'), (r'\\perp', '⊥'),
        (r'\\triangle', '△'), (r'\\ast', '∗'), (r'\\circ', '°'),
        (r'\\pm', '±'), (r'\\mp', '∓'), (r'\\mid', '|'),
        (r'\\%', '%'), (r'\\_', '_'), (r'\\&', '&'),
        (r'\\:', ' '), (r'\\,', ' '), (r'\\;', ' '), (r'\\"', ''),
    ]
    for pat, repl in rules:
        text = re.sub(pat, repl, text)
    
    # \text{...}, \textbf{...}, \textit{...}
    text = re.sub(r'\\text\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textbf\{([^}]*)\}', r'<b>\1</b>', text)
    text = re.sub(r'\\textit\{([^}]*)\}', r'<i>\1</i>', text)
    
    # \overline, \underline, \cancel
    text = re.sub(r'\\overline\{([^}]*)\}', r'<span style="text-decoration:overline;">\1</span>', text)
    text = re.sub(r'\\underline\{([^}]*)\}', r'<span style="text-decoration:underline;">\1</span>', text)
    text = re.sub(r'\\cancel\{([^}]*)\}', r'<s>\1</s>', text)
    
    # \sqrt, \underset, \overset
    text = re.sub(r'\\sqrt(?:\[([^}]*)\])?\{([^}]*)\}', r'√\2', text)
    text = re.sub(r'\\underset\{([^}]*)\}\{([^}]*)\}', r'\2<sub>\1</sub>', text)
    text = re.sub(r'\\overset\{([^}]*)\}\{([^}]*)\}', r'\2<sup>\1</sup>', text)
    
    # ^ and _ for sup/sub
    text = re.sub(r'\^\{([^}]*)\}', r'<sup>\1</sup>', text)
    text = re.sub(r'\^([0-9a-zA-Z])', r'<sup>\1</sup>', text)
    text = re.sub(r'\_\{([^}]*)\}', r'<sub>\1</sub>', text)
    text = re.sub(r'\_([0-9a-zA-Z])', r'<sub>\1</sub>', text)
    
    return text


def clean_math_content(text):
    """Full math cleanup: convert frac, convert symbols, remove stray braces."""
    # Handle potential ⁄ from previous runs
    text = text.replace('⁄', '/')
    
    # Convert \frac with balanced parser
    text = convert_frac_balanced(text)
    
    # Convert symbols
    text = convert_symbols(text)
    
    # Remove dangling LaTeX grouping braces (but not HTML tag brackets)
    text = re.sub(r'(?<!<)\{', '', text)
    text = re.sub(r'\}(?!>)', '', text)
    
    # Clean whitespace
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r'\s*>\s*<', '><', text)
    
    return text.strip()


def fix_math_in_spans(text):
    """Fix math inside <span class=\"math-inline\"> tags."""
    def handler(m):
        return f'<span class="math-inline">{clean_math_content(m.group(1))}</span>'
    return re.sub(r'<span class="math-inline">(.*?)</span>', handler, text, flags=re.DOTALL)


def fix_math_in_displays(text):
    """Fix math inside <div class=\"math-display\"> tags."""
    def handler(m):
        content = clean_math_content(m.group(1))
        return f'<div class="math-display">\n{content}\n</div>'
    return re.sub(r'<div class="math-display">\s*(.*?)\s*</div>', handler, text, flags=re.DOTALL)


def fix_display_math(text):
    """Convert $$...$$ to math-display divs."""
    def handler(m):
        content = clean_math_content(m.group(1).strip())
        return f'<div class="math-display">\n{content}\n</div>'
    return re.sub(r'\$\$(.*?)\$\$', handler, text, flags=re.DOTALL)


def fix_raw_latex(text):
    """Convert remaining raw \\(...\\) to styled spans."""
    def handler(m):
        content = clean_math_content(m.group(1))
        return f'<span class="math-inline">{content}</span>'
    text = re.sub(r'\\\((.*?)\\\)', handler, text, flags=re.DOTALL)
    # Remove any remaining stray \( or \)
    text = text.replace('\\(', '').replace('\\)', '')
    return text


def fix_file(filepath):
    """Apply all math fixes to a file."""
    text = filepath.read_text(encoding='utf-8')
    original = text
    
    # Step 1: Convert $$...$$ to display math divs
    text = fix_display_math(text)
    
    # Step 2: Convert \(...\) to inline math spans
    text = fix_raw_latex(text)
    
    # Step 3: Convert symbols in remaining plain text (outside math tags)
    text = convert_symbols(text)
    
    # Step 4: Clean any remaining stray \frac
    if '\\frac' in text:
        text = clean_math_content(text)
    
    # Clean up spacing
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    
    if text != original:
        filepath.write_text(text, encoding='utf-8')
        return True
    return False


def main():
    all_files = sorted(BASE_DIR.rglob('en/*.md'))
    total = 0
    modified = 0
    
    for f in all_files:
        total += 1
        if fix_file(f):
            modified += 1
    
    print(f"Checked {total} files, fixed {modified}")


if __name__ == '__main__':
    main()
