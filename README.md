# 💵 Money Simulation Project

This repository contains a collection of Python scripts simulating **money creation** and **banking operations**.

Each file (`Code01.py`, `Code02.py`, etc.) represents a specific part of the simulation process:

- Cash deposits
- Bank loans
- Customer payments
- Reserve movements
- Money supply tracking
- And more...

---

## 🚀 Quick Start

### 1. Install the required package

> ❗ **Important:** Before running the scripts, install the `abcFinance` library:

```bash
pip install abcfinance

📂 Project Structure
📄 Code01.py
Bank and customer initial setup.

Create balance sheets for Bank X, Bank Y, Customer A, Customer B, Customer C, and Central Bank.

📄 Code02.py
Customer A deposits cash into Bank X.

Money stock increases through deposit creation.

📄 Code03.py
Bank X gives a loan to Customer B.

Loan creates a new deposit in the banking system.

📄 Code04.py
Bank Y gives a loan to Customer C.

Another new deposit created through lending.

📄 Code05.py
Customer B repays part of their loan principal to Bank X.

Reduces outstanding loan and customer deposit.

📄 Code06.py
Customer A makes a payment to Customer B.

Transfer between deposits without changing total money supply.

📄 Code07.py
Customer C pays Customer A.

Interbank payment requiring reserve movements.

📄 Code08.py
Banks withdraw cash from the Central Bank.

Reduces reserves, increases cash holdings.

📄 Code09.py
Customer A withdraws cash from Bank X.

Cash leaves the banking system, reducing deposits.

📄 Code10.py
Bank Y borrows reserves from Bank X (interbank market transaction).

📄 Code11.py
Bank Y issues bonds to raise additional funds.

📄 Code12.py
Bank Y borrows directly from the Central Bank.

📄 Code13.py
Bank Y collects additional deposits from customers.

📄 Code14.py
Complex balance sheet operations combining multiple actions.

📄 Code15.py
Full simulation update.

Integrates previous steps into a more advanced system evolution.

📢 Notes
These scripts are developed for educational purposes to explain basic financial system mechanisms.

You can extend the project by adding:

Interest rates

Bank defaults

Inflation and money velocity

Central Bank interventions

👨‍💻 Author
Developed by veridelisi
