from cgi import test
from urllib import response
import requests

def test_post():
    url = 'http://127.0.0.1:5000/add'
    myCafe = {
        'name': 'Cafeteria Iban',
        'map_url':'https://lh3.googleusercontent.com/p/AF1QipPBAt6bYna7pv5c7e_PhCDPMKPb6oFf6kMT2VQ1=s0',
        'img_url':'https://lh3.googleusercontent.com/p/AF1QipPBAt6bYna7pv5c7e_PhCDPMKPb6oFf6kMT2VQ1=s0',
        'loc':'Les Coves',
        'sockets':'true',
        'toilet':'true',
        'wifi':'true',
        'calls':'true',
        'seats':'0-10',
        'coffee_price':'1'
        }


    response = requests.post(url, data = myCafe)

    print(response)

def test_patch():    
    cafe_id = 1
    url = f"http://127.0.0.1:5000/patch_new_price/{cafe_id}"
    cafePrice = {
        'new_price':99999
    }
    response = requests.patch(url=url,data=cafePrice)
    print(response.text)

test_patch()

