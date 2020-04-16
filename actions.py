from df_response import *
from database.db import initialize_db
from database.models import Order

tg = telegram_response()
ff = fulfillment_response()
products_final = []


def add_products(parameters: dict, session: str):
    product = parameters.get('product')
    # order_product = Order.objects.get(session = session)
    # if order_product.products is None:
    #     order_product.products = product
    # else:
    #     order_product.products.extend(product)
    # order_product.save()
    products_final.extend(product)

    fulfillment_text = 'Products added succesfully to Cart! Do you wish to add more product?'
    ff_text = ff.fulfillment_text(fulfillment_text)
    qr = tg.quick_replies(fulfillment_text, ['Check my cart', 'End conversation'])

    ff_msg = ff.fulfillment_messages([qr])

    reply = ff.main_response(ff_text, ff_msg)

    return reply


def delete_products(parameters: dict, session: str):
    products = parameters.get('product')
    try:
        for i in products:
            products_final.remove(i)
        fulfillment_text = 'Products removed from cart succesfully!'
    except ValueError:
        fulfillment_text = products, " weren't added to the cart!"

    ff_text = ff.fulfillment_text(fulfillment_text)
    qr = tg.quick_replies(fulfillment_text, ['Check my cart', 'End conversation'])

    ff_msg = ff.fulfillment_messages([qr])

    reply = ff.main_response(ff_text, ff_msg)
    return reply


def update_products(parameters: dict, session:str):
    product_from = parameters.get('product-from')
    product_to = parameters.get('product-to')

    try:
        for i in product_from:
            products_final.remove(i)
        products_final.extend(product_to)
        fulfillment_text = 'Products '+ ','.join(product_from) + ' swapped with '+ ','.join(product_to)+ ' succesfully!'
    except ValueError:
        fulfillment_text = product_to, " weren't added to the cart!"
    ff_text = ff.fulfillment_text(fulfillment_text)
    qr = tg.quick_replies(fulfillment_text, ['Check my cart', 'End conversation'])

    ff_msg = ff.fulfillment_messages([qr])

    reply = ff.main_response(ff_text, ff_msg)

    return reply


def check_order():
    
    if len(products_final) == 0:
        fulfillment_text = 'Your cart is empty!'
    else:
        fulfillment_text = ",".join(products_final)+ ' are in your cart!'
    ff_text = ff.fulfillment_text(fulfillment_text)
    qr = tg.quick_replies(fulfillment_text, ['Check my cart', 'End conversation'])

    ff_msg = ff.fulfillment_messages([qr])

    reply = ff.main_response(ff_text, ff_msg)

    return reply

