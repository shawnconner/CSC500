# Part 2:
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:
#
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.

books = int(input("Enter the number of books purchased this month: "))

if books < 2:
    print("You have earned 0 points")
elif books >= 2 and books < 4:
    print("You have earned 5 points")
elif books >= 4 and books < 6:
    print("You have earned 15 points")
elif books >= 6 and books < 8:
    print("You have earned 30 points")
elif books >= 8:
    print("You have earned 60 points")
else:
    print("Invalid number of books")