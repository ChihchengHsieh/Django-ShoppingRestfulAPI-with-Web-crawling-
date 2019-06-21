import requests
from bs4 import BeautifulSoup

def crawleChemistWarehouse():
    res = requests.get('https://www.chemistwarehouse.com.au/bestsellers?size=120')
    soup = BeautifulSoup(res.text, 'html.parser')
    all_products = soup.select('a.product-container')


    return_product = []

    for p in all_products:
        if p.select('img.product_image_overlay'): # get all half price
            # print(p['href']) # get all address to the single page
            # Check if it has a 1/2 image
            sub_req = requests.get('https://www.chemistwarehouse.com.au/%s'% p['href'])        
            sub_soup = BeautifulSoup(sub_req.text)
            # print(sub_soup.select('div.product-name h1')[0].text.strip())
            # print('The length is %d' % len(sub_soup.select('div.productDetail td#product_details_left div#product_images div#this_slider div#slider_pi_container')))
            img_list = []
            for imgs in sub_soup.select('div.productDetail td#product_details_left div#product_images div#this_slider div#slider_pi_container a.image_enlarger'):
                img_list.append(imgs['href'])
                

            # print(sub_soup.select('div.Price span')[0].text.strip())
            savings = sub_soup.select('div.Savings')[0].text.strip()
            savings = savings[savings.find('$'):]
            # print(savings)
            retailPrice = sub_soup.select('div.retailPrice')[0].text.strip()
            retailPrice = retailPrice[retailPrice.find('$'):]
            # print(retailPrice)


            return_product.append({
                'name': sub_soup.select('div.product-name h1')[0].text.strip(),
                'imgs': img_list,
                'currentPrice': sub_soup.select('div.Price span')[0].text.strip(),
                'saving': savings,
                'retialPrice': retailPrice
            })
    return return_product    