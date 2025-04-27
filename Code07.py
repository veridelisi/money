# Customer A makes a payment of 50 to Customer B
Xbank.book(debit=[('Customer A Deposit', 50)], credit=[('Customer B Deposit', 50)])
CustomerA.book(debit=[('Equity', 50)], credit=[('Deposits', 50)])
CustomerB.book(debit=[('Deposits', 50)], credit=[('Equity', 50)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(CustomerA.draw_balance_sheet("Customer A", width=500)))
display_svg(SVG(CustomerB.draw_balance_sheet("Customer B", width=500)))

# Money Supply
print_money_stocks()
