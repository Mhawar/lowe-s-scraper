from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").click("input[name=\"promoCode\"]")

    # Go to https://www.lowes.com/cart
    page.goto("https://www.lowes.com/cart")

    # Click text=Add Promotional Code
    page.click("text=Add Promotional Code")

    # Click text=Promo Code
    page.click("text=Promo Code")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "5676567818272713")

    # Click text=Apply
    page.click("text=Apply")

    # Click div[role="alert"]:has-text("Promotional code 5676567818272713 is invalid. Please check the data entered and ")
    page.click("div[role=\"alert\"]:has-text(\"Promotional code 5676567818272713 is invalid. Please check the data entered and \")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
