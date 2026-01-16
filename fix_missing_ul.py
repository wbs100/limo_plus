
import os

directory = r"c:\xampp\htdocs\agro management\admin_tem_xhtml"

# This is the end of the content we injected.
# We look for this specific signature to identify where we need to close the UL.
target_signature = """
										</div>
									</div>
								</li>"""

# We want to replace it with:
replacement = """
										</div>
									</div>
								</li>
							</ul>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if we have the signature
        if target_signature in content:
            # Check if it's already closed
            # We look a bit ahead.
            idx = content.find(target_signature)
            end_of_sig = idx + len(target_signature)
            
            # Look at the next non-whitespace characters
            next_chunk = content[end_of_sig:end_of_sig+50]
            
            if "</ul>" in next_chunk:
                print(f"Skipping {filename}: Already has </ul>")
            else:
                # Apply fix
                # We simply replace the signature with signature + </ul>
                # But we need to use 'replace' carefully if signature appears multiple times (unlikely here)
                new_content = content.replace(target_signature, replacement)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed missing </ul> in {filename}")
        else:
            print(f"Skipping {filename}: Signature not found (maybe different formatting?)")

