import pprint

market_orders = [
    {"location_id": 5, "type_id": 213, "price": 6},
    {"location_id": 5, "type_id": 213, "price": 8},
    {"location_id": 5, "type_id": 342, "price": 3},
    {"location_id": 6, "type_id": 600, "price": 1}
]

# This is how this starts
region_items = {
    5: {},
    6: {},
}

# This is how we want it to end: 
region_items_finished = {
    5: {
        213: [
            {"location_id": 5, "type_id": 213, "price": 6},
            {"location_id": 5, "type_id": 213, "price": 8}
        ],
        342: [
            {"location_id": 5, "type_id": 342, "price": 3}
        ],
    },
    6: {
        600: [
            {"location_id": 6, "type_id": 600, "price": 1}
        ]
    }
}

region_max_prices = {
    5: {},
    6: {}
}

region_max_prices_finished = {
    5: {
        213: 8,
        342: 3
    },
    6: {
        600: 1
    }
}

for order in market_orders:
    # Get the order's location_id and type_id
    order_location_id = order["location_id"]
    order_type_id = order["type_id"]
    order_price = order["price"]

    # Get the list of orders for this item type
    region_item_types = region_items.get(order_location_id)
    region_item_prices = region_max_prices.get(order_location_id)

    # This means that the location_id is not in region_items, meaning that
    # it's none of our preconfigured location ids and so we just go to the
    # next order because we don't care about this one.
    if region_item_types is None:
        continue

    # Get the item orders for the specific item type id of the order
    item_orders = region_item_types.get(order_type_id)
    item_max_price = region_item_prices.get(order_type_id)

    if item_orders is None:
        # If item_orders is none, that means we've never seen this item type
        # before which means there's nothing there in our dictionary.
        # We need to add the entry into the dictionary, it will start
        region_item_types[order_type_id] = [order]
    else:
        region_item_types[order_type_id] = item_orders.append(order)    

    if item_max_price is None or order_price > item_max_price:
        region_item_prices[order_type_id] = order_price

pprint.pprint(region_items)
pprint.pprint(region_max_prices)