import os
from playwright.sync_api import sync_playwright

USERNAME = os.environ["FREEGAME_USERNAME"]
PASSWORD = os.environ["FREEGAME_PASSWORD"]

print("Bot started")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Opening login page...")
    page.goto("https://panel.freegamehost.xyz")

    print("Filling username...")
    page.fill('input[name="username"]', USERNAME)

    print("Filling password...")
    page.fill('input[name="password"]', PASSWORD)

    print("Logging in...")
    page.click('button[type="submit"]')

    page.wait_for_timeout(5000)

    print("Current URL:", page.url)
    print("Page title:", page.title())

    print("Current URL:", page.url)
    print("Page title:", page.title())

    page.screenshot(path="login-result.png")

    browser.close()

print("Finished")
