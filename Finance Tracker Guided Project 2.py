salary = input('Annual Salary:\n')
housing = input('Monthly Housing:\n')
bills = input('Monthly Bills:\n')
food = input('Weekly Food:\n')
travel = input('Annual Travel:\n')

print("--------------------------------\n----- FINANCIAL VISUALIZER -----\n--------------------------------")
print(f"Annual Salary: $ {salary}")
print(f"Monthly Housing: $ {housing}")
print(f"Monthly Bills: $ {bills}")
print(f"Weekly Food: $ {food}")
print(f"Annual Travel: $ {travel}")
print("--------------------------------")

def isinvalid(x):
    for i in x:
        if i.isnumeric() == False and i != '.':
            return True
    return False

if isinvalid(salary) or isinvalid(housing) or isinvalid(bills) or isinvalid(food) or isinvalid(travel):
    print('Invalid input, please try again.')
else:
    print('All inputs confirmed valid.')   
salary  = float(salary)
housing = float(housing)
bills   = float(bills)
food    = float(food)
travel  = float(travel)

# Tax calculator
tax = 0
if salary <= 10000:
    tax = round(salary * 0.05, 2)
elif salary <= 40000:
    tax = round(salary * 0.1, 2)
elif salary <= 80000:
    tax = round(salary * 0.15, 2)
else:
    tax = round(salary * 0.2, 2)
    
# Annual calculations and percentages
annual_housing = housing * 12
annual_bills = bills * 12
annual_food = food * 52
extra = salary - annual_housing - annual_bills - annual_food - travel

percent_housing = annual_housing / salary 
percent_bills = annual_bills / salary 
percent_food = annual_food / salary 
percent_travel = travel / salary 
percent_tax = tax / salary
percent_extra = extra / salary

# Bar chart calculations

bar = "#"
house_chart = int(percent_housing * 100)
house_bar = house_chart * bar
bills_chart = int(percent_bills *100)
bills_bar = bills_chart * bar
food_chart = int(percent_food * 100)
food_bar = food_chart * bar
travel_chart = int(percent_travel * 100)
travel_bar = travel_chart * bar
tax_chart = int(percent_tax * 100)
tax_bar = tax_chart * bar
extra_chart = int(percent_extra * 100)
extra_bar = extra_chart * bar

dash = "-"
width = max(house_chart, bills_chart, food_chart, travel_chart, tax_chart, extra_chart)
boundary = (width * dash) + "-------------------------------------"

print()
print(boundary)
print('housing | $' + format(annual_housing, '11,.2f') + ' ', end='')
print('| ' + format(percent_housing * 100, '5,.1f') + '% | ' + (house_bar))
print('  bills | $' + format(annual_bills, '11,.2f') + ' ', end='')
print('| ' + format(percent_bills * 100, '5,.1f') + '% | ' + (bills_bar))
print('   food | $' + format(annual_food, '11,.2f') + ' ', end='')
print('| ' + format(percent_food * 100, '5,.1f') + '% | ' + (food_bar))
print(' travel | $' + format(travel, '11,.2f') + ' ', end='')
print('| ' + format(percent_travel * 100, '5,.1f') + '% | ' + (travel_bar))
print('    tax | $' + format(tax, '11,.2f') + ' ', end='')
print('| ' + format(percent_tax, '5,.1f') + '% | ' + (tax_bar))
print('  extra | $' + format(extra, '11,.2f') + ' ', end='')
print('| ' + format(percent_extra, '5,.1f') + '% | ' + (extra_bar))
print(boundary)
