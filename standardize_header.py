
import os
import re

directory = r"c:\xampp\htdocs\agro management\admin_tem_xhtml"

# Standard Calendar LI from index.html (Lines 730-748 approx)
calendar_li = """
								<li class="nav-item dropdown notification_dropdown">
									<a class="nav-link bell-link" href="javascript:void(0);">
										<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
											xmlns="http://www.w3.org/2000/svg">
											<path fill-rule="evenodd" clip-rule="evenodd"
												d="M3.5 16.87V9.257H21.5V16.931C21.5 20.07 19.5241 22 16.3628 22H8.62733C5.49561 22 3.5 20.03 3.5 16.87ZM8.45938 14.41C8.00494 14.431 7.62953 14.07 7.60977 13.611C7.60977 13.151 7.96542 12.771 8.41987 12.75C8.86443 12.75 9.22997 13.101 9.23985 13.55C9.2596 14.011 8.90395 14.391 8.45938 14.41ZM12.5198 14.41C12.0653 14.431 11.6899 14.07 11.6701 13.611C11.6701 13.151 12.0258 12.771 12.4802 12.75C12.9248 12.75 13.2903 13.101 13.3002 13.55C13.32 14.011 12.9643 14.391 12.5198 14.41ZM16.5505 18.09C16.096 18.08 15.7305 17.7 15.7305 17.24C15.7206 16.78 16.0862 16.401 16.5406 16.391H16.5505C17.0148 16.391 17.3902 16.771 17.3902 17.24C17.3902 17.71 17.0148 18.09 16.5505 18.09ZM11.6701 17.24C11.6899 17.7 12.0653 18.061 12.5198 18.04C12.9643 18.021 13.32 17.641 13.3002 17.181C13.2903 16.731 12.9248 16.38 12.4802 16.38C12.0258 16.401 11.6701 16.78 11.6701 17.24ZM7.59989 17.24C7.61965 17.7 7.99506 18.061 8.44951 18.04C8.89407 18.021 9.24973 17.641 9.22997 17.181C9.22009 16.731 8.85456 16.38 8.40999 16.38C7.95554 16.401 7.59989 16.78 7.59989 17.24ZM15.7404 13.601C15.7404 13.141 16.096 12.771 16.5505 12.761C16.9951 12.761 17.3507 13.12 17.3705 13.561C17.3804 14.021 17.0247 14.401 16.5801 14.41C16.1257 14.42 15.7503 14.07 15.7404 13.611V13.601Z"
												fill="#222B40"></path>
											<path opacity="0.4"
												d="M3.50336 9.2569C3.5162 8.6699 3.5656 7.5049 3.65846 7.1299C4.13267 5.0209 5.74298 3.6809 8.04485 3.4899H16.9559C19.238 3.6909 20.8681 5.0399 21.3423 7.1299C21.4342 7.4949 21.4836 8.6689 21.4964 9.2569H3.50336Z"
												fill="#222B40"></path>
											<path
												d="M8.80489 6.59C9.23958 6.59 9.56559 6.261 9.56559 5.82V2.771C9.56559 2.33 9.23958 2 8.80489 2C8.3702 2 8.04419 2.33 8.04419 2.771V5.82C8.04419 6.261 8.3702 6.59 8.80489 6.59Z"
												fill="#222B40"></path>
											<path
												d="M16.195 6.59C16.6198 6.59 16.9557 6.261 16.9557 5.82V2.771C16.9557 2.33 16.6198 2 16.195 2C15.7603 2 15.4343 2.33 15.4343 2.771V5.82C15.4343 6.261 15.7603 6.59 16.195 6.59Z"
												fill="#222B40"></path>
										</svg>
									</a>
								</li>"""

