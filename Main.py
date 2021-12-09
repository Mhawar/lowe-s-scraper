from playwright.sync_api import sync_playwright
import time
import pandas as pd
import os
import pickle


df = pd.read_csv('Promocode.csv')
List = df['Promo code'].to_list()



f = open('VALID CODES.txt','a')
f2 = open('INVALID CODES.txt','a')
ilist=pickle.load(open("i.dat","rb"))


i=ilist

for x in List:
     time.sleep(30)
     with sync_playwright() as p:
         print('open browser')
         browser = p.firefox.launch()
         context = browser.new_context()
         page = context.new_page()
         context.close()
         browser.close()
         print('close the browser')
     time.sleep(1)
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
             print('taking the screenshot')
             page.screenshot(path="screenshot.png")
             Cart= bool(page.is_visible('text=View Cart'))
             if Cart is False:
                 print('View Cart is invisible, See the screenshot for referrence')

                 time.sleep(1)
                 context.close()
                 browser.close()
                 time.sleep(100)
                 break
             else:  
                 page.click('text=View Cart')
                 page.mouse.move(56, 200)
                 print(4)
                 if os.path.isfile("C:\Desktop\Work\Projects\Lowe's scraper\screenshot.png"):
                     os.remove("C:\Desktop\Work\Projects\Lowe's scraper\screenshot.png")
                     print("Done")
                 else:
                     print('')
                
                 page.click("text=Add Promotional Code")
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
                     b = str(i)
                     pickle.dump(i, open("i.dat" , "wb"))
                     print("Promocodes checked =" ,i)
                     print(Promo+' = Invalid')
                     print('i to put =',b)
         
                 else:
                     f.write(Promo)
                     f.write('\n')
                     context.close()
                     browser.close()
                     b = str(i)
                     pickle.dump(i, open("i.dat" , "wb"))
                     f.close()
                     print("Promocodes checked =" ,i)
                     print(Promo+' = Valid')
                     print('i to put =',b)

        

