
file_path = r'c:\xampp\htdocs\agro management\admin_tem_xhtml\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines to comment out: 2352 to 2435 (1-based)
# 0-based: 2351 to 2435 (excluding 2435 i.e. up to 2434)
# Wait, 1-based inclusive.
# 2352 is start. 2351 index.
# 2435 is end. 2434 index.

start_line = 2352
end_line = 2435

start_idx = start_line - 1
end_idx = end_line - 1

# Verify content to be sure
if '<div class="swiper-slide">' not in lines[start_idx]:
    print(f"Error: Line {start_line} does not contain swiper-slide. Content: {lines[start_idx]}")
    exit(1)

# We want to comment out this block.
# Insert <!-- before start_idx
# Insert --> after end_idx

lines.insert(end_idx + 1, "-->\n")
lines.insert(start_idx, "<!--\n")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Successfully commented out animation slides.")
