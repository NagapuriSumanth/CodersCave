class User:
    def __init__(self, name,):
        self.name = name
        self.balance = 0
    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"


class Expense:
    def __init__(self, purpose, money, participants):
        self.purpose = purpose
        self.money = money
        self.participants = participants

    def __str__(self):
        return f"{self.purpose}: ${self.money:.2f}"


def add_expense(expenses, purpose, money, participants):
    expense = Expense(purpose, money, participants)
    expenses.append(expense)
    per_person_share = money / len(participants)
    for participant in participants:
        participant.balance += per_person_share


def calculate_balances(users, expenses):
    for expense in expenses:
        per_person_share = expense.money / len(expense.participants)
        for participant in expense.participants:
            participant.balance -= per_person_share


def display_balances(users):
    for user in users:
        print(user)


def main():
    users = [User("ramesh"), User("kiran"), User("suresh")]
    expenses = []

    while True:
        print("\n1. Add Expense\n2. Calculate Balances\n3. Display Balances\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            purpose = input("Enter expense purpose: ")
            money = float(input("Enter expense money:"))
            participants = input("Enter participants (comma-separated): ").split(",")
            participants = [user for user in users if user.name in participants]
            add_expense(expenses, purpose, money, participants)
            print("Expense added successfully!")


        elif choice == "3":
            display_balances(users)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
