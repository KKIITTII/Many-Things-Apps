from django.shortcuts import render, redirect
import omise
import requests

PUBLIC_KEY = "pkey_test_5yy97vgj8ukkpmjtjxu"
SECRET_KEY = "skey_test_5ym3oai2kcycw0r1yj3"

# Create your views here.
def pay(request):
    return render(request, 'omise_payment/index.html')

def charge(request):
    print(request.POST)
    omise.api_public = PUBLIC_KEY
    omise.api_secret = SECRET_KEY
    token_id = request.POST['omiseToken']
    source_id = request.POST['omiseSource']
    retrieve_source = omise.Source.retrieve( request.POST['omiseSource'])
    print(vars(retrieve_source))
    # print(retrieve_source.type)
    
    # credit or debit
    if token_id:
        # if amount and currency are as same as in cart then create charge 
        charge = omise.Charge.create(
        amount=100000,
        currency="THB",
        card=token_id,
        return_uri="https://www.youtube.com",
        )
    # alipay, wechat, qr all use publickey
    if source_id:
        source = omise.Source.create(
        type=f"{retrieve_source.type}",
        amount=f"{retrieve_source.amount}",
        currency="THB"
        # source=source_id,
        )
        charge = omise.Charge.create(
        amount=source.amount,
        currency=source.currency,
        source=source.id,
        return_uri="https://www.youtube.com",
        )
        print(charge.authorize_uri)
        # image_url = charge.source.scannable_code.image.download_uri
    return redirect(charge.authorize_uri)
    # return render(reuest, 'omise_payment/index.html')
    
def webhook(request):
    print(vars(request.POST))
    # if items still available then charge.capture() else charge.reverse() after retrieve charge
    return render(reuest, 'omise_payment/index.html')