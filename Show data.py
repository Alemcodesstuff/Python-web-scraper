import gettext
import bs4
import time
import requests


try:

    for x in range(1,51): #number of pages

        link_for_scraping='https://books.toscrape.com/catalogue/page-{}.html'
        result = requests.get(link_for_scraping.format(x))
        

        soup = bs4.BeautifulSoup(result.text, 'lxml')

        data = soup.select('.product_pod')


        for i in data:
            title = i.select('a')[1]['title']
            src = i.select('img')[0]['src']
            price = i.select('.price_color')[0].text
            availablity = i.select('.instock.availability')[0].text

            print(title," | ",price," | ",availablity.strip()) #too many whitespaces
            
            
        print(f'End of page {x}')
        
        time.sleep(3)



except KeyboardInterrupt:
    print('Manual interruption of code. Program exited.')
        


if __name__ == "__main__":
    input("Press any key to exit...")
    
    


