#!/usr/bin/env python3


from playwright.sync_api import sync_playwright


def test():
    # Start Playwright and launch Chromium with flags to reduce password-manager UI
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,
            args=[
                "--disable-save-password-bubble",
                "--disable-password-manager-reauthentication",
                "--disable-features=PasswordManagerOnboarding,AutofillServerCommunication"
            ],
        )

        # Open a new page
        page = browser.new_page()

        #  Navigate to SauceDemo
        page.goto("https://www.saucedemo.com/", timeout=30000)

        #  Wait 2000 ms to observe the opened browser/page
        page.wait_for_timeout(1000)

        #  Enter username and wait 1000 ms
        page.fill("#user-name", "standard_user")
        page.wait_for_timeout(1000)

        #  Enter password and wait 1000 ms
        page.fill("#password", "secret_sauce")
        page.wait_for_timeout(1000)

        #  Click the Login button
        page.click("#login-button")

        #  Wait 2000 ms for navigation/animations
        page.wait_for_timeout(2000)

        

        #  Capture the first product name, click it to open details
        first_product_locator = page.locator(".inventory_item_name").first

        first_product_locator.click()


        #  Wait 5000 ms so the UI can be observed in CI runs or during local debugging
        page.wait_for_timeout(5000)

        #  Close the browser
        browser.close()


test()
