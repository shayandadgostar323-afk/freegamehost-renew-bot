import os
from playwright.sync_api import sync_playwright, TimeoutError

USERNAME = os.environ["FREEGAME_USERNAME"]
PASSWORD = os.environ["FREEGAME_PASSWORD"]

print("Bot started")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        viewport={"width": 1280, "height": 720}
    )

    print("Opening login page...")
    page.goto(
        "https://panel.freegamehost.xyz",
        wait_until="networkidle"
    )

    print("Filling username...")
    page.fill('input[name="username"]', USERNAME)

    print("Filling password...")
    page.fill('input[name="password"]', PASSWORD)

    print("Logging in...")
    page.click('button[type="submit"]')

    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except TimeoutError:
        print("Page did not fully reload, continuing...")

    page.wait_for_timeout(3000)

    print("--------------------")
    print("Current URL:", page.url)
    print("Page title:", page.title())
    print("--------------------")

    text = page.locator("body").inner_text()

    print("PAGE TEXT:")
    print(text[:2000])

    page.screenshot(
        path="login-result.png",
        full_page=True
    )

    browser.close()

print("Finished")
