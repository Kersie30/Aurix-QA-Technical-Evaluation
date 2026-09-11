from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open login page
    page.goto(
        "https://aurixapp.de/auth/login.php",
        wait_until="domcontentloaded"
    )

    # Leave email and password EMPTY
    page.fill('input[name="email"]', "")
    page.fill('input[name="password"]', "")

    # Click Sign In
    page.click('button[type="submit"]')

    # Wait briefly
    page.wait_for_timeout(3000)

    print("Current URL:", page.url)
    print("Page text:", page.locator("body").inner_text())

    # Keep browser open briefly
    page.wait_for_timeout(10000)

    browser.close()