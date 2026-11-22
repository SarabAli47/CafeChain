import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.width", 140)
pd.set_option("display.max_columns", 30)

# Reading csv files
stores = pd.read_csv("stores.csv")
products = pd.read_csv("products.csv")
price_history = pd.read_csv("price_history.csv", dtype=str)
customers_raw = pd.read_csv("customers.csv",dtype=str)
orders_raw = pd.read_csv("orders.csv", dtype=str)
items_raw = pd.read_csv("order_items.csv", dtype=str)
staff_raw = pd.read_csv("staff.csv", dtype=str)
shifts_raw = pd.read_csv("shifts.csv", dtype=str)
reviews_raw = pd.read_csv("reviews.csv", dtype=str)
weather = pd.read_csv('weather.csv', parse_dates=['date'])
calendar = pd.read_csv('calendar.csv', parse_dates=['date'])