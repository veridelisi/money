# 💵 Money Simulation Project

This repository contains a collection of Python scripts simulating money creation, banking operations, and the mechanics of the financial system. Each script represents a specific part of the simulation process, from cash deposits to interbank transactions.

## 🚀 Quick Start

### 1. Install Required Package

Before running the scripts, install the `abcFinance` library:

```bash
pip install abcfinance

## 📂 Project Structure
Each file in this repository represents a specific step in the simulation process. Below is a detailed overview of the project structure, organized by key concepts and actions.

###📄 Code01.py
Description:
Initial setup of banks and customers.

Actions:
Create balance sheets for:
Bank X
Bank Y
Customer A
Customer B
Customer C
Central Bank
📄 Code02.py
Description:
Customer A deposits cash into Bank X.

Key Concept:
Increase in money stock through deposit creation.

📄 Code03.py
Description:
Bank X gives a loan to Customer B.

Key Concept:
Loan creates a new deposit in the banking system.

📄 Code04.py
Description:
Bank Y gives a loan to Customer C.

Key Concept:
Another deposit created through lending.

📄 Code05.py
Description:
Customer B repays part of their loan principal to Bank X.

Key Concept:
Reduction in outstanding loan and customer deposit.

📄 Code06.py
Description:
Customer A makes a payment to Customer B.

Key Concept:
Transfer between deposits without changing total money supply.

📄 Code07.py
Description:
Customer C pays Customer A.

Key Concept:
Interbank payment requiring reserve movements.

📄 Code08.py
Description:
Banks withdraw cash from the Central Bank.

Key Concept:
Reduction in reserves, increase in cash holdings.

📄 Code09.py
Description:
Customer A withdraws cash from Bank X.

Key Concept:
Cash leaves the banking system, reducing deposits.

📄 Code10.py
Description:
Bank Y borrows reserves from Bank X (interbank market transaction).

📄 Code11.py
Description:
Bank Y issues bonds to raise additional funds.

📄 Code12.py
Description:
Bank Y borrows directly from the Central Bank.

📄 Code13.py
Description:
Bank Y collects additional deposits from customers.

📄 Code14.py
Description:
Complex balance sheet operations combining multiple actions.

📄 Code15.py
Description:
Full simulation update.

Key Concept:
Integrates previous steps into a more advanced system evolution.

📈 Extend the Project
You can extend this project by adding features such as:

Interest Rates : Simulate how interest rates affect loans and deposits.
Bank Defaults : Model scenarios where banks fail to meet obligations.
Inflation and Money Velocity : Explore the impact of inflation on the economy.
Central Bank Interventions : Simulate quantitative easing or tightening.
📢 Notes
These scripts are developed for educational purposes to explain the basic mechanisms of the financial system. They provide a foundational understanding of money creation, banking operations, and central bank interactions.

👨‍💻 Author
Developed by veridelisi .

Feel free to contribute, open issues, or suggest improvements!

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
