# yami_task

A Python-based **Shopping Order Management System** built using Object-Oriented Programming (OOP) concepts.

## Description

This project simulates a simple shop system where customers can place orders for products, cancel orders, and view sales reports. It handles stock management, discount calculations, and a waiting list when stock runs out.

## Features

- Place orders with automatic stock tracking
- Waiting list management when stock is unavailable
- Order cancellation with automatic waiting list fulfillment
- Discount system (premium customers and bulk orders)
- Sales report generation
- Total revenue and average utilization calculation

## Concepts Used

- Object-Oriented Programming (Classes, Inheritance)
- Lambda functions
- Lists, Tuples, Dictionaries, Sets
- Loops and conditionals
- f-strings and string formatting

## How It Works

1. Products are defined with ID, name, category, stock, price, and discount.
2. Customers can be premium (gets 10% discount) or regular.
3. Bulk orders of 2+ items get an additional 5% discount.
4. If stock is unavailable, the customer is added to a waiting list.
5. On cancellation, the next person in the waiting list is automatically assigned the order.

## Sample Output

```
Order Placed: 1 42750.0
Order Placed: 2 47500.0
Added to Waiting List: Indravathi
Order Placed: 3 47500.0
P101 2 2 0 95000.0
P102 1 0 0 0
Total Revenue: 95000.0
Average Utilization: 50.0
```

## How to Run

```bash
python task.py
```

## Author

**Yami Chowdary**  
GitHub: [@Yamichowdary2505](https://github.com/Yamichowdary2505)
