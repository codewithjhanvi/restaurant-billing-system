# 🍽️ Restaurant Menu and Billing System

A simple console-based Python application that displays a restaurant menu, takes
customer orders, calculates the bill automatically, applies a discount and prints
a neatly formatted receipt.

Built as a **BCA Computer Science mini-project** using only core Python concepts.

---

## 📌 Features

- Displays a restaurant menu with item numbers and prices
- Lets the customer order **multiple items** with **quantities**
- Repeated items are merged automatically (e.g. ordering Naan twice adds the quantities)
- Calculates the **subtotal, discount and final total** automatically
- Applies a **10% discount on bills of ₹500 or above**
- Prints a **formatted receipt** with bill number, date and time
- **Input validation** for item numbers, quantities and yes/no answers (no crashes on wrong input)
- Option to **place another order or exit**
- Works in **VS Code** and **Python IDLE**

## 🛠️ Technologies & Concepts Used

| Item | Details |
|------|---------|
| Language | Python 3.8 or higher |
| Libraries | Only the built-in `sys` and `datetime` modules (nothing to install) |
| Concepts | Variables, Dictionaries, Lists, Loops, if-else, Functions, Exception Handling (`try-except`) |

## 📁 Project Structure

```
restaurant-billing-system/
│
├── main.py        # Complete program code
├── README.md      # Project documentation
└── .gitignore     # Files Git should ignore
```

## ⚙️ Installation

1. Install **Python 3.8+** from [python.org](https://www.python.org/downloads/).
   During installation on Windows, tick **"Add Python to PATH"**.
2. Check the installation:
   ```bash
   python --version
   ```
3. Download or clone this repository:
   ```bash
   git clone https://github.com/<your-username>/restaurant-billing-system.git
   cd restaurant-billing-system
   ```

No extra packages are required.

## ▶️ How to Run

**VS Code**
1. Open the project folder (`File → Open Folder`).
2. Open `main.py`.
3. Click the ▶ **Run Python File** button, or type in the terminal:
   ```bash
   python main.py
   ```

**Python IDLE**
1. Open `main.py` with `File → Open`.
2. Press **F5** (or `Run → Run Module`).

**Command line**
```bash
python main.py        # Windows
python3 main.py       # Linux / macOS
```

## 🧾 How to Use

1. The menu is displayed.
2. Enter an **item number**, then the **quantity**.
3. Repeat for more items. Enter **0** to finish ordering.
4. The receipt is printed.
5. Type **y** to place another order or **n** to exit.

## 💡 Discount Rule

| Bill Amount | Discount |
|-------------|----------|
| Below ₹500 | None |
| ₹500 or above | 10% |

## 🖥️ Sample Output

```
====================================================
              Spice Garden Restaurant               
                        MENU                        
====================================================
No.  Item                                    Price
----------------------------------------------------
1    Paneer Butter Masala                     ₹220
2    Dal Tadka                                ₹150
3    Veg Biryani                              ₹180
4    Butter Naan                               ₹40
5    Tandoori Roti                             ₹20
6    Masala Dosa                              ₹120
7    Gulab Jamun (2 pcs)                       ₹60
8    Sweet Lassi                               ₹70
9    Masala Chai                               ₹25
----------------------------------------------------

Enter the item number to order (enter 0 to finish).

Item number (0 to finish): 1
Quantity of Paneer Butter Masala (1-20): 2
  Added: 2 x Paneer Butter Masala

Item number (0 to finish): 2
Quantity of Dal Tadka (1-20): 4
  Added: 4 x Dal Tadka

Item number (0 to finish): 3
Quantity of Veg Biryani (1-20): 1
  Added: 1 x Veg Biryani

Item number (0 to finish): 0

====================================================
              Spice Garden Restaurant               
                  CUSTOMER RECEIPT                  
====================================================
Bill No : 001
Date    : 26-11-2026 09:41 AM
----------------------------------------------------
Item                      Qty     Price       Amount
----------------------------------------------------
Paneer Butter Masala        2      ₹220      ₹440.00
Dal Tadka                   4      ₹150      ₹600.00
Veg Biryani                 1      ₹180      ₹180.00
----------------------------------------------------
Subtotal                                    ₹1220.00
Discount (10%)                              -₹122.00
====================================================
TOTAL PAYABLE                               ₹1098.00
====================================================
     Thank you for dining with us! Visit again.     
====================================================

Place another order? (y/n): n

Thank you for using the Billing System. Goodbye!
```

## 🚀 Future Improvements

- Save receipts to a text file
- Add categories (Starters, Main Course, Desserts)
- Add GST calculation
- Admin option to add or edit menu items
- Build a GUI using Tkinter

## 👤 Author

**Your Name** – BCA Computer Science
Roll No: XXXXXXX | College: Your College Name

## 📄 License

This project is created for educational purposes. Feel free to use and modify it.
