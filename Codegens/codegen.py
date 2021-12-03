from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.lowes.com/
    page.goto("https://www.lowes.com/")

    # Fill [placeholder="What are you looking for today?"]
    page.fill("[placeholder=\"What are you looking for today?\"]", "s")

    # Press F12
    page.press("body:has-text(\"Find a Store Near MeLink to Lowe's Home Improvement Home PageLowe's Credit Cards\")", "F12")

    # Click [placeholder="What are you looking for today?"]
    page.click("[placeholder=\"What are you looking for today?\"]")

    # Press F12
    page.press("[placeholder=\"What are you looking for today?\"]", "F12")

    # Press F12
    page.press("[placeholder=\"What are you looking for today?\"]", "F12")

    # Click [placeholder="What are you looking for today?"]
    page.click("[placeholder=\"What are you looking for today?\"]", button="right")

    # Click [placeholder="What are you looking for today?"]
    page.click("[placeholder=\"What are you looking for today?\"]")

    # Fill [placeholder="What are you looking for today?"]
    page.fill("[namer=\"promoCode?\"]")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
