from django.shortcuts import render
from django.http import HttpResponse
from webapp import recommend
from webapp import data

cartList = []


def index(request):
    names = data.get_name()
    cartAmount = len(cartList)
    return render(request, 'index.html', {'names': names, 'cart': cartAmount})


def showDetail(request):
    name = request.POST.get('game')
    desc = data.get_data(name, 'desc_snippet')
    dev = data.get_data(name, 'developer')
    pub = data.get_data(name, 'publisher')
    date = data.get_data(name, 'release_date')
    tags = data.get_data(name, 'popular_tags')
    price = data.get_data(name, 'original_price')
    tags = tags.replace(',', ' , ')
    cartAmount = len(cartList)
    recs = recommend.TF_IDF(name, 5)
    return render(request, 'detail.html', {'name': name, 'desc': desc, 'dev': dev, 'pub': pub, 'date': date, 'tags': tags, 'price': price, 'recs':recs, 'cart': cartAmount})


def addToCart(request):
    name = request.POST.get('game')
    priceList = []
    total = 0
    if(name != None):
        cartList.append(name)
        for cart in cartList:
            price = data.get_data(cart, 'original_price')
            total = total + price
            priceList.append(price)
        return render(request, 'cart.html', {'cartList': cartList, 'pricelist': priceList, 'total': total})


def cart(request):
    priceList = []
    total = 0
    for cart in cartList:
        price = data.get_data(cart, 'original_price')
        total = total + price
        priceList.append(price)
    return render(request, 'cart.html', {'cartList': cartList, 'pricelist': priceList, 'total': total})


def remove(request):
    priceList = []
    cartList.clear()
    total = 0
    return render(request, 'cart.html', {'cartList': cartList, 'pricelist': priceList, 'total': total})


def thank(request):
    cartList.clear()
    return render(request, 'thank.html',{'cartList': cartList})
