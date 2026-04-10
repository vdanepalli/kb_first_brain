import os
import hashlib
from urllib.parse import quote

# 1. Complex Markers
START_MARKER = "<!-- SITEMAP_START -->"
END_MARKER = "<!-- SITEMAP_END -->"

EXCLUDE_DIRS = {'assets', '.git', '.github', '.venv', '__pycache__', '80_Archive'}
EXCLUDE_FILES = {'readme.md', 'sitemap.md', 'temp.md', 'generate_sitemap.py', '.ds_store'}

FOLDER_METADATA = {
    '00_INBOX': '📥 00. Inbox',
    '10_CS_CORE': '💻 10. Computer Science Core',
    '20_SOFTWARE_ENG': '🛠️ 20. Software Engineering',
    '30_DATA_SYSTEMS': '🗄️ 30. Data Systems',
    '40_HARDWARE_ELECTRICAL': '⚡ 40. Hardware & Electrical',
    '50_MATH_AI': '🧠 50. Mathematics & AI',
    '60_CAREER_LIFE': '👔 60. Career & Life',
    '70_LIBRARY': '📚 70. Library',
    '80_ARCHIVE': '🗑️ 80. Archive'
}

def get_color(name):
    """Generate a consistent hex color for a given folder name."""
    return hashlib.md5(name.encode('utf-8')).hexdigest()[:6]

def get_h1_title(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line.lstrip('#').strip()
    except: pass
    return os.path.basename(file_path).replace('.md', '').replace('_', ' ').title()

def generate_sitemap_content(root_dir):
    sitemap_lines = []
    
    top_level_dirs = sorted([d for d in os.listdir(root_dir) 
                             if os.path.isdir(os.path.join(root_dir, d)) 
                             and d not in EXCLUDE_DIRS 
                             and not d.startswith('.')])
                             
    for tld in top_level_dirs:
        upper_folder = tld.upper()
        display_name = FOLDER_METADATA.get(upper_folder, upper_folder)
        
        tld_path = os.path.join(root_dir, tld)
        tld_url = quote(tld.replace('\\', '/'))
        
        # 1. Root Level Accordion (Fix arrow bug with <kbd>)
        sitemap_lines.append(f"<details open>")
        sitemap_lines.append(f"<summary><a href='{tld_url}'><b><kbd>{display_name}</kbd></b></a></summary>\n")
        
        tld_path = os.path.join(root_dir, tld)
        for root, dirs, files in os.walk(tld_path):
            dirs[:] = sorted([d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')])
            
            level = root.replace(tld_path, '').count(os.sep)
            
            # 2. Dynamic Shields.io Badge for Sub-folders
            if root != tld_path:
                indent = "  " * (level - 1)
                folder_name = os.path.basename(root).replace('_', ' ').title()
                safe_folder_name = quote(folder_name.replace('-', '--'))
                color = get_color(folder_name)
                badge_url = f"https://img.shields.io/badge/{safe_folder_name}-{color}?style=flat-square&logo=files&logoColor=white"
                
                # Use Markdown image notation instead of raw HTML to prevent list breaking!
                # sitemap_lines.append(f"{indent}- ![]({badge_url})")
                rel_folder_path = quote(os.path.relpath(root, root_dir).replace('\\', '/'))
                sitemap_lines.append(f"{indent}- [![{folder_name}]({badge_url})]({rel_folder_path})")
                
            sub_indent = "  " * level
            
            # 3. KBD Buttons for File Links
            md_files = sorted([f for f in files if f.lower().endswith('.md') and f.lower() not in EXCLUDE_FILES])
            for f in md_files:
                file_path = os.path.join(root, f)
                title = get_h1_title(file_path)
                rel_path = quote(os.path.relpath(file_path, root_dir).replace('\\', '/'))
                
                # Use Markdown links containing the HTML <kbd> for modern clickable UI feel
                sitemap_lines.append(f"{sub_indent}- [<kbd>📝 {title}</kbd>]({rel_path})")
                
        # Close accordion block
        sitemap_lines.append(f"\n</details>")
        sitemap_lines.append(f"<br>\n")
        
    return "\n".join(sitemap_lines)

def update_readme():
    target = "README.md"
    if not os.path.exists(target): return

    with open(target, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_sitemap_block = False
    sitemap_injected = False

    # 2. Line-by-Line State Machine
    for line in lines:
        if START_MARKER in line:
            in_sitemap_block = True
            
            if not sitemap_injected:
                new_lines.append(START_MARKER + "\n\n")
                new_lines.append(generate_sitemap_content(".") + "\n\n")
                new_lines.append(END_MARKER + "\n")
                sitemap_injected = True
            continue 
        
        if END_MARKER in line:
            in_sitemap_block = False
            continue 
        
        if not in_sitemap_block:
            new_lines.append(line)

    if not sitemap_injected:
        print("FAILED: Markers not found in README.md. File unchanged.")
        return

    with open(target, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("SUCCESS: Sitemap generated and file healed.")

if __name__ == "__main__":
    update_readme()