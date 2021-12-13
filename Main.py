from playwright.sync_api import sync_playwright
import time
import pandas as pd
import os
import pickle
import schedule

df = pd.read_csv('Promocode.csv')
List = df['Promo code'].to_list()
def loop():
    f = open('VALID CODES.txt','a')
    f2 = open('INVALID CODES.txt','a')
    ilist=pickle.load(open("i.dat","rb"))
    i=ilist
    with sync_playwright() as p:
        print('open browser')
        browser = p.firefox.launch()
        context = browser.new_context()
        page = context.new_page()
        context.close()
        browser.close()
        print('close the browser')
        time.sleep(1)
    for a in range(10):
            with sync_playwright() as p:
                print('Open the browser for checking')
                browser = p.firefox.launch()

                # create a new incognito browser context
                context = browser.new_context()

                # create a new page inside context.
                page = context.new_page()


                print('Go to lowes.com')
                page.goto('https://www.lowes.com/')

                # Mouse move 
                page.mouse.move(0, 100)
                print('fill in the search bar')
                page.fill('input#search-query' , 'smart tv')
                

                page.mouse.move(100, 10)
                print('Click the button')
                page.click('#frmQuickSearch > section > button')
                page.mouse.move(100, 10)
                
                time.sleep(3)
                print('Click the cart button')
                page.click('#add-to-cart-button-5002068535')
                page.mouse.move(40, 103)

                
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
                        print("")
                    else:
                        print('')
                    print('Clicked on Add Promotional Code')
                    page.click("text=Add Promotional Code")
                    
                    page.mouse.move(90, 133)
                
                    print('')
                    page.click(".sc-kDTinF.dwAnLX")
                    
                    Promo = str(List[i])
                    print('Wait for input to be filled')


                    #Adding the promocode
                    page.fill('[aria-label=\"input\"]', Promo)
                    print('Filled')

                    page.click("text=Apply")
                    print('Clicking Apply')

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

for promo in List:
 loop()

