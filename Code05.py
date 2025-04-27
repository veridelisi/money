# Bank Y gives a loan to Customer C
Ybank.book(debit=[('Credits', 100)], credit=[('Customer C Deposit', 100)])
CustomerC.book(debit=[('Deposits', 100)], credit=[('Credits', 100)])

# Balance Sheets
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(CustomerC.draw_balance_sheet("Customer C", width=500)))

# Money Supply
print_money_stocks()
