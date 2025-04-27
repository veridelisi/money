# 💵 Money Simulation Project

This repository contains a collection of Python scripts simulating money creation, banking operations, and the mechanics of the financial system. Each script represents a specific part of the simulation process, from cash deposits to interbank transactions.

## 🚀 Quick Start

### 1. Install Required Package

Before running the scripts, install the `abcFinance` library:

pip install abcfinance

## 📂 Project Structure
### 📄 Code01.py (https://github.com/veridelisi/money/blob/main/Code01.py)
Bank and customer initial setup.

Create balance sheets for:

Bank X

Bank Y

Customer A

Customer B

Customer C

Central Bank

###  📄 Code02.py
Customer A deposits cash into Bank X.

Money stock increases through deposit creation.

###  📄 Code03.py
Bank X gives a loan to Customer B.

Loan creates a new deposit in the banking system.

###  📄 Code04.py
Bank Y gives a loan to Customer C.

Another deposit is created through lending.

### 📄 Code05.py
Customer B repays part of their loan principal to Bank X.

Reduces outstanding loan and customer deposit.

### 📄 Code06.py
Customer A makes a payment to Customer B.

Transfer between deposits without changing total money supply.

### 📄 Code07.py
Customer C makes a payment to Customer A.

Interbank transfer requiring reserve movements.

### 📄 Code08.py
Banks withdraw cash from the Central Bank.

Reduces reserves and increases cash holdings.

### 📄 Code09.py
Customer A withdraws cash from Bank X.

Cash leaves the banking system, reducing deposits.

### 📄 Code10.py
Bank Y borrows reserves from Bank X (interbank market transaction).

### 📄 Code11.py
Bank Y issues bonds to raise additional funds.

### 📄 Code12.py
Bank Y borrows directly from the Central Bank.

### 📄 Code13.py
Bank Y collects additional customer deposits.

### 📄 Code14.py
Complex balance sheet operations combining multiple steps.

### 📄 Code15.py
Full simulation update.

Integrates previous steps into a full financial system evolution.


## 👨‍💻 Author

Developed by **veridelisi**.

Feel free to contribute, open issues, or suggest improvements!

## 📜 License

This project is licensed under the **MIT License**.
