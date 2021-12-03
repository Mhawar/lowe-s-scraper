from playwright.sync_api import sync_playwright
import time
import pandas as pd
import csv

df = pd.read_csv('Promocode.csv')
List = df['Promo code'].to_list()

f = open('VALID CODES.txt','a')


i = 0

for x in List:
  with sync_playwright() as p:
     browser = p.firefox.launch()

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
     time.sleep(3)
     page.click('#add-to-cart-button-5002068535')
     page.mouse.move(40, 103)
     
     print(3)
     
     page.click("text=View Cart")
     page.mouse.move(56, 200)
     page.mouse.wheel(0,100)
     print(4)

     page.click('#app > div.sc-fMfAsl.kpyQUO > div.sc-pVTFL.iPjCUm.sc-dlVxhl.sc-ezDxBL.dvqZOE.HXcio > div > div.sc-kDTinF.dwAnLX > div > div > div > div.sc-pVTFL.iPjCUm > div.sc-kSWJqS.bcCgiM > div > a')
     print(5)
     page.mouse.move(90, 133)
    

     page.click(".sc-kDTinF.dwAnLX")
     print(6)
     Promo = str(List[i])
     print('wait for input to be filled')
     page.fill('[aria-label=\"input\"]', Promo)
     print('filled')

     page.click("text=Apply")
     print('Finished')
     
     i = i + 1
     time.sleep(3)
     
     if page.is_visible('div[role=\"alert\"]') is True:
         context.close()
         browser.close()
         print("Enter succesfully =" ,i)
     else:
         f.write(Promo)
         context.close()
         browser.close()
         print("Enter succesfully =" ,i)

        

