# import Modules
import os
import csv
# placeholders for month, profit/loss, and profit/loss change
date = []
profit = []
change = []

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis","financial_analysis.txt")
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Loop through each row, grab each field and store in a new list
    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))
    
    # Loop though each element in list profit, and calculate the change and store it in list change
    for i in range(len(profit)-1):
        n = float(profit[i+1])-float(profit[i])
        change.append(n)

    total_month = len(date)
    total_profit = sum(profit)
    avg_change = sum(change)/len(change)
    increase_max = max(change)
    decrease_max = min(change)

    date1 = date[int(change.index(increase_max))+1]
    date2 = date[int(change.index(decrease_max))+1]

# Generate Output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Month: {total_month}\n"
    f"Total Profit/Loss: ${total_profit:,.0f}\n"
    f"Average Change: ${avg_change:,.2f}\n"
    f"Greatest Increase in Profits: {date1} ( ${increase_max:,.0f})\n"
    f"Greatest Increase in Profits: {date2} ( ${decrease_max:,.0f})")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)