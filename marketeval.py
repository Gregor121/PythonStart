import json

with open('market.json', 'r') as market:
    market_data = json.load(market)
    
#We want to be able to answer the questions:
#"is this a station we care about"
#and
#"what region does this station represent"
#That's it.
#Ignore systems. Just use stations.
#And only the first station (ignore multiple stations)

#have to go into file and check location_id(station)
#if that is true have to compare it to value to look at key? 

region = {
        "jita":{60003760}, 
        "dodixie":{60011866}
        }

group_orders = {
    60011866:{
    },
    60003760:{
    }
}
      

for market_info in market_data:
    filtered_location = group_orders.get(market_info["location_id"])

    if filtered_location is None:
        continue

    type_id = market_info["type_id"]
    filtered_orders = filtered_location.get(type_id)

    if filtered_orders is None:
        filtered_orders = [market_info]
    else:
        filtered_orders.append(market_info)    

    filtered_location[type_id] = filtered_orders

print(len(group_orders))
print(len(group_orders[60011866]))
print(len(group_orders[60003760]))

