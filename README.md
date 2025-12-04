# Simple Shop Cashier Program

A very basic console-based shop program written in Python that lets you:
- Register customers
- Add products (with prices) to their basket
- Automatically apply discounts based on the total amount
- Print a receipt for each customer
- Show daily earnings and total items sold at the end of the day

Good for learning basic Python concepts like loops, functions, input validation, and simple calculations.

## Features

- Customer name validation (only letters and spaces allowed)
- Price input with error handling (only positive numbers)
- Tiered discount system:
  - 0% for total ≤ 20
  - 5% for total ≤ 50
  - 15% for total ≤ 100
  - 20% for total > 100
- Shows receipt for each customer
- At the end shows total earnings and number of items sold today
- Type `quit` when entering a customer name to close the program
- Type `0` when entering a price to finish the current customer's order
