# Import math module
import math

### Example of validation function
def get_valid_number():
    while True:
        user_input = input("Enter a number: ")
        try:
            user_float = float(user_input)
            if user_float > 0:
                return user_float
        except ValueError:
            print("Enter a valid number greater than 0")

### Call function and assign output to variable e.g.
interest_rate = get_valid_number()

# Display options for user and ask them to select one
print("investment\t - to calculate the amount of interest you'll earn on your investment")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan\n")
choose_program = input("Enter either 'investment' or 'bond' from " ### Move into the loop
                       "the menu above to proceed: ").lower()

while True:

# Start of investment option

    if choose_program == "investment":

        while True: # Begin data validation for investment amount
            investment_amount = input("Please enter the total amount deposited: ")
            try:
                investment_amount = float(investment_amount)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
            if investment_amount <= 0:
                print("\nPlease enter a number greater than 0.")
                continue
            break # End validation for investment amount

        while True: # Begin data validation for investment rate
            investment_rate = input("Please enter the interest rate: ")
            try:
                investment_rate = float(investment_rate)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
            if investment_rate <= 0:
                print("\nPlease enter a number greater than 0.")
                continue
            break # End validation for investment rate

        while True: # Begin data validation for investment years
            investment_years = input("Please enter the number of years to invest: ")
            try:
                investment_years = float(investment_years)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
            if investment_years <= 0:
                print("\nPlease enter a number greater than 0.")
                continue
            break # End validation for investment years

        while True: # Begin data validation for interest type
            interest = input("Please enter 'Simple' or 'Compound' interest: ").lower()

            # Calculate simple investment interest ### Inefficient, move the calculations into the if statements 
            interest_simple = round(investment_amount *
                                (1 + (investment_rate / 100) * investment_years), 2)

            # Calculate compound investment interest
            interest_compound = round(investment_amount *
                                  math.pow((1 + (investment_rate / 100)),investment_years), 2)

            if interest == "simple":
                print(f"At the end of the period, your investment will be worth {interest_simple}")
                break

            elif interest == "compound":
                print(f"At the end of the period, your investment will be worth {interest_compound}")
                break

            else:
                print("\nInvalid input.")
                continue

        break # End data validation for interest type

# End of investment option/Start of bond option

    elif choose_program == "bond":

        while True: # Begin data validation for bond value
            bond_value = input("Please enter the present value of the house: ")
            try:
                bond_value = float(bond_value)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
            if bond_value <= 0:
                print("\nPlease enter a number greater than 0.")
                continue
            break # End validation for bond value

        while True: # Begin data validation for bond rate
            bond_rate = input("Please enter the interest rate: ")
            try:
                bond_rate = float(bond_rate)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
            if bond_rate <= 0:
                print("\nPlease enter a number greater than 0.")
                continue
            break # End validation for bond rate

        while True: # Begin data validation for bond months
            bond_months = input("Please enter the number of months to repay the bond: ")
            try:
                bond_months = float(bond_months)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
            if bond_months <= 0:
                print("\nPlease enter a number greater than 0.")
                continue
            break # End validation for bond months

        # Calculate bond repayment per month
        bond_repayment = round(((bond_rate / 100 / 12) * bond_value) /
                               (1 - (1 + (bond_rate / 100 / 12)) ** (-bond_months)), 2)

        print(f"The monthly repayment will be {bond_repayment}")

        break

# End of bond option

    else: # if an invalid program is entered then repeat the question
        print("\nInvalid input.")
        choose_program = input("Enter either 'investment' or 'bond' from " ### This is repeated 
                               "the menu above to proceed: ").lower()
