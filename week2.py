expenses = []


def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Expense must be greater than 0.\n")
            return

        expenses.append(amount)
        print("Expense added successfully.\n")

    except ValueError:
        print("Invalid amount entered.\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n------ Expense History ------")

    for index, amount in enumerate(expenses, start=1):
        print(f"{index}. ₹{amount}")

    print()


def calculate_total():
    total = sum(expenses)

    print(f"\nTotal Spent: ₹{total:.2f}\n")


def calculate_average():
    if not expenses:
        print("No expenses available.\n")
        return

    average = sum(expenses) / len(expenses)

    print(f"\nAverage Expense: ₹{average:.2f}\n")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: "))

        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            print(f"Removed expense ₹{removed}\n")
        else:
            print("Invalid expense number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. View Average Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Thank you for using Expense Tracker.")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()