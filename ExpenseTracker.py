Expenses = []


def add_expenses():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    Expenses.append([category, amount])
    print("Expenses added successfully!")


def display_expenses():
    if len(Expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\n--- All Expenses ---")

        for expense in Expenses:
            print("Category:", expense[0], "Amount:", expense[1])


def total_expenses():
    total = 0

    for expense in Expenses:
        total = total + expense[1]

    print("Total Expenses:", total)


def highest_expenses():
    if len(Expenses) == 0:
        print("No expenses recorded.")
    else:
        highest = Expenses[0][1]

        for expense in Expenses:
            if expense[1] > highest:
                highest = expense[1]

        print("Highest Expense:", highest)


def lowest_expenses():
    if len(Expenses) == 0:
        print("No expenses recorded.")
    else:
        lowest = Expenses[0][1]

        for expense in Expenses:
            if expense[1] < lowest:
                lowest = expense[1]

        print("Lowest Expense:", lowest)


def category_total():
    if len(Expenses) == 0:
        print("No expenses recorded.")
    else:
        categories = []

        for expense in Expenses:
            if expense[0] not in categories:
                categories.append(expense[0])

        print("\n--- Category-wise Total ---")

        for category in categories:
            total = 0

            for expense in Expenses:
                if expense[0] == category:
                    total = total + expense[1]

            print(category, ": ₹", total)


def search_expense():
    search = input("Enter category to search: ")

    found = False

    for expense in Expenses:
        if expense[0] == search:
            print("Category:", expense[0], "Amount: ₹", expense[1])
            found = True

    if found == False:
        print("No expense found in this category.")


while True:

    print("\n==== STUDENT EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Total Expense")
    print("4. Highest Expense")
    print("5. Lowest Expense")
    print("6. Category-wise Total")
    print("7. Search Expense")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expenses()

    elif choice == 2:
        display_expenses()

    elif choice == 3:
        total_expenses()

    elif choice == 4:
        highest_expenses()

    elif choice == 5:
        lowest_expenses()

    elif choice == 6:
        category_total()

    elif choice == 7:
        search_expense()

    elif choice == 8:
        print("Thank you for using Student Expense Tracker!")
        break

    else:
        print("Invalid choice.")