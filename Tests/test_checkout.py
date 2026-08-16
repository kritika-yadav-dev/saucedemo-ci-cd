from playwright.sync_api import sync_playwright


def test():
	# Use Playwright's synchronous API to drive Chromium
	with sync_playwright() as p:
		# Launch Chromium with visible window and a 1s slow-motion delay
		browser = p.chromium.launch(headless=False, slow_mo=1000)

		# Open a new page/tab
		page = browser.new_page()

		# 2. Navigate to SauceDemo
		page.goto("https://www.saucedemo.com/")

		# 3. Wait for 2000 ms after opening the website
		page.wait_for_timeout(2000)

		# 4. Log in using provided credentials
		# Enter username, then wait 1000 ms
		page.fill("#user-name", "standard_user")
		page.wait_for_timeout(1000)

		# Enter password, then wait 1000 ms
		page.fill("#password", "secret_sauce")
		page.wait_for_timeout(1000)

		# 7. Click the Login button
		page.click("#login-button")

		# 8. Wait for 2000 ms after login
		page.wait_for_timeout(2000)

		# 9. Select the first product (click its name to open details)
		page.locator(".inventory_item .inventory_item_name").first.click()

		# 10. Wait for 2000 ms
		page.wait_for_timeout(2000)

		# 11. Click "Add to cart"
		page.get_by_text("Add to cart").click()

		# 12. Wait for 2000 ms
		page.wait_for_timeout(2000)

		# 13. Open the shopping cart
		page.locator(".shopping_cart_link").click()

		# 14. Wait for 2000 ms
		page.wait_for_timeout(2000)

		# 15. Click the "Checkout" button
		page.click("#checkout")

		# 16. Wait for 2000 ms
		page.wait_for_timeout(2000)

		# 17. Enter checkout information
		page.fill("#first-name", "Kritika")
		# 18. Wait 1000 ms after entering first name
		page.wait_for_timeout(1000)

		page.fill("#last-name", "QA")
		# 18. Wait 1000 ms after entering last name
		page.wait_for_timeout(1000)

		page.fill("#postal-code", "110001")
		# 18. Wait 1000 ms after entering postal code
		page.wait_for_timeout(1000)

		# 19. Click the "Continue" button
		page.click("#continue")

		# 20. Wait for 2000 ms
		page.wait_for_timeout(2000)

		# 21. Click the "Finish" button
		page.click("#finish")

		# 22. Wait for 5000 ms to observe final UI state
		page.wait_for_timeout(5000)

		# 23. Close the browser
		browser.close()


# Call the test function when the script is executed
test()

