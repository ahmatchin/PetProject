data = {
            1: ["LELO Sona vibrator", ["Vibrators"], 45, 10, 1],
            2: ["Queeny Love Giant Lover", ["Vibrators"], 37, 20, 2],
            3: ["Natural Vibrator", ["Vibrators"], 50, 30, 3],
            4: ["Cameron Realistic Hollow Dildo", ["Strap-on"], 60, 20, 4],
            5: ["OTOUCH - Airturn3 Masturbator", ["Vaginas and Masturbators"], 5, 10, 5],
            6: ["Lubricants", ["Sex Cosmetics Pharmacy"], 20, 60, 6],
            7: ["Real Feel Lady", ["Vaginas and Masturbators"], 50, 10, 7],
            8: ["Male doll with penis TRAVIS Luminous", ["Sex Dolls"], 85, 25, 8],
            9: ["Doll JEZEBEL", ["Sex Dolls"], 85, 5, 9],
            10: ["Penis Casts", ["Dildos"], 40, 5, 10],
            11: ["Glass Dildos", ["Dildos"], 40, 10, 11],
            12: ["Metal Dildos", ["Dildos"], 40, 10, 12]
}
cart = {}


def get_all():
    return data.values()


def get_all_category():
    category = []
    for x in data.values():
        for i in x[1]:
            if i not in category:
                category.append(i)
    return category


def choose_category(name):
    category = get_all_category()
    try:
        choosen_category = category[name - 1]
    except IndexError:
        return False
    products = filter(lambda x: choosen_category in x[1], data.values())
    return products


def add_to_cart(code, total):
        try:
            if cart.get(code):
                cart[code][3] += total
            else:
                cart[code] = data[code].copy()
                cart[code][3] = total
            return True
        except:
            return False


def get_name(code):
    return data[code][0]


def get_all_codes():
    return data.keys()


def get_price_all():
    price = 0
    for f in cart.values():
        price += f[2] * f[3]
    return price


def show_cart():
    return cart


def buy():
    global cart
    cart = {}
