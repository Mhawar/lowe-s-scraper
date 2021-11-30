from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
 browser = p.firefox.launch(headless=False)

 # create a new incognito browser context
 context = browser.new_context()

 # create a new page inside context.
 page = context.new_page()

 page.goto('https://www.lowes.com/')

 # Mouse move 
 page.mouse.move(0, 100)

 page.fill('input#search-query' , 'smart tv')
 
 page.mouse.move(100, 10)

 page.click('#frmQuickSearch > section > button')
 
 print("Enter succesfully")

 page.click('#add-to-cart-button-5002068527')

 page.click('#plp-atc > div > div > div.Slider__SliderStyled-RC__sc-1dw14i5-1.fa-Dhmj.slider > div.sc-eCssSg.esrtzC > div.sc-fubCfw.irPtrP > div > div.sc-fHuLdG.sc-tYoTV.ktbFdU.brBOZr > a')

 page.click('#app > div.sc-fMfAsl.kpyQUO > div.sc-pVTFL.iPjCUm.sc-dlVxhl.sc-ezDxBL.dvqZOE.HXcio > div > div.sc-kDTinF.dwAnLX > div > div > div > div.sc-pVTFL.iPjCUm > div.sc-kSWJqS.bcCgiM > div > a')

 time.sleep(10)
 

 promo_code_1 = 'a'
 
 
 






