# Customer B makes a principal payment to Bank X
Xbank.book(debit=[('Customer B Deposit', 70)], credit=[('Credits', 70)])
CustomerB.book(debit=[('Credits', 70)], credit=[('Deposits', 70)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(CustomerB.draw_balance_sheet("Customer B", width=500)))

# Money Supply
print_money_stocks()
