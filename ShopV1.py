def get_customer_name():
    while True:
        name = input("New customer - please enter name or type 'quit' to exit:  ").strip()
        if name.lower() == "quit":
            print("Goodbye!")
            return None

        if name == "":
            print("Name cannot be empty")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters")
            continue

        print(f"Welcome to our shop {name}, what would you like to buy?")
        return name


def get_price():
    while True:
        price = input("Please enter price or type '0' to exit:  ").strip()
        try:
            if price == "0":
                return 0.0

            price = float(price)

            if price < 0:
                print("Price must be greater than 0")
                continue
            return price
        except ValueError:
            print("Please enter a valid price")
            continue


def calculate_discount(total_before):
    if total_before <= 20:
        bonus = 0
    elif total_before <= 50:
        bonus = 5
    elif total_before <= 100:
        bonus = 15
    else:
        bonus = 20
    return bonus

def print_receipt(name, customer_summary, customer_products, total_before, total_after):
    print(f"Summary for {name}\n"
          f"Products: {format_prices(customer_summary)}\n"
          f"Amount of products: {customer_products}\n"
          f"Price before discount: {total_before:.2f}\n"
          f"Discount: {calculate_discount(total_before)}\n"
          f"To payout: {total_after:.2f}")

def print_daily_summary(daily_earnings, total_items):
    print(f"We earn today {daily_earnings:.2f} and we sold {total_items} products!")

def format_prices(customer_summary):
    return ", ".join(f"{p:g}" for p in customer_summary)
def main():
    daily_earnings = 0.0
    total_items = 0

    while True:
        customer_summary = []
        customer_products = 0
        name = get_customer_name()
        if name is None:
            print_daily_summary(daily_earnings, total_items)
            break
        while True:
            price = get_price()
            if price == 0.0:
                total_before = sum(customer_summary)
                discount = total_before * calculate_discount(total_before) / 100
                total_after = total_before - discount
                daily_earnings += total_after
                print_receipt(name, customer_summary, customer_products, total_before, total_after)
                break
            customer_summary.append(price)
            customer_products += 1
            total_items += 1

if __name__ == "__main__":
    main()