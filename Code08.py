# Customer C makes a payment of 50 to Customer A
Xbank.book(debit=[('Reserves', 50)], credit=[('Customer A Deposit', 50)])
Ybank.book(debit=[('Customer C Deposit', 50)], credit=[('Reserves', 50)])
CustomerA.book(debit=[('Deposits', 50)], credit=[('Equity', 50)])
CustomerC.book(debit=[('Equity', 50)], credit=[('Deposits', 50)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(CustomerA.draw_balance_sheet("Customer A", width=500)))
display_svg(SVG(CustomerC.draw_balance_sheet("Customer C", width=500)))

# Money Supply
print_money_stocks()
