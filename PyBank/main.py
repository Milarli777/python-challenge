#first I need to create the import section bit
import os
import csv
#show where the file path is
csvlocation =os.path.join('.', 'Resources', 'budget_data.csv')

budgetdata = []

# need to open the file and move into looping through it all to store in a dict remember your commands like append and len 
with open(csvlocation) as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        budgetdata.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

total_months = len(budgetdata)

previous_amount = budgetdata[0]["amount"]
for i in range(total_months):
    budgetdata[i]["change"] = budgetdata[i]["amount"] - previous_amount
    prev_amount = budgetdata[i]["amount"]

# next step I will have to calculate the total amount, average and increases/decreases.
total_amount = sum(row['amount'] for row in budgetdata) 
total_change = sum(row['change'] for row in budgetdata)
average = round(total_change / (total_months-1), 2)
get_increase = max(budgetdata, key=lambda x:x['change'])
get_decrease = min(budgetdata, key=lambda x:x['change'])


# fnally I will print the stuff. make sure you add the ------ like in the results wanted
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})')
print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})')


# when I print the final results and export to text i need to set my path again cause its a different file 
csvlocation = os.path.join('.', 'Resources', 'PyBank_Results.txt')
with open(csvlocation, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_amount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)

