#!/usr/bin/env python3


from playwright.sync_api import sync_playwright


def test():
    # Start Playwright and launch Chromium (headless)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo = 1000)

        # Create a new browser page
        page = browser.new_page()

        # Navigate to the SauceDemo login page
        page.goto("https://www.saucedemo.com/")
        # Provide delay for 1000 milliseconds
        page.wait_for_timeout(2000)
        # Fill in the username and password fields
        page.fill("#user-name", "standard_user")
        # Provide delay for 1000 milliseconds
        page.wait_for_timeout(2000)
        page.fill("#password", "secret_sauce")

        # Click the login button
        page.click("#login-button")

        
        # Provide delay for 5000 milliseconds
        page.wait_for_timeout(5000)

        # Close the browser
        browser.close()

test()

