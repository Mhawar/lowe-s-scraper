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






from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.lowes.com/
    page.goto("https://www.lowes.com/")

    # Click [placeholder="What are you looking for today?"]
    page.click("[placeholder=\"What are you looking for today?\"]")

    # Fill [placeholder="What are you looking for today?"]
    page.fill("[placeholder=\"What are you looking for today?\"]", "smart tv")

    # Go to https://www.lowes.com/search?searchTerm=smart+tv
    page.goto("https://www.lowes.com/search?searchTerm=smart+tv")

    # Click text=View Cart
    page.click("text=View Cart")
    # assert page.url == "https://www.lowes.com/cart"

    # Click text=Add Promotional Code
    page.click("text=Add Promotional Code")

    # Click text=Promo Code
    page.click("text=Promo Code")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "23456789876567862")

    # Click text=Apply
    page.click("text=Apply")

    # Click div[role="alert"]:has-text("Promotional code 23456789876567862 is invalid. Please check the data entered and")
    page.click("div[role=\"alert\"]:has-text(\"Promotional code 23456789876567862 is invalid. Please check the data entered and\")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
