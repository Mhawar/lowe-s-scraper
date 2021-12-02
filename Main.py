from playwright.sync_api import sync_playwright
import time
import pandas as pd
df = pd.read_csv('Promocode.csv')

List = df['Promo code'].to_list()


i = 0
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
 print(1)
 
 page.mouse.move(100, 10)

 page.click('#frmQuickSearch > section > button')
 page.mouse.move(100, 10)
 print(2)
 
 page.click('#add-to-cart-button-5002068535')
 page.mouse.move(40, 103)
 print(3)

 page.click('#plp-atc > div > div > div.Slider__SliderStyled-RC__sc-1dw14i5-1.fa-Dhmj.slider > div.sc-eCssSg.esrtzC > div.sc-fubCfw.irPtrP > div > div.sc-fHuLdG.sc-tYoTV.ktbFdU.brBOZr > a')
 page.mouse.move(56, 200)
 print(4)

 page.click('#app > div.sc-fMfAsl.kpyQUO > div.sc-pVTFL.iPjCUm.sc-dlVxhl.sc-ezDxBL.dvqZOE.HXcio > div > div.sc-kDTinF.dwAnLX > div > div > div > div.sc-pVTFL.iPjCUm > div.sc-kSWJqS.bcCgiM > div > a')
 print(5)
 page.mouse.move(90, 133)

 page.click('input.styles__InputStyled-RC__sc-e4cx9l-5')
 print('clicked')
 Promo = List[i]
 page.fill('input.styles__InputStyled-RC__sc-e4cx9l-5', str(Promo))

 page.click('button.sc-iCfMLu:nth-child(2)')

 print("Enter succesfully =" ,i)
 i = i + 1
