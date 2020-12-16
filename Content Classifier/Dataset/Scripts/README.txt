ptpages_r contains pages from Phishtank URLS
azpages_r contains pages from AZSecure downloads (Phishmonger in https://www.azsecure-data.org/phishing-websites.html)

AZSecure files were in a file structure that was too entangled. Unzip,create a folder 'op' and then use './combine.sh' to combine all of them into op based on the target site. Change the range in combine.sh before running it.

Create pages_r and use 'python create_ds.py' inside the 'op' folder to save the relevant HTML files from each directory into pages_r folder

Use html_scraper_pt.py to gather HTML content from Phishtank URLS