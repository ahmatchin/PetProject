import business_logic


def get_value(message, end=":\n"):
    flag = False
    out_message = None
    while flag == False:
        out_message = input(message + end)
        flag = user_input_check(out_message)
    return int(out_message)


def user_input_check(message):
    if not message.isdigit():
        print('Please text a number!')
        return False
    return True


def show_message(message):
    print(message)
    print("==================================================================")


def show_all():
    show_message(business_logic.get_all())


def choose_category():
    number = int(get_value("Enter the number of the desired category."))
    data = business_logic.choose_category(number)
    show_message(data)


def add_to_cart():
    code = get_value('Select product code')
    total = get_value("How much you want?", end='\n')
    try:
        show_message(business_logic.check_quantity(code, total))
    except:
        show_message(business_logic.add_to_cart(code, total))


def show_cart():
    cart = business_logic.show_cart()
    show_message(cart)
    if cart != "Your cart is empty!":
        return True
    return False


def buy():
    show_message(business_logic.buy())


def total_price():
    show_message(business_logic.get_price_all())


def main_flow():
    while True:
        choosen_value = get_value("You are welcome! \nWe introdusing our intim internet-shop! \n\n"
                                  "Choose your action:\n0. Exit\n1. Show all products\n2. Choose category\n3. Add item to cart\n4. Show cart\n", end='')
        if choosen_value == 0:
            print("Are you leaving already? We will miss you...bye...")
            break
        elif choosen_value == 1:
            show_all()
        elif choosen_value == 2:
            choose_category()
            while True:
                choosen_value_on_category = get_value("Choose your action:\n0. Back to menu\n1. See another category\n",end='')
                if choosen_value_on_category == 0:
                    break
                elif choosen_value_on_category == 1:
                    choose_category()
                else:
                    show_message('Input true value!')
        elif choosen_value == 3:
            add_to_cart()
        elif choosen_value == 4:
            while True:
                if not show_cart():
                    break
                choosen_value_on_basket = get_value("Choose your action:\n0. Back to menu;\n1. Buy;\n2. Show total cost;\n", end='')
                if choosen_value_on_basket == 0:
                    break
                elif choosen_value_on_basket == 1:
                    buy()
                elif choosen_value_on_basket == 2:
                    total_price()
                else:
                    show_message('Input true value!')
