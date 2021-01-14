import csv

f = open("analysis/bank_analysis.txt" , "w")

with open('Resources/budget_data.csv') as csvFile:

    next(csvFile)
    csvRead = csv.reader(csvFile)
    months = 0
    total = 0
    change = 0
    prev_revenue = 0
    avg_ch = 0
    greatest_Increase = 0
    greatest_Decrease = 0
    greatest_Increase_cur = 0
    greatest_Decrease_cur = 0

    for i, row in enumerate(csvRead):
        months += 1
        rev = int(row[1])
        total += rev

        if i == 0:
            prev_revenue = rev
            greatest_Increase = rev
            greatest_Decrease = rev

        if prev_revenue < 0:
            currentChange = abs(prev_revenue) + rev
        else:
            currentChange = rev - prev_revenue

         
        if currentChange > greatest_Increase:
            greatest_Increase = currentChange
            greatest_Inc_Date = row[0]   

        if currentChange < greatest_Decrease:
            greatest_Decrease = currentChange
            greatest_Dec_Date = row[0]
            
        
        change = rev - prev_revenue
        avg_ch += change
        prev_revenue = rev

        
        

output = (
    f'\n  Financial Analysis\n\
  ----------------------------\n\
  Total Months: {months}\n\
  Total: ${total:,}\n\
  Average  Change: ${avg_ch/(months-1):,.2f}\n\
  Greatest Increase in Profits: {greatest_Inc_Date} ${greatest_Increase}\n\
  Greatest Decrease in Profits: {greatest_Dec_Date} ${greatest_Decrease}'
)

print(output)

f.write(output)