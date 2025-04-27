# Banks withdraw cash from the Central Bank
Xbank.book(debit=[('Cash', 10)], credit=[('Reserves', 10)])
Ybank.book(debit=[('Cash', 10)], credit=[('Reserves', 10)])
Central_Bank.book(debit=[('Reserves', 20)], credit=[('Cash', 20)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(Ybank.draw_balance_sheet("Bank Y", width=500)))
display_svg(SVG(Central_Bank.draw_balance_sheet("Central Bank", width=500)))

# Money Supply
print_money_stocks()
