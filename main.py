from ResourceStore import ResourceStore

store = ResourceStore()

store.add("water",5)
store.add("water",-3)
print(store.quantity_of("water"))