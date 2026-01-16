
import os

directory = r"c:\xampp\htdocs\agro management\admin_tem_xhtml"

style_fix = """
	<style>
		/* Fix for black line on calendar button click and other links */
		.nav-link:focus, .nav-link.active, .bell-link:focus, .header-profile2 .nav-link:focus {
			outline: none !important;
			border: none !important;
			box-shadow: none !important;
		}
	</style>
"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if style already exists to avoid duplication
        if "/* Fix for black line on calendar button click" in content:
            continue
            
        # Insert before </head>
        if "</head>" in content:
            new_content = content.replace("</head>", style_fix + "\n</head>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected CSS fix into {filename}")
        else:
            print(f"Skipping {filename}: No </head> tag found")

print("Focus fix injection complete.")
