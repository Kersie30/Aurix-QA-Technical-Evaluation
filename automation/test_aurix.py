import os
from playwright.sync_api import sync_playwright

EMAIL = os.getenv("AURIX_EMAIL")
PASSWORD = os.getenv("AURIX_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open login page
    page.goto(
        "https://aurixapp.de/auth/login.php",
        wait_until="domcontentloaded"
    )

    # Enter valid credentials
    page.fill('input[name="email"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)

    # Submit login
    page.click('button[type="submit"]')

    # Wait for redirected page
    page.wait_for_load_state("domcontentloaded")

    # Verify successful authentication
    page.get_by_text("Sign out", exact=True).wait_for(
        state="visible",
        timeout=10000
    )

    print("PASS: Successful login - Sign out is visible")
    print("Current URL:", page.url)

    page.wait_for_timeout(5000)

    browser.close()