import json
import main
import asyncio

from model.product import Product


def lambda_handler(event, context):
    products = []
    for req_product in event:
        product = Product(req_product['product_id'], req_product['url'], req_product['name'], req_product['price'],
                          req_product['scrap_field'], req_product['created_at'], req_product['updated_at'])
        products.append(product)

    loop = asyncio.get_event_loop()

    result = loop.run_until_complete(main.main(products))

    products_res = []

    for product in result:
        products_res.append(
            {"product_id": product.product_id, "name": product.name, "price": product.price, "url": product.url,
             "scrap_field": product.scrap_field, "created_at": product.created_at, "updated_at": product.updated_at}
        )

    return {
        'statusCode': 200,
        'body': json.dumps(products_res)
    }