# Standard Profile LI from index.html (Lines 769-839 approx)
profile_li = """
								<li class="nav-item ps-3">
									<div class="dropdown header-profile2">
										<a class="nav-link" href="javascript:void(0);" role="button"
											data-bs-toggle="dropdown" aria-expanded="false">
											<div class="header-info2 d-flex align-items-center">
												<div class="header-media">
													<img src="images/user.jpg" alt="">
												</div>
											</div>
										</a>
										<div class="dropdown-menu dropdown-menu-end">
											<div class="card border-0 mb-0">
												<div class="card-header py-2">
													<div class="products">
														<img src="images/user.jpg" class="avatar avatar-md" alt="">
														<div>
															<h6>Bimsara Sandruwan</h6>
															
														</div>
													</div>
												</div>
												<div class="card-body px-0 py-2">
													<a href="#" class="dropdown-item ai-icon ">
														<svg width="20" height="20" viewBox="0 0 24 24" fill="none"
															xmlns="http://www.w3.org/2000/svg">
															<path fill-rule="evenodd" clip-rule="evenodd"
																d="M11.9848 15.3462C8.11714 15.3462 4.81429 15.931 4.81429 18.2729C4.81429 20.6148 8.09619 21.2205 11.9848 21.2205C15.8524 21.2205 19.1543 20.6348 19.1543 18.2938C19.1543 15.9529 15.8733 15.3462 11.9848 15.3462Z"
																stroke="var(--primary)" stroke-width="1.5"
																stroke-linecap="round" stroke-linejoin="round" />
															<path fill-rule="evenodd" clip-rule="evenodd"
																d="M11.9848 12.0059C14.5229 12.0059 16.58 9.94779 16.58 7.40969C16.58 4.8716 14.5229 2.81445 11.9848 2.81445C9.44667 2.81445 7.38857 4.8716 7.38857 7.40969C7.38 9.93922 9.42381 11.9973 11.9524 12.0059H11.9848Z"
																stroke="var(--primary)" stroke-width="1.42857"
																stroke-linecap="round" stroke-linejoin="round" />
														</svg>
														
														<span class="ms-2">Profile </span>
													</a>

													
												</div>
												<div class="card-footer px-0 py-2">
													<a href="javascript:void(0);" class="dropdown-item ai-icon ">
														<svg width="20" height="20" viewBox="0 0 24 24" fill="none"
															xmlns="http://www.w3.org/2000/svg">
															<path fill-rule="evenodd" clip-rule="evenodd"
																d="M20.8066 7.62355L20.1842 6.54346C19.6576 5.62954 18.4907 5.31426 17.5755 5.83866V5.83866C17.1399 6.09528 16.6201 6.16809 16.1307 6.04103C15.6413 5.91396 15.2226 5.59746 14.9668 5.16131C14.8023 4.88409 14.7139 4.56833 14.7105 4.24598V4.24598C14.7254 3.72916 14.5304 3.22834 14.17 2.85761C13.8096 2.48688 13.3145 2.2778 12.7975 2.27802H11.5435C11.0369 2.27801 10.5513 2.47985 10.194 2.83888C9.83666 3.19791 9.63714 3.68453 9.63958 4.19106V4.19106C9.62457 5.23686 8.77245 6.07675 7.72654 6.07664C7.40418 6.07329 7.08843 5.98488 6.8112 5.82035V5.82035C5.89603 5.29595 4.72908 5.61123 4.20251 6.52516L3.53432 7.62355C3.00838 8.53633 3.31937 9.70255 4.22997 10.2322V10.2322C4.82187 10.574 5.1865 11.2055 5.1865 11.889C5.1865 12.5725 4.82187 13.204 4.22997 13.5457V13.5457C3.32053 14.0719 3.0092 15.2353 3.53432 16.1453V16.1453L4.16589 17.2345C4.41262 17.6797 4.82657 18.0082 5.31616 18.1474C5.80575 18.2865 6.33061 18.2248 6.77459 17.976V17.976C7.21105 17.7213 7.73116 17.6515 8.21931 17.7821C8.70746 17.9128 9.12321 18.233 9.37413 18.6716C9.53867 18.9488 9.62708 19.2646 9.63043 19.5869V19.5869C9.63043 20.6435 10.4869 21.5 11.5435 21.5H12.7975C13.8505 21.5 14.7055 20.6491 14.7105 19.5961V19.5961C14.7081 19.088 14.9088 18.6 15.2681 18.2407C15.6274 17.8814 16.1154 17.6806 16.6236 17.6831C16.9451 17.6917 17.2596 17.7797 17.5389 17.9393V17.9393C18.4517 18.4653 19.6179 18.1543 20.1476 17.2437V17.2437L20.8066 16.1453C21.0617 15.7074 21.1317 15.1859 21.0012 14.6963C20.8706 14.2067 20.5502 13.7893 20.111 13.5366V13.5366C19.6717 13.2839 19.3514 12.8665 19.2208 12.3769C19.0902 11.8872 19.1602 11.3658 19.4153 10.9279C19.5812 10.6383 19.8213 10.3981 20.111 10.2322V10.2322C21.0161 9.70283 21.3264 8.54343 20.8066 7.63271V7.63271V7.62355Z"
																fill="#222B40" />
															<circle cx="12.175" cy="11.889" r="2.63616"
																stroke="var(--primary)" stroke-width="1.5"
																stroke-linecap="round" stroke-linejoin="round" />
														</svg>
														
														<span class="ms-2">Settings </span>
													</a>
													<a href="page-login.html" class="dropdown-item ai-icon">
														<svg class="logout-svg" xmlns="http://www.w3.org/2000/svg"
															width="18" height="18" viewBox="0 0 24 24" fill="none"
															stroke="currentColor" stroke-width="2"
															stroke-linecap="round" stroke-linejoin="round">
															<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
															<polyline points="16 17 21 12 16 7"></polyline>
															<line x1="21" y1="12" x2="9" y2="12"></line>
														</svg>
														<span class="ms-2 text-danger">Logout </span>
													</a>
												</div>
											</div>

										</div>
									</div>
								</li>"""

