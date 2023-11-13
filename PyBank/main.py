import os
import csv

#path to the data file
pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# initalize the variables
total_months = 0
net_total = 0
change_tracker = 0
best_day = " "
best_gain = 0
worst_day = " "
worst_loss = 0
previous_month = 0
current_month = 0
change = 0.0


with open(pybank_csv, 'r') as csvfile:
    
    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    #skip header row
    header = next(csvreader)
    
    # loop through the data
    for row in csvreader:
        
        #convert profit and loss comlunm into an integer
        row[1] = int(row[1])
        #count total months
        total_months += 1
        
        #calculate net total 
        net_total += row[1]
        
        #calculate change from previous month,     
        if previous_month == 0:
            previous_month = row[1]
        elif row[1] > previous_month:
            change = row[1] - previous_month
            change_tracker += change
            previous_month = row[1]
            
            if change > best_gain:
                best_gain = change
                best_day = row[0]
        
        elif row[1] < previous_month:
            change = previous_month - row[1]
            change_tracker -= change
            previous_month = row[1]
            
            if change > worst_loss:
                worst_loss = change
                worst_day = row[0]
                
        

average_change = round(change_tracker / (total_months - 1), 2)


results= (f"Financial Analysis \n------------------------- \nTotal Months: {total_months} \nTotal: ${net_total} \nAverage Change: ${average_change} \nGreatest Increase in Profits: {best_day} (${best_gain}) \nGreatest Decrease in Profits: {worst_day} ($-{worst_loss})")
       
print(results)
    

with open('results.txt', 'w') as f:

  f.write(results)

      