import os
import csv

summed_profit_list = 0
biggest_pl_increase = 0
biggest_pl_decrease = 0
biggest_pl_decrease_month = 0
biggest_pl_increase_month = 0
csv_path = os.path.join("Resources","budget_data.csv")
     
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    numofmonths = len(list(csvreader))
 
profit_delta_list = []
date_of_change = []
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    row = next(csvreader)
    last_month_profit = int(row[1])
    biggest_pl_increase = int(row[1])
    biggest_pl_increase_month = (row[0])
    summed_profit_list = summed_profit_list + int(row[1])

    for row in csvreader:
        #calc the total profit/loss
        summed_profit_list = summed_profit_list + int(row[1])
        #calc the difference from month to month
        profit_delta = int(row[1]) - last_month_profit
        profit_delta_list.append(profit_delta)
        last_month_profit = int(row[1])
        date_of_change.append(row[0])
        if int(row[1]) > biggest_pl_increase:
            biggest_pl_increase = int(row[1])
            biggest_pl_increase_month = row[0]
        if int(row[1]) < biggest_pl_decrease:
            biggest_pl_decrease = int(row[1])
            biggest_pl_decrease_month = (row[0])
   
    average_pl_change =str(round( sum(profit_delta_list)/(numofmonths - 1),2))

    highest_delta = max(profit_delta_list)
    lowest_delta = min(profit_delta_list)

    print("Total Months: " + str(numofmonths))    
    print("Total: $" + str(summed_profit_list))
    print("Average Change: " + "$" + str(average_pl_change))
    print("Greatest Increase in Profits:" + " " + str(biggest_pl_increase_month) + " " + "("+"$" + str(highest_delta)+ ")")
    print("Greatest Decrease in Profits:" + " " + str(biggest_pl_decrease_month) + " " + "("+"$" + str(lowest_delta)+ ")")

    analysis_out = open("Analysis/pybankanalysis.txt", "w")
    analysis_out.write("Total Months:" + str(numofmonths))
    analysis_out.write("\n")    
    analysis_out.write("Total: $" + str(summed_profit_list))
    analysis_out.write("\n")  
    analysis_out.write("Average Change:" + str(average_pl_change))
    analysis_out.write("\n")  
    analysis_out.write("Greatest Increase in Profits:" + " " + str(biggest_pl_increase_month) + " " + "("+"$" + str(highest_delta)+ ")")
    analysis_out.write("\n")  
    analysis_out.write("Greatest Decrease in Profits:" + " " + str(biggest_pl_decrease_month) + " " + "("+"$" + str(lowest_delta)+ ")")

