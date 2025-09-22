import math
from rich.console import Console
from rich.panel import Panel
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero not possible."
    return x / y
def power(x,y):
    return x ** y
def sqrt(x):
    if x < 0:
        return "Error! Square root of negative number is not a real number."
    return x ** 0.5

console = Console()
console.print(Panel("[bold green]Welcome to the Enhanced Calculator![/bold green]", title="Calculator App", expand=False))
while True:
    console.print("[bold red]---------CALCULATOR MENU---------[/bold red]")
    console.print("[blue]Select operation:[/blue]")
    console.print("[blue]1. Add[/blue]")
    console.print("[blue]2. Subtract[/blue]")
    console.print("[blue]3. Multiply[/blue]")
    console.print("[blue]4. Divide[/blue]")
    console.print("[blue]5. Power[/blue]")
    console.print("[blue]6. Square Root[/blue]")
    console.print("[blue]7. Exit[/blue]")
    choice = input("Enter choice(1/2/3/4/5/6/7 or C(to clear)): ")
    if choice in ['1','2','3','4','5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1,num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1,num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1,num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1,num2)}")
    elif choice == '6':
        num = float(input("Enter number: "))
        print(f"√{num} = {sqrt(num)}")
    elif choice.upper() == 'C':
        result = None
        console.print("[bold]Calculator cleared.[/bold]")
        continue
    elif choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Please enter a valid choice.")