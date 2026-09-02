annual_salary = float(input("Write your annual salary: "))
portion_saved = float(input("Write the percentage in decimal form of the portion of salary to be saved: "))
total_cost = float(input("Write the cost of your dream home: "))
portion_down_payment = 0.25*total_cost
current_savings = 0.0
r = 0.04
investment = current_savings*r/12
months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + investment + portion_saved*(annual_salary/12)
    months = months + 1
    investment = current_savings*r/12
print("The number of months is: " , months)

