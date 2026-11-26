"""
Restaurant Menu and Billing System
----------------------------------
A beginner-friendly console project built with core Python concepts:
variables, dictionaries, lists, loops, if-else, functions and
exception handling. No external libraries are used.
"""

import sys
from datetime import datetime

# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------
RESTAURANT_NAME = "Spice Garden Restaurant"
DISCOUNT_LIMIT = 500      # Discount applies on bills of Rs. 500 or more
DISCOUNT_PERCENT = 10     # 10% discount
LINE_WIDTH = 52

# Use the rupee symbol if the console supports it, otherwise "Rs."
try:
    "\u20b9".encode(sys.stdout.encoding or "ascii")
    CURRENCY = "\u20b9"
except (UnicodeEncodeError, LookupError):
    CURRENCY = "Rs."

# Menu stored as a dictionary: item number -> item details
MENU = {
    1: {"name": "Paneer Butter Masala", "price": 220},
    2: {"name": "Dal Tadka",            "price": 150},
    3: {"name": "Veg Biryani",          "price": 180},
    4: {"name": "Butter Naan",          "price": 40},
    5: {"name": "Tandoori Roti",        "price": 20},
    6: {"name": "Masala Dosa",          "price": 120},
    7: {"name": "Gulab Jamun (2 pcs)",  "price": 60},
    8: {"name": "Sweet Lassi",          "price": 70},
    9: {"name": "Masala Chai",          "price": 25},
}


# ---------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------
def display_menu():
    """Print the restaurant menu in a neat table."""
    print("\n" + "=" * LINE_WIDTH)
    print(RESTAURANT_NAME.center(LINE_WIDTH))
    print("MENU".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)
    print(f"{'No.':<5}{'Item':<32}{'Price':>13}")
    print("-" * LINE_WIDTH)
    for number, item in MENU.items():
        price_text = f"{CURRENCY}{item['price']}"
        print(f"{number:<5}{item['name']:<32}{price_text:>13}")
    print("-" * LINE_WIDTH)


def get_whole_number(prompt, minimum, maximum):
    """
    Keep asking until the user enters a whole number between
    minimum and maximum (both included). Returns the number.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum <= value <= maximum:
                return value
            print(f"  Please enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid input! Please enter a whole number.")


def ask_yes_no(prompt):
    """Ask a yes/no question. Returns True for yes, False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please type 'y' for yes or 'n' for no.")


def take_order():
    """
    Let the customer pick items and quantities.
    Returns a list of dictionaries, one per ordered item.
    """
    order = []   # list of {"name", "price", "qty"}
    print("\nEnter the item number to order (enter 0 to finish).")

    while True:
        choice = get_whole_number("\nItem number (0 to finish): ", 0, len(MENU))

        if choice == 0:
            if not order:
                print("  You have not ordered anything yet!")
                continue
            break

        qty = get_whole_number(
            f"Quantity of {MENU[choice]['name']} (1-20): ", 1, 20
        )

        # If the item is already in the order, just increase its quantity
        for line in order:
            if line["name"] == MENU[choice]["name"]:
                line["qty"] += qty
                break
        else:
            order.append({
                "name": MENU[choice]["name"],
                "price": MENU[choice]["price"],
                "qty": qty,
            })
        print(f"  Added: {qty} x {MENU[choice]['name']}")

    return order


def calculate_bill(order):
    """
    Calculate subtotal, discount and final amount.
    Returns a tuple: (subtotal, discount, total)
    """
    subtotal = 0
    for line in order:
        subtotal += line["price"] * line["qty"]

    if subtotal >= DISCOUNT_LIMIT:
        discount = subtotal * DISCOUNT_PERCENT / 100
    else:
        discount = 0

    total = subtotal - discount
    return subtotal, discount, total


def print_receipt(order, bill_no):
    """Print the final formatted receipt."""
    subtotal, discount, total = calculate_bill(order)
    now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    print("\n" + "=" * LINE_WIDTH)
    print(RESTAURANT_NAME.center(LINE_WIDTH))
    print("CUSTOMER RECEIPT".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)
    print(f"Bill No : {bill_no:03d}")
    print(f"Date    : {now}")
    print("-" * LINE_WIDTH)
    print(f"{'Item':<24}{'Qty':>5}{'Price':>10}{'Amount':>13}")
    print("-" * LINE_WIDTH)

    for line in order:
        amount = line["price"] * line["qty"]
        print(f"{line['name']:<24}{line['qty']:>5}"
              f"{CURRENCY + str(line['price']):>10}"
              f"{CURRENCY + format(amount, '.2f'):>13}")

    print("-" * LINE_WIDTH)
    print(f"{'Subtotal':<39}{CURRENCY + format(subtotal, '.2f'):>13}")

    if discount > 0:
        label = f"Discount ({DISCOUNT_PERCENT}%)"
        print(f"{label:<39}{'-' + CURRENCY + format(discount, '.2f'):>13}")
    else:
        print(f"{'Discount':<39}{CURRENCY + '0.00':>13}")
        needed = DISCOUNT_LIMIT - subtotal
        print(f"(Order {CURRENCY}{needed:.2f} more to get "
              f"{DISCOUNT_PERCENT}% off!)")

    print("=" * LINE_WIDTH)
    print(f"{'TOTAL PAYABLE':<39}{CURRENCY + format(total, '.2f'):>13}")
    print("=" * LINE_WIDTH)
    print("Thank you for dining with us! Visit again.".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)


# ---------------------------------------------------------------
# Main program
# ---------------------------------------------------------------
def main():
    """Run the billing system until the user chooses to exit."""
    bill_no = 1
    print("\nWelcome to " + RESTAURANT_NAME + "!")

    try:
        while True:
            display_menu()
            order = take_order()
            print_receipt(order, bill_no)
            bill_no += 1

            if not ask_yes_no("\nPlace another order? (y/n): "):
                break

    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted.")

    print("\nThank you for using the Billing System. Goodbye!")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
