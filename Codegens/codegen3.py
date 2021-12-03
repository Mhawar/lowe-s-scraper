from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Click .sc-kDTinF.dwAnLX
    page.click(".sc-kDTinF.dwAnLX")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "12345678900")

    # Click text=Apply
    page.click("text=Apply")

    # Click text=Promotional code 12345678900 is invalid. Please check the data entered and try a
    page.click("text=Promotional code 12345678900 is invalid. Please check the data entered and try a")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
