print('To calculate bill amount')

quantity_sold = int(input("Enter your quantity: "))
value = float(input("Enter value: "))
discount = float(input("discount: "))
tax = float(input("Enter tax amount: "))

total_cost=quantity_sold*value
print('total_cost',total_cost)
dis_amt=((total_cost*discount)/100)
print('dis_amt',dis_amt)
dis_cost=quantity_sold-dis_amt
print('dis_cost',dis_cost)
tax_amt=((tax*dis_cost)/100)
print('tax_amt',tax_amt)




5