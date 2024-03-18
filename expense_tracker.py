from expense import Expense
import datetime


def main():
    print(f"📝Running expense Tracker\n")
    expense_file_path = "expense.csv"
    budget = 6000
    # Get user input for expense
    #expense = get_user_expense()
    
    # Write their expense in a file
    #save_expenses(expense, expense_file_path)

    # Read file and summarize
    summarize_expense(expense_file_path,budget)
def remaining_days_in_month():
    # Get today's date
    today = datetime.date.today()
    # Get the first day of the next month
    first_day_of_next_month = today.replace(day=1, month=today.month + 1)
    # Calculate the last day of the current month
    last_day_of_current_month = first_day_of_next_month - datetime.timedelta(days=1)
    # Calculate the remaining days in the month
    remaining_days = (last_day_of_current_month - today).days
    return remaining_days

def get_user_expense():
    print(f"👉getting user expense\n ")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount "))
    print("You have entered ", expense_name, expense_amount)

    expense_cat = ["🍽️Food", "🧳Travel", "🏠Rent", "📝Bills", "🏥Hospital"]

    while True:
        print("Select category: ")
        for i, category_name in enumerate(expense_cat):
            print(f"{i+1}.{category_name}")

        value_range = f"[1-{len(expense_cat)}]"

        try:
            select_index = int(input(f"Enter a category number {value_range}: ")) - 1
        except ValueError:
            print("Invalid choice")
            continue

        if select_index in range(len(expense_cat)):
            selected_category = expense_cat[select_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid choice")
def colorize(text, color):
    """
    Colorize the text with the specified color.

    Parameters:
    text (str): The text to be colorized.
    color (str): The color to apply. This should be one of 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', or 'white'.

    Returns:
    str: The colorized text with ANSI escape codes.
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m'
    }
    reset = '\033[0m'

    # Check if the color is valid
    if color not in colors:
        raise ValueError("Invalid color. Choose one of: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'")

    # Return the colorized text
    return colors[color] + text + reset

def save_expenses(expense: Expense, expense_file_path):
    print(f"🗃️saving user expense:{expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path, budget):
    print(f"📂getting user expense from {expense_file_path}")
    expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")

            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expense by category")
    for key, amount in amount_by_category.items():
        print(" {}: ${:.2f}".format(key, amount))
    
    total_sum=sum([x.amount for x in expenses])
    print("You have spent",total_sum,"this month")

    remaning_budget= budget-total_sum
    print("budget Remaining",remaning_budget,"this month")
 

    # Test the function
    remaining_days = remaining_days_in_month()
    print(remaining_days)
    Daily_aloowance = f"You can spend {remaning_budget//remaining_days} everyday"

    colored_text = colorize(Daily_aloowance, 'green')
    print(colored_text)
if __name__ == "__main__":
    main()
