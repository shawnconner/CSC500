# Part 1:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for
#     the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month.
#     Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should
#     display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

total_rainfall = 0

num_years = int(input("Enter the number of years: "))
total_months = num_years*12

for i in range(num_years):
    for j in range(0, 12):
        rainfall = int(input(f"Enter rain fall for year {i + 1} and month {j + 1} in inches: "))
        total_rainfall += rainfall

print("Total months: ", total_months)
print("Total rainfall in inches: ", total_rainfall)
print("Average rainfall: ", total_rainfall/(total_months))
