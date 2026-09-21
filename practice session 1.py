cashier_name = "imran ahmed"
supermarket = "Tuskeys"
location = "Nairobi, Adams Arcade"
shopping_items = ["rice", "sugar", "maize flour", "milk", "eggs", "cooking oil", "meat", "bread"]
prices = {
    "rice": 1000,
    "sugar": 500,
    "maize flour": 800,
    "milk": 200,
    "eggs": 300,
    "cooking oil": 400,
    "meat": 1500,
    "bread": 250,
}
amount_received = 10000
total_cost = sum(prices.values())
change = amount_received - total_cost

print("name of cashier is", cashier_name)
print("supermarket is", supermarket)
print("location is", location)
print("shopping items are", shopping_items)
print("prices are", prices)
print("amount received is", amount_received)
print("total cost is", total_cost)
print("change is", change)