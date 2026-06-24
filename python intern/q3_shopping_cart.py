# PART A - Spot the Bug
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))      # ['apple']
print(add_item("banana"))     # ['apple', 'banana'] - BUG! Same list reused
print(add_item("milk", ["bread"]))  # ['bread', 'milk']
print(add_item("eggs"))       # ['apple', 'banana', 'eggs']


# PART B - Fixed Version
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item_fixed("apple"))   # ['apple']
print(add_item_fixed("banana"))  # ['banana']


# PART C - Complete Shopping Cart
def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def calculate_total(cart):
    total = sum(item["price"] * item["qty"] for item in cart["items"])
    discount = total * (cart["discount"] / 100)
    return total - discount

# Demonstration
cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Priya", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)
add_to_cart(cart2, "Book", 300, 3)
add_to_cart(cart2, "Pen", 50, 5)

print(f"Cart1 total: ₹{calculate_total(cart1)}")
print(f"Cart2 total: ₹{calculate_total(cart2)}")
print(f"Cart1 items: {len(cart1['items'])}, Cart2 items: {len(cart2['items'])}")


# DISCUSSION POINTS (as comments)
# 1. discount=0 safe (int immutable), cart=[] dangerous (list mutable - same object reused)
# 2. Rebinding = new value assignment, Mutating = changing object contents
# 3. Mutable: list, dict, set | Immutable: tuple, str, int, float, bool
# 4. Yes, because list passed by reference - modifications affect original