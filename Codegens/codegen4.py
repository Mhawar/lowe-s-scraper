from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Click text=View Cart
    page.click("text=View Cart")
    # assert page.url == "https://www.lowes.com/cart"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
