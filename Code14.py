# Bank Y collects deposits
Xbank.book(debit=[('Customer A Deposit', 20)], credit=[('Reserves', 20)])
Ybank.book(debit=[('Reserves', 20)], credit=[('Customer A Deposit', 20)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))

# Money Supply
print_money_stocks()
