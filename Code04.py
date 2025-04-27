# Bank X gives a loan to Customer B
Xbank.book(debit=[('Credits', 100)], credit=[('Customer B Deposit', 100)])
CustomerB.book(debit=[('Deposits', 100)], credit=[('Credits', 100)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(CustomerB.draw_balance_sheet("Customer B", width=500)))

# Money Supply
print_money_stocks()
