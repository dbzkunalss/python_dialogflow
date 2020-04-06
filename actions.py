from df_response import *

tg = telegram_response()
ff = fulfillment_response()
products_final = []

def add_products(products:list):
    products_final.extend(products)

    fulfillment_text = 'Products added succesfully to Cart! Do you wish to add more product?'
    ff_text = ff.fulfillment_text(fulfillment_text)
    qr = tg.quick_replies(fulfillment_text, ['YES','NO'])

    ff_msg = ff.fulfillment_messages([qr])

    reply = ff.main_response(fulfillment_text,ff_msg)

    return reply

def delete_products(products:list):
    try:
        products_final.remove()
        fulfillment_text = 'Products removed from cart succesfully!'
    except ValueError:
        fulfillment_text = products," weren't added to the cart!"
    
    
    ff_text = ff.fulfillment_text(fulfillment_text)
    tg_sr = tg.text_response(fulfillment_text)
    ff_msg = ff. fulfillment_messages([tg_sr])
    reply = ff.main_response(fulfillment_text, ff_msg)
    return reply

