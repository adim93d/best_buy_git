import products
import stores


def menu():
    print("""
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
----------
        """)


def user_menu_input():
    user_input = int(input("Please choose a number 1-4\n"
                           "To exit choose 4 or quit()\n"
                           "Input: "))
    return user_input


def start(shop, product):
    menu()
    try:
        user_input = user_menu_input()
    except ValueError:
        print("Invalid value, Please choose a number")
        user_input = user_menu_input()
    while True:
        if user_input == 1:
            shop.get_all_products()
            menu()
            user_input = user_menu_input()

        elif user_input == 2:
            total_quantity = shop.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")
            menu()
            user_input = user_menu_input()

        elif user_input == 3:
            shopping_cart(shop, product)
            menu()
            user_input = user_menu_input()

        elif user_input == 4:
            print("Good bye!")
            quit()


def shopping_cart(shop, product):
    basket = []
    all_products = shop.get_all_products
    buy = products.Product.buy
    print("------")
    all_products()
    print("------")
    print("When you want to finish order, enter empty text.")
    try:
        user_order_index = int(input("Which product # do you want? "))
        user_order_quantity = int(input("What amount do you want? "))
    except ValueError:
        user_input = input("No input, Did you tried to exit? Y/N ").lower()
        if 'y' in user_input:
            print("Good bye!")
            quit()
        else:
            pass
        user_order_index = int(input("Which product # do you want? "))
        user_order_quantity = int(input("What amount do you want? "))
    while user_order_index != "" or user_order_quantity != "":
        try:
            item = (shop.product_list[user_order_index - 1], user_order_quantity)
        except IndexError:
            print("Index out of range, choose item in range")
            user_order_index = int(input("Which product # do you want? "))
            user_order_quantity = int(input("What amount do you want? "))
            item = (shop.product_list[user_order_index - 1], user_order_quantity)
            print(item[0].buy(user_order_quantity))
        basket.append(item)
        stores.Store.order(shop, basket)

        print("------")
        all_products()
        print("------")
        try:
            user_order_index = int(input("Which product # do you want? "))
            user_order_quantity = int(input("What amount do you want? "))
        except ValueError:
            user_input = input("No input, Did you tried to exit? Y/N ").lower()
            if 'y' in user_input:
                print("Good bye!")
                break
            else:
                continue


def main():
    product_list = [
        products.Product(
            name="MacBook Air M2",
            price=1450,
            quantity=100,
            active=True),
        products.Product(
            name="Bose QuietComfort Earbuds",
            price=250,
            quantity=500,
            active=True),
        products.Product(
            name="Google Pixel 7",
            price=500,
            quantity=250,
            active=True),
        products.NonStockedProducts(
            name="Windows 10 Professional",
            price=350,
            active=True,
            quantity="Unlimited",
            ),
        products.LimitedProducts(
            name="Shipping",
            price=10,
            quantity=1,
            active=True,
            order_limit=1)
                    ]
    second_half_price = products.SecondHalfPrice("Second Half price!")
    third_one_free = products.ThirdOneFree("Third One Free!")
    thirty_percent = products.PercentDiscount("30% off!", percent=30)
    product_list[0].set_promo(second_half_price)
    product_list[1].set_promo(third_one_free)
    product_list[3].set_promo(thirty_percent)
    best_buy = stores.Store(product_list)
    start(best_buy, product_list)


if __name__ == '__main__':
    main()
