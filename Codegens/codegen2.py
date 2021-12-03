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

    # Go to https://www.lowes.com/cart
    page.goto("https://www.lowes.com/cart")

    # Click text=Presque Isle Lowe's | 135 Maysville St, Presque Isle, ME 04769 | Change Store
    page.click("text=Presque Isle Lowe's | 135 Maysville St, Presque Isle, ME 04769 | Change Store")

    # Click text=Add Promotional Code
    page.click("text=Add Promotional Code")

    # Click text=Promo Code
    page.click("text=Promo Code")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i will not facing any problem")

    # Click text=Apply
    page.click("text=Apply")

    # Click text=Promotional code hey now i will not facing any problem is invalid. Please check
    page.click("text=Promotional code hey now i will not facing any problem is invalid. Please check ")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").click("input[name=\"promoCode\"]")

    # Click .sc-kmiuhe
    page.click(".sc-kmiuhe")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i will not facing anyproblem")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i will not facing anproblem")

    # Click input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").click("input[name=\"promoCode\"]")

    # Click text=Item Subtotal (1)
    page.click("text=Item Subtotal (1)")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i will not facing aproblem")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i will not facing problem")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i will not facingproblem")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "hey now i problem")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "problem")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Click input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").click("input[name=\"promoCode\"]")

    # Click a[role="button"]:has-text("Presque Isle Lowe's")
    page.click("a[role=\"button\"]:has-text(\"Presque Isle Lowe's\")")

    # Click [aria-label="modal-close"]
    page.click("[aria-label=\"modal-close\"]")

    # Click [aria-label="input"]
    page.click("[aria-label=\"input\"]")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "p")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Fill [aria-label="input"]
    page.fill("[aria-label=\"input\"]", "")

    # Fill input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").fill("input[name=\"promoCode\"]", "")

    # Click input[name="promoCode"]
    page.frame(name="viceSecuredIframe_Strict").click("input[name=\"promoCode\"]")

    # Click a[role="button"]:has-text("Presque Isle Lowe's")
    page.click("a[role=\"button\"]:has-text(\"Presque Isle Lowe's\")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
