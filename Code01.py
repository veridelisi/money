from abcFinance import Ledger

from IPython.core.display import SVG
from IPython.display import display_svg

def print_money_stocks():
    # The amount of deposits in each customer's account is added to the bank money variable.
    Bank_Money = Xbank.get_balance('Customer A Deposit')[1]
    Bank_Money += Xbank.get_balance('Customer B Deposit')[1]
    Bank_Money += Xbank.get_balance('Customer C Deposit')[1]
    Bank_Money += Ybank.get_balance('Customer A Deposit')[1]
    Bank_Money += Ybank.get_balance('Customer B Deposit')[1]
    Bank_Money += Ybank.get_balance('Customer C Deposit')[1]
    
    # The amount of cash held by each customer and bank is added to the central bank money variable.
    Central_Bank_Money = CustomerA.get_balance('Cash')[1]
    Central_Bank_Money += CustomerB.get_balance('Cash')[1]
    Central_Bank_Money += CustomerC.get_balance('Cash')[1]
    Central_Bank_Money += Xbank.get_balance('Cash')[1]
    Central_Bank_Money += Ybank.get_balance('Cash')[1]
    
    print("Bank Money:",Bank_Money)
    if Central_Bank_Money>0:
        print("Central Bank Money:",Central_Bank_Money)
        
    # The sum of bank money and central bank money gives the money supply variable.
    print("Money Supply:",Bank_Money+Central_Bank_Money)

def print_balance_sheets_and_money_stocks(*args):
    CustomerA.book_end_of_period()
    CustomerB.book_end_of_period()
    CustomerC.book_end_of_period()
    
    if len(args)==0:
        args = ("b1","b2","pA","pB","pC","cb")
    if "b1" in args and Xbank.get_total_assets() > 0: display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
    if "b2" in args and Ybank.get_total_assets() > 0: display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
    if "pA" in args and CustomerA.get_total_assets() > 0: display_svg(SVG(CustomerA.draw_balance_sheet("Customer A", width=500)))
    if "pB" in args and CustomerB.get_total_assets() > 0: display_svg(SVG(CustomerB.draw_balance_sheet("Customer B", width=500)))
    if "pC" in args and CustomerC.get_total_assets() > 0: display_svg(SVG(CustomerC.draw_balance_sheet("Customer C", width=500)))
    if "cb" in args and Central_Bank.get_total_assets() > 0: display_svg(SVG(Central_Bank.draw_balance_sheet("Central Bank", width=500)))
        
    print_money_stocks()
    
#  The residual account of each actor's balance sheet, (Asset-Liability), is called Equity.
Xbank = Ledger(residual_account_name="Equity")
Ybank = Ledger(residual_account_name="Equity")
CustomerA = Ledger(residual_account_name="Equity")
CustomerB = Ledger(residual_account_name="Equity")
CustomerC = Ledger(residual_account_name="Equity")
Central_Bank = Ledger(residual_account_name="Equity")


#  Assets and liabilities of banks are defined.
Xbank.make_asset_accounts(['Cash','Credits','Reserves','Interbank Receivables'])
Xbank.make_liability_accounts(['Customer A Deposit','Customer B Deposit','Customer C Deposit','Interbank Debt', 'Bond Issuance', 'Due to Central Bank'])
Ybank.make_asset_accounts(['Cash','Credits','Reserves','Interbank Receivables'])
Ybank.make_liability_accounts(['Customer A Deposit','Customer B Deposit','Customer C Deposit','Interbank Debt', 'Bond Issuance', 'Due to Central Bank'])

# Customer's asset and liability items are identified.
CustomerA.make_asset_accounts(['Cash','Deposits','Bank Bond'])
CustomerA.make_liability_accounts(['Credits'])
CustomerB.make_asset_accounts(['Cash','Deposits','Bank Bond'])
CustomerB.make_liability_accounts(['Credits'])
CustomerC.make_asset_accounts(['Cash','Deposits','Bank Bond'])
CustomerC.make_liability_accounts(['Credits'])


# Central Bank's assets and liabilities are defined.
Central_Bank.make_asset_accounts(['Government Securities','Credits to Banks'])
Central_Bank.make_liability_accounts(['Cash','Reserves'])


#Start
Xbank.book(debit=[('Cash',50)],credit=[('Equity',50)])
Ybank.book(debit=[('Cash',50)],credit=[('Equity',50)])
CustomerA.book(debit=[('Cash',100)],credit=[('Equity',100)])
Central_Bank.book(debit=[('Government Securities',200)],credit=[('Cash',200)])

#Start- Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(CustomerA.draw_balance_sheet("Customer A", width=500)))
display_svg(SVG(Central_Bank.draw_balance_sheet("Central Bank", width=500)))

#Start- Money Supply
print_money_stocks()
