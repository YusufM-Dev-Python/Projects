# Define a function to perform addition of two numbers
def add(a, b):
    return a + b


# Define a function to perform subtraction of two numbers
def subtract(a, b):
    return a - b


# Define a function to perform multiplication of two numbers
def multiply(a, b):
    return a * b


# Define a function to perform division, including error handling for division by zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Define the main calculator function to handle user interaction and control flow
def calculator():
    print("--- Algorithmic Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Start a continuous loop to keep the calculator running until the user decides to quit
    while True:
        # Prompt the user to select an option or quit, and remove any trailing/leading whitespace
        choice = input(
            "\nEnter choice (1/2/3/4) or type 'q' to quit: "
        ).strip()

        # Check if the user wants to exit the application
        if choice.lower() == "q":
            print("Exiting calculator. Goodbye!")
            break

        # Validate that the user entered a valid menu option
        if choice in ("1", "2", "3", "4"):
            try:
                # Prompt the user for numerical inputs and cast them to floats to handle decimals
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Catch invalid non-numeric inputs and prompt the user again without crashing
                print(
                    "Invalid input. Please enter valid numerical values."
                )
                continue

            # Execute the corresponding arithmetic operation based on user choice
            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            # Handle out-of-range choices
            print("Invalid Choice. Please select a valid option from 1 to 4.")


# Ensure the calculator function runs only when the script is executed directly
if __name__ == "__main__":
    calculator()