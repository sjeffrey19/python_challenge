{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "0e2b6d3a-4b88-4c41-a3c5-86078eaea72a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578.00\n",
      "Average Change: 446309.05\n",
      "Greatest Increase in Profits: Aug-2013 $(999942)\n",
      "Greatest Decrease in Profits: Aug-2012 $(-1022534)\n"
     ]
    }
   ],
   "source": [
    "#load dependencies\n",
    "import pathlib\n",
    "import csv\n",
    "\n",
    "#read CSV file and skipping first line of headers\n",
    "csvpath = pathlib.Path('Resources/budget_data.csv')\n",
    "with open(csvpath) as csvfile:\n",
    "    budgetdata = csv.reader(csvfile, delimiter = ',')\n",
    "    budgetdata_header = next(budgetdata)\n",
    "    \n",
    "    #set lists/variables\n",
    "    months = []\n",
    "    aggregate_pfchanges = []\n",
    "  \n",
    "    #Loop through each row of budgetdata adding months to the month list and profits/losses to the aggregate list  \n",
    "    for row in budgetdata:\n",
    "        aggregate_pfchanges.append(row[1])\n",
    "        months.append(row[0])\n",
    "    \n",
    "    #Calculate the total number of months by getting the length of list\n",
    "    totalmonths = len(months)\n",
    "    \n",
    "    #Calculate the total net change\n",
    "    aggregate_pfchanges_int = map(int, list)\n",
    "    totalnet_change = sum(aggregate_pfchanges_int)\n",
    "    \n",
    "    #Calculate the average change/month\n",
    "    average_change = totalnet_change/totalmonths\n",
    "\n",
    "    #Calculate greatest increase in profits (date and amount) over the entire period\n",
    "    greatest_increase_amount = max(aggregate_pfchanges)\n",
    "    monthrow_max = aggregate_pfchanges.index(greatest_increase_amount)\n",
    "    greatest_increase_month = months[monthrow_max]\n",
    "    \n",
    "    #Calculate greatest decrease in profits (date and amount) over the entire period\n",
    "    greatest_decrease_amount = min(aggregate_pfchanges)\n",
    "    monthrow_min = aggregate_pfchanges.index(greatest_decrease_amount)\n",
    "    greatest_decrease_month = months[monthrow_min]\n",
    "    \n",
    "    #Print Financial Analysis Report     \n",
    "    print(f\"Financial Analysis\")\n",
    "    print(f\"----------------------------\")\n",
    "    print(f\"Total Months: {totalmonths}\")\n",
    "    print(f\"Total: ${totalnet_change:.2f}\")\n",
    "    print(f\"Average Change: {average_change:.2f}\")\n",
    "    print(f\"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_amount})\")\n",
    "    print(f\"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_amount})\")\n",
    "\n",
    "    #Save Report to .txt file\n",
    "    output_file = pathlib.Path('Analysis/report.txt')\n",
    "    \n",
    "    with open(output_file, \"w\") as report:\n",
    "    \n",
    "        title = (\"Financial Analysis\")\n",
    "        divider = (\"----------------------------\")\n",
    "        total_months = (f\"Total Months: {totalmonths}\")\n",
    "        totalnet_change = (f\"Total: ${totalnet_change:.2f}\")\n",
    "        average_change = (f\"Average Change: {average_change:.2f}\")\n",
    "        greatest_increase = (f\"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_amount})\")\n",
    "        greatest_decrease = (f\"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_amount})\")\n",
    "    \n",
    "        report.write('{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n'.format(title,divider,total_months,totalnet_change,average_change,greatest_increase,greatest_decrease))\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
