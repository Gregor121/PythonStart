import requests
import json

jita = '10000002'

dodixie = '10000032'

def region_orders(region_id):
    orders = []
    page = 1

    while True:
        url = 'https://esi.evetech.net/latest/markets/' + region_id +'/orders/?order_type=all&page=' + str(page)
        r = requests.get(url)
        total_pages = int(r.headers.get('x-pages'))
        print(url)
        
        if r.status_code != 200:
            print('Request failed to get 200: ' + str(r.status_code))
            exit(1)
        parsed = r.json()
        if page >= total_pages:
            break

        orders.extend(parsed)
        page = page + 1
        
    print('Finished downloading Region Data: ' + region_id)
    return orders

orders = region_orders(dodixie)
orders.extend(region_orders(jita))
orders_json = json.dumps(orders)

with open('market.json', 'w') as f:
    f.write(orders_json)

    

    

