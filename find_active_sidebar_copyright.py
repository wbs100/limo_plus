
import os
import re

directory = r"c:\xampp\htdocs\agro management\admin_tem_xhtml"
sidebar_marker = "Sidebar end"

bad_files = []

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find sidebar section
        sidebar_end_idx = content.find(sidebar_marker)
        if sidebar_end_idx == -1:
            continue
            
        sidebar_content = content[:sidebar_end_idx]
        
        # Check for copyright div in sidebar
        # We need to see if <div class="copyright"> exists and is NOT wrapped in <!-- -->
        # Simple heuristic: find "class=\"copyright\"" and see if <!-- appears before it without --> in between
        
        matches = [m.start() for m in re.finditer(r'class=["\']copyright["\']', sidebar_content)]
        
        for m_idx in matches:
            # Check context around match
            # Look backwards for <!--
            # Look forwards for -->
            # This is tricky with multiple comments.
            # Simpler: Extract the lines containing class="copyright"
            
            lines = sidebar_content.split('\n')
            for i, line in enumerate(lines):
                 if 'class="copyright"' in line or "class='copyright'" in line:
                     # Check if this specific line is commented out?
                     # Often the comment block spans multiple lines:
                     # <!--
                     # <div class="copyright">...
                     # -->
                     
                     # We'll check if the block appears to be inside a comment structure
                     # Let's count <!-- and --> occurrences up to this point in the file?
                     # No, that's unreliable.
                     
                     # Let's check if the specific string "class="copyright"" is strictly between <!-- and -->
                     # We can search for the last <!-- before the match and the first --> after match
                     # If last <!-- is closer than last --> (or no -->), it might be commented?
                     # Actually, finding if it's active is easier by just checking if it's NOT commented.
                     
                     pass
        
        # Let's interpret the whole sidebar_content and remove comments first
        # Then check if copyright exists
        
        clean_sidebar = re.sub(r'<!--.*?-->', '', sidebar_content, flags=re.DOTALL)
        
        if 'class="copyright"' in clean_sidebar or "class='copyright'" in clean_sidebar:
            bad_files.append(filename)

print("Files with active Sidebar Copyright:")
for f in bad_files:
    print(f)
