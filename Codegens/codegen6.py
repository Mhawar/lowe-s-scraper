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

    # Click [placeholder="What are you looking for today?"]
    page.click("[placeholder=\"What are you looking for today?\"]")

    # Fill [placeholder="What are you looking for today?"]
    page.fill("[placeholder=\"What are you looking for today?\"]", "smart tv")

    # Press Enter
    page.press("[placeholder=\"What are you looking for today?\"]", "Enter")
    # assert page.url == "https://www.lowes.com/search?searchTerm=smart+tv"

    # Click button:has-text("Add to Cart")
    page.click("button:has-text(\"Add to Cart\")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
