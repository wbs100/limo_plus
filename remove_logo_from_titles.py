import os
import re

# Define the pattern to remove
# Matches the specific img tag added earlier, accounting for potential whitespace
pattern = re.compile(r'<img src="images/logo\.jpg" alt="Limo Plus Logo" style="max-height: 30px; margin-right: 10px; vertical-align: middle;">\s*', re.IGNORECASE)

def remove_logo(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        updated_content = pattern.sub('', content)
        
        if updated_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Removed logo from {filepath}")
        else:
            print(f"No logo found in {filepath}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    print("Removing logo from titles...")
    for filename in files:
        remove_logo(filename)
