import pandas as pd
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

orders["revenue"] = orders["quantity"] * orders["price"]
# print(orders)

merged = pd.merge(orders,customers, on="customer_id")
# print(merged)

# revenue_per_city = merged.groupby("city")["revenue"].sum()
# print(revenue_per_city)

# highest_revenue = revenue_per_city.idxmax()
# print(f"Highest grossing store is {highest_revenue}")

revenue_per_person = merged.groupby("name")["revenue"].sum()
print(revenue_per_person)

highest_rev_customer = revenue_per_person.idxmax()
print(f"Highest revenue generating customer is {highest_rev_customer}")