import pandas as pd
from playwright.sync_api import sync_playwright

# Function to extract expiry date using Playwright
def extract_expiry_date(service_tag):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"https://www.dell.com/support/home/en-uk/product-support/servicetag/{service_tag}/overview")
        expiry_date = page.inner_text('.warrantyExpiringLabel')
        browser.close()
        return expiry_date.strip()

# Read Excel data and update expiry dates
def main():
    excel_file = 'D:\My Documents\Code\service_tags.xlsx'
    df = pd.read_excel(excel_file)
    df['Expiry Date'] = df['Service Tag'].apply(extract_expiry_date)
    df.to_excel(excel_file, index=False)
    print("Expiry dates updated in", excel_file)

if __name__ == "__main__":
    main()