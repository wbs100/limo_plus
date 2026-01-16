
import os

directory = r"c:\xampp\htdocs\agro management\admin_tem_xhtml"

# This CSS will force the full sidebar mode on large screens and ensure visibility
# It specifically targets the sidebar state attributes and forces width.
# Also fix toggle visibility if hidden.

sidebar_fix_css = """
	<style>
		/* Fix Sidebar to be Full Width by default on large screens */
		@media (min-width: 768px) {
			[data-sidebar-style="mini"] .deznav {
				width: 17.5rem !important;
			}
			[data-sidebar-style="mini"] .deznav .metismenu > li > a > .nav-text {
				display: inline-block !important;
				padding-left: 0.5rem;
			}
			[data-sidebar-style="mini"] .nav-header {
				width: 17.5rem !important;
			}
			[data-sidebar-style="mini"] .header {
				padding-left: 17.5rem !important;
			}
			[data-sidebar-style="mini"] .content-body {
				margin-left: 17.5rem !important;
			}
            
            /* Ensure hamburger is visible */
            .nav-control {
                display: block !important;
                z-index: 9999;
            }
		}
	</style>
"""

# Actually, forcing styles like this might break the toggle functionality (making it permanent).
# A better approach is to change the default attribute in the HTML if it exists.
# Or check if there is a script setting it to "mini".

# Let's check the HTML for 'data-sidebar-style="mini"'
# If found, replace with "full".

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        
        # Check for data-sidebar-style="mini" and replace with "full"
        if 'data-sidebar-style="mini"' in content:
            content = content.replace('data-sidebar-style="mini"', 'data-sidebar-style="full"')
            updated = True
            print(f"Fixed sidebar style to 'full' in {filename}")
            
        # Also check for body class "mini" or similar if pertinent
        # And ensure the hamburger button is not hidden by my previous CSS hacks
        
        # Check for nav-header width override?
        # In my view_file output, I saw specific CSS injected in line 220 of index.html:
        # 220: margin-left: 17.5rem !important;
        
        # If I hardcoded margin-left, it might conflict with the sidebar state.
        
        # Let's clean up hardcoded CSS if it's causing the issue.
        # But first, let's try setting the attribute.
        
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Sidebar attribute fix complete.")