# Combined Navbar Content
new_navbar_content = calendar_li + "\n" + profile_li

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find <ul class="navbar-nav"> ... </ul>
        # We need to be careful not to match the sidebar regex or others.
        # We look for <ul class="navbar-nav"> that is INSIDE <div class="header-right ...">
        # Or just find the one that occurs after <div class="header-right
        
        # Strategy: Find start of header-right
        header_right_start = content.find('class="header-right')
        if header_right_start == -1:
            print(f"Skipping {filename}: No header-right found")
            continue
            
        # Find start of navbar-nav AFTER header-right
        navbar_start = content.find('<ul class="navbar-nav">', header_right_start)
        if navbar_start == -1:
            print(f"Skipping {filename}: No navbar-nav found in header-right")
            continue
            
        # Find the matching closing </ul>
        # Simple search for </ul> might fail if nested. But navbar items usually don't have nested <ul>?
        # Actually Notification dropdowns MIGHT have nested <ul> if complex? 
        # Looking at index.html code: Dropdowns use <div> for menu, not nested <ul> (usually).
        # Let's check: <div class="dropdown-menu"> ... <ul class="contacts"> ... </ul> </div>
        # Yes, Chat/Notification dropdowns DO have nested <ul> inside!
        # So we can't just look for next </ul>.
        
        # We need to count balanced tags? Or use regex with non-greedy?
        # Or observe indentation?
        # The Navbar-nav usually ends before the `Header end` comment.
        
        header_end_comment = content.find('Header end', navbar_start)
        if header_end_comment == -1:
             print(f"Skipping {filename}: No Header end comment found")
             continue
             
        # Locate the LAST </ul> before `Header end`.
        # This is a bit risky if there are multiple uls.
        # But `navbar-nav` should be the main wrapper.
        
        # Valid strategy:
        # Find </ul> that closes `navbar-nav`.
        # Locate the positions of all </ul> between navbar_start and header_end_comment.
        # Locate the positions of all <ul> between navbar_start and header_end_comment.
        # Match them.
        
        # Let's extract the chunk.
        chunk = content[navbar_start:header_end_comment]
        
        cnt = 0
        end_idx = -1
        
        # Iterate through tags in chunk
        # Using a simplistic parser for <ul> and </ul>
        
        # Actually, let's just use the indentation pattern if possible, or robust counting.
        
        # Robust counting:
        ul_starts = [m.start() for m in re.finditer(r'<ul', chunk)]
        ul_ends = [m.start() for m in re.finditer(r'</ul>', chunk)]
        
        # We know chunk starts with <ul (index 0).
        # We need to find the matching </ul>.
        # A stack check:
        
        stack = 0
        # Combine starts and ends and sort
        
        tags = []
        for pos in ul_starts:
            tags.append((pos, 1)) # +1 for open
        for pos in ul_ends:
            tags.append((pos, -1)) # -1 for close
        
        tags.sort(key=lambda x: x[0])
        
        found_end = False
        current_pos = 0
        
        for pos, val in tags:
            stack += val
            if stack == 0:
                # Found the closing tag of the first UL
                # Length of closing tag is 5 ("</ul>")
                end_idx = pos + 5
                found_end = True
                break
        
        if not found_end:
            print(f"Skipping {filename}: Could not find matching </ul>")
            continue
            
        # Global position of end
        global_end = navbar_start + end_idx
        
        # Replace content
        new_content = content[:navbar_start] + '<ul class="navbar-nav">' + new_navbar_content + content[global_end:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

print("Done standardizing headers.")
