from playwright.sync_api import sync_playwright
import time
import pandas as pd
import os
import csv

df = pd.read_csv('Promocode.csv')
List = df['Promo code'].to_list()

f = open('VALID CODES.txt','a')
f2 = open('INVALID CODES.txt','a')

i=56

for x in List:
     time.sleep(1)
     with sync_playwright() as p:
         print('open browser')
         browser = p.firefox.launch()
         context = browser.new_context()
         page = context.new_page()
         context.close()
         browser.close()
         print('close the browser')
     for a in range(5):
         with sync_playwright() as p:
             print('open the browser for checking')
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
             time.sleep(4)
             page.screenshot(path="screenshot.png")
             page.click('text=View Cart , #plp-atc')
             page.mouse.move(56, 200)
             print(4)
             os.remove("C:\Users\mhawa\Desktop\Work\Projects\Lowe's scraper\screenshot.png")

             page.click('#app > div.sc-fMfAsl.kpyQUO > div.sc-pVTFL.iPjCUm.sc-dlVxhl.sc-ezDxBL.dvqZOE.HXcio > div > div.sc-kDTinF.dwAnLX > div > div > div > div.sc-pVTFL.iPjCUm > div.sc-kSWJqS.bcCgiM > div > a')
             print(5)
             page.mouse.move(90, 133)
    

             page.click(".sc-kDTinF.dwAnLX")
             print(6)
             Promo = str(List[i])
             print('Wait for input to be filled')


             #Adding the promocode
             page.fill('[aria-label=\"input\"]', Promo)
             print('Filled')

             page.click("text=Apply")
             print('Applied')
     
             #The ++
             i = i + 1
             time.sleep(3)
             visible = bool(page.is_visible("div[role=\"alert\"]:has-text(\"Please check the data entered and\")"))
             #the instructions to check the code validity
             if visible is True:
                 f2.write(Promo)
                 f2.write('\n')
                 context.close()
                 browser.close()
                 b = i
                 print("Promocodes checked =" ,i)
                 print('i to put =',b)
         
             else:
                 f.write(Promo)
                 f.write('\n')
                 context.close()
                 browser.close()
                 b = i
                 print("Promocodes checked =" ,i)
                 print('i to put =',b)

        

