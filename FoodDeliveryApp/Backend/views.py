import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .db import customers_col, restaurants_col, foods_col, cart_col, orders_col


def json_response(data, status=200):
    return JsonResponse(data, status=status, safe=False)


def parse_body(request):
    return json.loads(request.body.decode('utf-8'))


def serialize(doc):
    doc['_id'] = str(doc['_id'])
    return doc


# ==================== CUSTOMER APIs ====================

@csrf_exempt
@require_http_methods(["POST"])
def add_customer(request):
    body = parse_body(request)
    customers_col.insert_one(body)
    return json_response({'message': 'Customer added successfully'}, 201)


@csrf_exempt
@require_http_methods(["GET"])
def get_customers(request):
    customers = [serialize(doc) for doc in customers_col.find()]
    return json_response(customers)


@csrf_exempt
@require_http_methods(["PUT"])
def update_customer(request, id):
    body = parse_body(request)
    customers_col.update_one({'customer_id': id}, {'$set': body})
    return json_response({'message': 'Customer updated successfully'})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_customer(request, id):
    customers_col.delete_one({'customer_id': id})
    return json_response({'message': 'Customer deleted successfully'})


# ==================== RESTAURANT APIs ====================

@csrf_exempt
@require_http_methods(["POST"])
def add_restaurant(request):
    body = parse_body(request)
    restaurants_col.insert_one(body)
    return json_response({'message': 'Restaurant added successfully'}, 201)


@csrf_exempt
@require_http_methods(["GET"])
def get_restaurants(request):
    search = request.GET.get('search', '')
    if search:
        query = {
            '$or': [
                {'restaurant_name': {'$regex': search, '$options': 'i'}},
                {'cuisine': {'$regex': search, '$options': 'i'}},
                {'location': {'$regex': search, '$options': 'i'}}
            ]
        }
        restaurants = [serialize(doc) for doc in restaurants_col.find(query)]
    else:
        restaurants = [serialize(doc) for doc in restaurants_col.find()]
    return json_response(restaurants)


@csrf_exempt
@require_http_methods(["PUT"])
def update_restaurant(request, id):
    body = parse_body(request)
    restaurants_col.update_one({'restaurant_id': id}, {'$set': body})
    return json_response({'message': 'Restaurant updated successfully'})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_restaurant(request, id):
    restaurants_col.delete_one({'restaurant_id': id})
    return json_response({'message': 'Restaurant deleted successfully'})


# ==================== FOOD MENU APIs ====================

@csrf_exempt
@require_http_methods(["POST"])
def add_food(request):
    body = parse_body(request)
    foods_col.insert_one(body)
    return json_response({'message': 'Food item added successfully'}, 201)


@csrf_exempt
@require_http_methods(["GET"])
def get_foods(request):
    search = request.GET.get('search', '')
    restaurant = request.GET.get('restaurant', '')
    if restaurant:
        foods = [serialize(doc) for doc in foods_col.find({'restaurant_name': restaurant})]
    elif search:
        query = {
            '$or': [
                {'food_name': {'$regex': search, '$options': 'i'}},
                {'category': {'$regex': search, '$options': 'i'}},
                {'restaurant_name': {'$regex': search, '$options': 'i'}}
            ]
        }
        foods = [serialize(doc) for doc in foods_col.find(query)]
    else:
        foods = [serialize(doc) for doc in foods_col.find()]
    return json_response(foods)


@csrf_exempt
@require_http_methods(["PUT"])
def update_food(request, id):
    body = parse_body(request)
    foods_col.update_one({'food_id': id}, {'$set': body})
    return json_response({'message': 'Food item updated successfully'})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_food(request, id):
    foods_col.delete_one({'food_id': id})
    return json_response({'message': 'Food item deleted successfully'})


# ==================== CART APIs ====================

@csrf_exempt
@require_http_methods(["POST"])
def add_cart(request):
    body = parse_body(request)
    body['total_price'] = body['quantity'] * body['price']
    cart_col.insert_one(body)
    return json_response({'message': 'Item added to cart successfully'}, 201)


@csrf_exempt
@require_http_methods(["GET"])
def get_cart(request):
    customer = request.GET.get('customer', '')
    if customer:
        cart_items = [serialize(doc) for doc in cart_col.find({'customer_name': customer})]
    else:
        cart_items = [serialize(doc) for doc in cart_col.find()]
    return json_response(cart_items)


@csrf_exempt
@require_http_methods(["PUT"])
def update_cart(request, id):
    body = parse_body(request)
    body['total_price'] = body['quantity'] * body['price']
    cart_col.update_one({'cart_id': id}, {'$set': body})
    return json_response({'message': 'Cart updated successfully'})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_cart(request, id):
    cart_col.delete_one({'cart_id': id})
    return json_response({'message': 'Item removed from cart successfully'})


# ==================== ORDER APIs ====================

@csrf_exempt
@require_http_methods(["POST"])
def add_order(request):
    body = parse_body(request)
    orders_col.insert_one(body)
    return json_response({'message': 'Order placed successfully'}, 201)


@csrf_exempt
@require_http_methods(["GET"])
def get_orders(request):
    customer = request.GET.get('customer', '')
    if customer:
        orders = [serialize(doc) for doc in orders_col.find({'customer_name': customer})]
    else:
        orders = [serialize(doc) for doc in orders_col.find()]
    return json_response(orders)


@csrf_exempt
@require_http_methods(["PUT"])
def update_order(request, id):
    body = parse_body(request)
    orders_col.update_one({'order_id': id}, {'$set': body})
    return json_response({'message': 'Order updated successfully'})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_order(request, id):
    orders_col.delete_one({'order_id': id})
    return json_response({'message': 'Order deleted successfully'})
