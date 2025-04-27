# Customer A deposits cash into Bank X
Xbank.book(debit=[('Cash', 100)], credit=[('Customer A Deposit', 100)])
CustomerA.book(debit=[('Deposits', 100)], credit=[('Cash', 100)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(CustomerA.draw_balance_sheet("Customer A", width=500)))

# Money Supply
print_money_stocks()
