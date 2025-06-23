def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)  # Convert to monthly and percentage
    months = years * 12

    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / (((1 + monthly_rate) ** months) - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    return emi, total_payment, total_interest, months

def print_schedule(principal, emi, monthly_rate, months):
    balance = principal
    print("\n Payment Schedule:")
    print("-" * 50)
    print(f"{'Month':<6} {'EMI':<10} {'Interest':<10} {'Principal':<10} {'Balance':<10}")
    print("-" * 50)

    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal_payment = emi - interest
        balance -= principal_payment
        print(f"{month:<6} {emi:<10.2f} {interest:<10.2f} {principal_payment:<10.2f} {balance:<10.2f}")
        if balance < 0:
            break

def main():
    print(" Loan EMI Calculator")
    print("-" * 30)

    try:
        principal = float(input("Enter loan amount (₹): "))
        rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter loan duration (years): "))

        emi, total_payment, total_interest, months = calculate_emi(principal, rate, years)

        print("\n EMI Calculation Results")
        print("-" * 30)
        print(f"Monthly EMI: ₹{emi:.2f}")
        print(f"Total Payment: ₹{total_payment:.2f}")
        print(f"Total Interest: ₹{total_interest:.2f}")

        show_schedule = input("\nShow monthly payment schedule? (y/n): ").lower()
        if show_schedule == 'y':
            monthly_rate = rate / (12 * 100)
            print_schedule(principal, emi, monthly_rate, months)

    except ValueError:
        print(" Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
