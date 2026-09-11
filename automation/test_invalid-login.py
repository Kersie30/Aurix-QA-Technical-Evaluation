import os
from playwright.sync_api import sync_playwright

EMAIL = os.getenv("AURIX_EMAIL")
WRONG_PASSWORD = "WrongPassword123!"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open login page
    page.goto(
        "https://aurixapp.de/auth/login.php",
        wait_until="domcontentloaded"
    )

    # Enter valid email and WRONG password
    page.fill('input[name="email"]', EMAIL)
    page.fill('input[name="password"]', WRONG_PASSWORD)

    # Click Sign In
    page.click('button[type="submit"]')

    # Give AURIX time to respond
    page.wait_for_timeout(3000)

    print("Current URL:", page.url)
    print("Page text:", page.locator("body").inner_text())

    # Keep browser open briefly
    page.wait_for_timeout(10000)

    browser.close()