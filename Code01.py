from abcFinance import Ledger

from IPython.core.display import SVG
from IPython.display import display_svg

def print_money_stocks():
    # The amount of deposits in each customer's account is added to the bank money variable.
    Bank_Money = Xbankasi.get_balance('Customer A Deposit')[1]
    Bank_Money += Xbankasi.get_balance('Customer B Deposit')[1]
    Bank_Money += Xbankasi.get_balance('Customer C Deposit')[1]
    Bank_Money += Ybankasi.get_balance('Customer A Deposit')[1]
    Bank_Money += Ybankasi.get_balance('Customer B Deposit')[1]
    Bank_Money += Ybankasi.get_balance('Customer C Deposit')[1]
    
    # The amount of cash held by each customer and bank is added to the central bank money variable.
    Central_Bank_Money = MusteriA.get_balance('Cash')[1]
    Central_Bank_Money += MusteriB.get_balance('Cash')[1]
    Central_Bank_Money += MusteriC.get_balance('Cash')[1]
    Central_Bank_Money += Xbankasi.get_balance('Cash')[1]
    Central_Bank_Money += Ybankasi.get_balance('Cash')[1]
    
    print("Bank Money:",Bank_Money)
    if Central_Bank_Money>0:
        print("Central Bank Money:",Central_Bank_Money)
        
    # The sum of bank money and central bank money gives the money supply variable.
    print("Money Supply:",Bank_Money+Central_Bank_Money)

def print_balance_sheets_and_money_stocks(*args):
    MusteriA.book_end_of_period()
    MusteriB.book_end_of_period()
    MusteriC.book_end_of_period()
    
    if len(args)==0:
        args = ("b1","b2","pA","pB","pC","cb")
    if "b1" in args and Xbankasi.get_total_assets() > 0: display_svg(SVG(Xbankasi.draw_balance_sheet("Bank X", width=500)))
    if "b2" in args and Ybankasi.get_total_assets() > 0: display_svg(SVG(Ybankasi.draw_balance_sheet("Bank Y", width=500)))
    if "pA" in args and MusteriA.get_total_assets() > 0: display_svg(SVG(MusteriA.draw_balance_sheet("Customer A", width=500)))
    if "pB" in args and MusteriB.get_total_assets() > 0: display_svg(SVG(MusteriB.draw_balance_sheet("Customer B", width=500)))
    if "pC" in args and MusteriC.get_total_assets() > 0: display_svg(SVG(MusteriC.draw_balance_sheet("Customer C", width=500)))
    if "cb" in args and Merkez_Bankasi.get_total_assets() > 0: display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Central Bank", width=500)))
        
    print_money_stocks()
    
#  The residual account of each actor's balance sheet, (Asset-Liability), is called Equity.
Xbankasi = Ledger(residual_account_name="Equity")
Ybankasi = Ledger(residual_account_name="Equity")
MusteriA = Ledger(residual_account_name="Equity")
MusteriB = Ledger(residual_account_name="Equity")
MusteriC = Ledger(residual_account_name="Equity")
Merkez_Bankasi = Ledger(residual_account_name="Equity")


#  Assets and liabilities of banks are defined.
Xbankasi.make_asset_accounts(['Cash','Credits','Reserves','Interbank Receivables'])
Xbankasi.make_liability_accounts(['Customer A Deposit','Customer B Deposit','Customer C Deposit','Interbank Debt', 'Bond Issuance', 'Due to Central Bank'])
Ybankasi.make_asset_accounts(['Cash','Credits','Reserves','Interbank Receivables'])
Ybankasi.make_liability_accounts(['Customer A Deposit','Customer B Deposit','Customer C Deposit','Interbank Debt', 'Bond Issuance', 'Due to Central Bank'])

# Customer's asset and liability items are identified.
MusteriA.make_asset_accounts(['Cash','Deposits','Bank Bond'])
MusteriA.make_liability_accounts(['Credits'])
MusteriB.make_asset_accounts(['Cash','Deposits','Bank Bond'])
MusteriB.make_liability_accounts(['Credits'])
MusteriC.make_asset_accounts(['Cash','Deposits','Bank Bond'])
MusteriC.make_liability_accounts(['Credits'])


# Central Bank's assets and liabilities are defined.
Merkez_Bankasi.make_asset_accounts(['Government Securities','Credits to Banks'])
Merkez_Bankasi.make_liability_accounts(['Cash','Reserves'])


#Başlangıç
Xbankasi.book(debit=[('Cash',50)],credit=[('Equity',50)])
Ybankasi.book(debit=[('Cash',50)],credit=[('Equity',50)])
MusteriA.book(debit=[('Cash',100)],credit=[('Equity',100)])
Merkez_Bankasi.book(debit=[('Government Securities',200)],credit=[('Cash',200)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybankasi.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Customer A", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Central Bank", width=500)))

#Başlangıç- Para Arzı
print_money_stocks()
