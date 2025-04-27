# Customer A withdraws cash from Bank X
Xbank.book(debit=[('Customer A Deposit', 20)], credit=[('Cash', 20)])
CustomerA.book(debit=[('Cash', 20)], credit=[('Deposits', 20)])

# Balance Sheets
display_svg(SVG(Xbank.draw_balance_sheet("Bank X", width=500)))
display_svg(SVG(CustomerA.draw_balance_sheet("Customer A", width=500)))

# Money Supply
print_money_stocks()
