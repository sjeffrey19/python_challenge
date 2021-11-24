#load dependencies
import pathlib
import csv

#read CSV file and skipping first line of headers
csvpath = pathlib.Path('Resources/budget_data.csv')
with open(csvpath) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter = ',')
    budgetdata_header = next(budgetdata)
    
    #set lists/variables
    months = []
    aggregate_pfchanges = []
    
    #Loop through each row of budgetdata adding months to the month list and profits/losses to the aggregate list
    for row in budgetdata:
        aggregate_pfchanges.append(row[1])
        months.append(row[0])
    
    #Calculate the total number of months by getting the length of list\n",
    totalmonths = len(months)
    
    #Calculate the total net change
    aggregate_pfchanges_int = map(int, aggregate_pfchanges)
    totalnet_change = sum(aggregate_pfchanges_int)
    
    #Calculate the average change/month
    average_change = totalnet_change/totalmonths

    #Calculate greatest increase in profits (date and amount) over the entire period
    greatest_increase_amount = max(aggregate_pfchanges)
    monthrow_max = aggregate_pfchanges.index(greatest_increase_amount)
    greatest_increase_month = months[monthrow_max]
    
    #Calculate greatest decrease in profits (date and amount) over the entire period
    greatest_decrease_amount = min(aggregate_pfchanges)
    monthrow_min = aggregate_pfchanges.index(greatest_decrease_amount)
    greatest_decrease_month = months[monthrow_min]
    
    #Print Financial Analysis Report
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${totalnet_change:.2f}")
    print(f"Average Change: {average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_amount})")

    #Save Report to .txt file
    output_file = pathlib.Path('Analysis/report.txt')

    with open(output_file, "w") as report:

        title = ("Financial Analysis")
        divider = ("----------------------------")
        total_months = (f"Total Months: {totalmonths}")
        totalnet_change = (f"Total: ${totalnet_change:.2f}")
        average_change = (f"Average Change: {average_change:.2f}")
        greatest_increase = (f"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_amount})")
        greatest_decrease = (f"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_amount})")

        report.write('{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n'.format(title,divider,total_months,totalnet_change,average_change,greatest_increase,greatest_decrease))