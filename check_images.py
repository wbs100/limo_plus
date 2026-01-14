
import os

# To replace the "icon next to the title" in the browser tab, we need to update the favicon.
# The user wants "limo pius icon" (likely the leaf icon we are using).
# Since the leaf icon is a FontAwesome SVG/font, we can't directly link it as a favicon image file (png/ico).
# We have two options:
# 1. Provide a PNG version of the leaf icon and link to it. 
# 2. Use a Data URI SVG (modern browsers support this).
#
# Given the user says "limo pius icon" and shared a screenshot showing the browser tab 'Y' logo,
# and previously we discussed `images/favicon.png`...
# I should generate a new `images/favicon.png` that matches the green leaf icon, OR update the link to point to a new file.
# Since I can't generate a binary image file easily to overwrite `favicon.png` without an input image,
# I will try to use an SVG data URI or see if there is a leaf image available.
#
# Actually, the user might mean the "Dashboard" text or something in the UI? 
# "replace the icon nest to the title with the limo pius icon"
# Looking at the screenshot, the browser tab has a purple logo. That is the favicon.
#
# I will try to find if there is a leaf image in the project, or I will use an SVG data URI for the favicon 
# which is supported in most modern browsers.

# Let's check images folder first.
import glob
print(glob.glob(r"c:\xampp\htdocs\agro management\admin_tem_xhtml\images\*"))
