# Bank Y borrows from Bank X
Xbank.book(debit=[('Interbank Receivables', 50)], credit=[('Reserves', 50)])
Ybank.book(debit=[('Reserves', 50)], credit=[('Interbank Debt', 50)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))

# Money Supply
print_money_stocks()
