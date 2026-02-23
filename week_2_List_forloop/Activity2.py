november_sales = [
    ['Chicken', 150, 'Food', 'Standard VAT', 804, 1200],
    ['Hotdog', 50, 'Food', 'Standard VAT', 1200, 2000],
    ['Rice', 40, 'Food', 'Zero-Rated', 1500, 2500],
    ['Bread', 30, 'Food', 'Standard VAT', 900, 1500],
    ['Soap', 25, 'Non-Food', 'Standard VAT', 600, 1000],
    ['Shampoo', 120, 'Non-Food', 'Standard VAT', 450, 800],
    ['Vitamins', 300, 'Health', 'VAT-Exempt', 300, 600],
    ['Medicine', 500, 'Health', 'VAT-Exempt', 200, 400],
    ['Notebook', 80, 'Stationery', 'Standard VAT', 750, 1200],
    ['Pen', 15, 'Stationery', 'Standard VAT', 1000, 1500],
    ['Pencil', 10, 'Stationery', 'Standard VAT', 1100, 1600],
    ['Eraser', 5, 'Stationery', 'Standard VAT', 950, 1400],
    ['Juice', 60, 'Food', 'Standard VAT', 850, 1300],
    ['Soda', 40, 'Food', 'Standard VAT', 950, 1400],
    ['Vegetables', 70, 'Food', 'Zero-Rated', 1300, 2000],
    ['Fruits', 90, 'Food', 'Zero-Rated', 1250, 1900],
    ['Toothpaste', 80, 'Non-Food', 'Standard VAT', 500, 900],
    ['Toothbrush', 60, 'Non-Food', 'Standard VAT', 550, 950],
    ['Bandages', 150, 'Health', 'VAT-Exempt', 400, 700],
    ['Calculator', 200, 'Stationery', 'Standard VAT', 300, 500],
] 

# --- [1] Total number of items sold ---
items_sold = 0
for item in november_sales:
    items_sold += item[4] # Index 4 is 'sold items quantity'

print(f"Total number of items sold: {items_sold}")
print("-" * 30)

# --- [2] Total number of sold items per category ---
food_qty = 0
non_food_qty = 0
health_qty = 0
stationery_qty = 0

for item in november_sales:
    category = item[2]
    quantity = item[4]
    if category == 'Food':
        food_qty += quantity
    elif category == 'Non-Food':
        non_food_qty += quantity
    elif category == 'Health':
        health_qty += quantity
    elif category == 'Stationery':
        stationery_qty += quantity

print(f"Food sold: {food_qty}")
print(f"Non-Food sold: {non_food_qty}")
print(f"Health sold: {health_qty}")
print(f"Stationery sold: {stationery_qty}")
print("-" * 30)

# --- [3] Total sales amount ---
total_sales_val = 0
for item in november_sales:
    # Price (Index 1) * Quantity (Index 4)
    total_sales_val += (item[1] * item[4])

print(f"Total sales amount: {total_sales_val}")
print("-" * 30)

# --- [4] Total sales amount per category ---
food_sales = 0
non_food_sales = 0
health_sales = 0
stationery_sales = 0

for item in november_sales:
    sales_amt = item[1] * item[4]
    if item[2] == 'Food':
        food_sales += sales_amt
    elif item[2] == 'Non-Food':
        non_food_sales += sales_amt
    elif item[2] == 'Health':
        health_sales += sales_amt
    elif item[2] == 'Stationery':
        stationery_sales += sales_amt

print(f"Food Total Sales: {food_sales}")
print(f"Non-Food Total Sales: {non_food_sales}")
print(f"Health Total Sales: {health_sales}")
print(f"Stationery Total Sales: {stationery_sales}")
print("-" * 30)

# --- [5] Average price of items per category ---
# We need Sum of Prices / Number of unique items in that category
f_price_sum, f_count = 0, 0
nf_price_sum, nf_count = 0, 0
h_price_sum, h_count = 0, 0
s_price_sum, s_count = 0, 0

for item in november_sales:
    price = item[1]
    cat = item[2]
    if cat == 'Food':
        f_price_sum += price
        f_count += 1
    elif cat == 'Non-Food':
        nf_price_sum += price
        nf_count += 1
    elif cat == 'Health':
        h_price_sum += price
        h_count += 1
    elif cat == 'Stationery':
        s_price_sum += price
        s_count += 1

print(f"Average Food Price: {f_price_sum / f_count:.2f}")
print(f"Average Non-Food Price: {nf_price_sum / nf_count:.2f}")
print(f"Average Health Price: {h_price_sum / h_count:.2f}")
print(f"Average Stationery Price: {s_price_sum / s_count:.2f}")
