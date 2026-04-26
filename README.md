# Customer Orders Analysis (Python + Pandas)

## Project Overview

This project demonstrates how raw CSV data can be transformed into meaningful business insights using Python and pandas. It simulates a real-world scenario where customer and order datasets are processed to analyze revenue, identify trends, and support decision-making.

---

## Features

* Load and process CSV data
* Calculate revenue per order
* Merge datasets (customers + orders)
* Analyze revenue per customer and city
* Identify top customer and top-performing city

---

## Dataset Description

### Customers Dataset

* customer_id: Unique identifier for each customer
* name: Customer name
* city: Customer location

### Orders Dataset

* order_id: Unique order identifier
* customer_id: Links order to customer
* product: Product name
* price: Price per unit
* quantity: Number of units purchased

---

## Key Operations Performed

* Loaded CSV files using pandas
* Created a revenue column (price × quantity)
* Merged datasets using customer_id
* Grouped data to calculate total revenue per customer and city
* Filtered high-value transactions
* Identified top-performing customer and city

---

## Example Output

Top Customer:
John (Revenue: 950)

Top City:
Karachi (Revenue: 1040)

Revenue per Customer:

* John: 950
* Umar: 850
* Sara: 300

---

## Tech Stack

* Python
* Pandas

---

## Project Structure

customer-orders-analysis/
│
├── data/
│   ├── customers.csv
│   └── orders.csv
│
├── main.py
├── README.md
└── requirements.txt

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the script:
   python main.py

---

## Learning Outcomes

* Understanding of CSV data handling in Python
* Practical use of pandas for data manipulation
* Experience with grouping, aggregation, and filtering
* Improved problem-solving using real-world datasets

---

## Future Improvements

* Add data visualization using matplotlib or seaborn
* Build a command-line interface (CLI)
* Handle larger datasets efficiently
* Integrate with a database instead of CSV files

---

## Purpose

Built as a practice project to strengthen data analysis fundamentals and prepare for internships.
