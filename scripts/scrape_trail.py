import asyncio
import csv
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Target Trail or Module URL (Replace with your target link)
DEFAULT_TRAIL_URL = "https://trailhead.salesforce.com/content/learn/trails/force_com_dev_beginner"

async def scrape_trailhead_units(url=DEFAULT_TRAIL_URL, output_prefix="trailhead_units"):
    print(f"Navigating to {url}...")
    
    async with async_playwright() as p:
        # Launch headless Chromium browser
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to Trailhead page and wait for network activity to settle
        await page.goto(url, wait_until="networkidle")
        
        # Give dynamic LWC components extra time to render
        await page.wait_for_timeout(3000)
        
        # Extract rendered HTML content
        content = await page.content()
        await browser.close()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract Trail Title
    trail_title_el = soup.find('h1') or soup.find('title')
    trail_title = trail_title_el.text.strip() if trail_title_el else "Trailhead Content"
    
    print(f"\n==========================================")
    print(f" TRAIL: {trail_title}")
    print(f"==========================================\n")
    
    # Extract Links for Badges/Modules/Units
    unit_links = soup.find_all('a', href=True)
    
    extracted_units = []
    seen_urls = set()

    for link in unit_links:
        href = link['href']
        text = link.get_text(strip=True)
        
        # Filter for Unit / Badge / Module links
        if ('/units/' in href or '/modules/' in href or '/projects/' in href) and text and href not in seen_urls:
            full_url = href if href.startswith('http') else f"https://trailhead.salesforce.com{href}"
            extracted_units.append((text, full_url))
            seen_urls.add(href)
            
    # Save to Text File
    txt_filename = f"{output_prefix}.txt"
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(f"Trail: {trail_title}\nURL: {url}\n\nUnits Extracted:\n")
        f.write("-" * 60 + "\n")
        
        for idx, (unit_name, unit_url) in enumerate(extracted_units, 1):
            line = f"{idx:02d}. {unit_name}\n    Link: {unit_url}\n"
            print(line)
            f.write(line + "\n")

    # Save to CSV File
    csv_filename = f"{output_prefix}.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Unit Name", "URL"])
        for idx, (unit_name, unit_url) in enumerate(extracted_units, 1):
            writer.writerow([idx, unit_name, unit_url])

    print(f"\n[Success] Extracted {len(extracted_units)} items.")
    print(f" Saved to text file: '{txt_filename}'")
    print(f" Saved to CSV file:  '{csv_filename}'")

if __name__ == "__main__":
    import sys
    target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TRAIL_URL
    asyncio.run(scrape_trailhead_units(target_url))
