from ResourceStore import ResourceStore

store = ResourceStore()

store.add("food", 2)
store.add("water", 1)
store.add("oxygen", 3)

print("Starting stock:", store)

# failed_request = {"food": 1, "water": 2, "oxygen": 1}
# print("Request that needs too much water:", failed_request)
# print("Result:", store.try_consume(failed_request))
# print("Stock after failed request:", store)

# successful_request = {"food": 1, "water": 1, "oxygen": 1}
# print("Request with enough supplies:", successful_request)
# print("Result:", store.try_consume(successful_request))
# print("Stock after successful request:", store)

# print("Adding negative water:", store.add("water", -3))
# print("Adding unknown fuel:", store.add("fuel", 2))
# print("Final stock:", store)
# print("Food remaining:", store.quantity_of("food"))

