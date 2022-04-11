import data

def get_all():
    product = data.get_all()
    return '\n'.join([f"{(i[4])}.{', '.join(i[1])}: {(i[0])} - {i[2]}$, in quantity {i[3]}, product code {i[4]}" for i in product])

def get_all_category():
    category = data.get_all_category()
    return "\n".join([f"{i + 1}. {category[i]}" for i in range(0, len(category))])

def choose_category(name):
    choose = data.choose_category(name)
    if choose:
        return "\n".join(
            [f"{i[0]}. Product code - {i[4]}. Price - {i[2]}$." for i in choose])
    else:
        return "There is no such category."

def add_to_cart(code, total):
    products = data.get_all_codes()
    if code not in products:
        return 'There is no product with this product code.'
    elif data.add_to_cart(code, total):
        return f'{data.get_name(code)} add to your cart.'

def check_quantity(code, total):
    product = data.get_all()
    for i in product:
        if total > i[3]:
            return "Sorry, we don't have enough products at the moment! Try reducing the amount!"
    if data.add_to_cart(code, total):
        return f'{data.get_name(code)} add to your cart.'

def show_cart():
    cart = data.show_cart()
    if cart == {}:
        return "Your shopping cart is empty."
    cart_values = cart.values()
    return "In your cart:\n" + '\n'.join(
        [f"{i[0]}. {','.join(i[1])}. Product code - {i[4]}. Number of items in cart - {i[3]}" for i in
         cart_values])

def get_price_all():
    return f'Total price is {data.get_price_all()}$'

def buy():
    summary = data.get_price_all()
    data.buy()
    return f'Total cost - {summary}$'
