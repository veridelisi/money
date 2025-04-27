# Bank Y borrows from the Central Bank
Ybank.book(debit=[('Reserves', 10)], credit=[('Due to Central Bank', 10)])
Central_Bank.book(debit=[('Credits to Banks', 10)], credit=[('Reserves', 10)])

# Balance Sheets
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(Central_Bank.draw_balance_sheet("Central Bank", width=500)))

# Money Supply
print_money_stocks()
