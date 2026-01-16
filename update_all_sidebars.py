
import os

target_dir = r"c:\xampp\htdocs\agro management\admin_tem_xhtml"
sidebar_link_html = """
					<li><a href="crop-management.html" class="" aria-expanded="false">
							<div class="menu-icon">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path
										d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
										stroke="#90959F" stroke-width="2" stroke-linecap="round"
										stroke-linejoin="round" />
									<path d="M12 10V16" stroke="#90959F" stroke-width="2" stroke-linecap="round"
										stroke-linejoin="round" />
									<path d="M12 12L15 9" stroke="#90959F" stroke-width="2" stroke-linecap="round"
										stroke-linejoin="round" />
									<path d="M12 14L9 11" stroke="#90959F" stroke-width="2" stroke-linecap="round"
										stroke-linejoin="round" />
								</svg>
							</div>
							<span class="nav-text">Crop Management</span>
						</a>
					</li>"""

plantation_link_pattern = 'Plantation Management</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</li>'

def update_sidebar():
    count = 0
    for filename in os.listdir(target_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(target_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if "crop-management.html" in content:
                    print(f"Skipping {filename}: already has crop-management.html")
                    continue
                
                # Check for Plantation Management link to insert after
                if plantation_link_pattern in content:
                    new_content = content.replace(plantation_link_pattern, plantation_link_pattern + sidebar_link_html)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
                    count += 1
                else:
                     # Try a looser match if specific indentation fails
                    if "Plantation Management" in content and "crop-management.html" not in content:
                         # Attempt to find the closing </li> of plantation management
                         # This is a bit risky with simple replace, so logging it
                         print(f"Could not find exact pattern in {filename}, manual check needed.")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    update_sidebar()
