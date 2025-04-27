# Banks receive reserves from the Central Bank
Xbank.book(debit=[('Reserves', 100)], credit=[('Due to Central Bank', 100)])
Ybank.book(debit=[('Reserves', 100)], credit=[('Due to Central Bank', 100)])
Central_Bank.book(debit=[('Credits to Banks', 200)], credit=[('Reserves', 200)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(Central_Bank.draw_balance_sheet("Central Bank", width=500)))

# Money Supply
print_money_stocks()
