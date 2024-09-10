from apps.master_price.models import MainProducts
from apps.master_price.conecctions_shopify import ConnectionsShopify
from apps.master_price.graphiqL_queries import GET_COST_PRODUCT

def update_or_create_main_product(product_json):
    print('Parametros iniciales')
    con = ConnectionsShopify()
    id_product = product_json['id']
    title = product_json['title']
    tags = product_json['tags']
    vendor = product_json['vendor']
    status = product_json['status']
    variants = product_json['variants']
    category = product_json['category']['full_name']
    print('Parametros Variantes')
    for i in len(variants):
        response = con.request_graphql(GET_COST_PRODUCT.format('gid://shopify/ProductVariant/' + i['id']))
        object, created = MainProducts.objects.get_or_create(i['id'])
        object.id_product = id_product
        object.title = title
        object.tags = tags
        object.vendor = vendor
        object.status = status
        object.id_variantShopi = i['id']
        object.price = i['price']
        object.compare_at_price = i['compare_at_price']
        object.sku = i['sku']
        object.barcode = i['barcode']
        object.inventory_quantity = i['inventory_quantity']
        try:
            object.costo = float(response['productVariant']['unitCost']['amount'])
        except:    
            pass
        try:
            object.image_link = product_json['images'][0]['src']
        except:
            pass
        object.category = category
        object.save()
