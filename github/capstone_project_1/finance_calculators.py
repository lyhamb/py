# Import math module
import math

# Data validation function
def get_valid_number():
    while True:
        user_input = input(f"Please enter the {input_text}")
        try:
            user_float = float(user_input)
            if user_float > 0:
                return user_float
            elif user_float <= 0:
                print ("Enter a number greater than 0.")
        except ValueError:
            print("Enter a valid number.")


# Display options for user and ask them to select one
print("investment\t - to calculate the amount of interest you'll earn on your investment")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan\n")
choose_program = input("Enter either 'investment' or 'bond' from "
                       "the menu above to proceed: ").lower()

while True:

# Start of investment option

    if choose_program == "investment":

        input_text = "total amount deposited: "
        investment_amount = get_valid_number()

        input_text = "interest rate: "
        investment_rate = get_valid_number()

        input_text = "number of years to invest: "
        investment_years = get_valid_number()

        while True: # Begin data validation for interest type

            interest = input("Please enter 'Simple' or 'Compound' interest: ").lower()

            if interest == "simple":
                # Calculate simple investment interest
                interest_simple = round(investment_amount *
                                (1 + (investment_rate / 100) * investment_years), 2)
                print(f"At the end of the period, your investment will be worth {interest_simple}")
                break

            elif interest == "compound":
                # Calculate compound investment interest
                interest_compound = round(investment_amount *
                                  math.pow((1 + (investment_rate / 100)),investment_years), 2)
                print(f"At the end of the period, your investment will be worth {interest_compound}")
                break

            else:
                print("Invalid input.")
                continue

        break # End data validation for interest type

# End of investment option/Start of bond option

    elif choose_program == "bond":

        input_text = "present value of the house: "
        bond_value = get_valid_number()

        input_text = "interest rate: "
        bond_rate = get_valid_number()

        input_text = "number of months to repay the bond: "
        bond_months = get_valid_number()

        # Calculate bond repayment per month
        bond_repayment = round(((bond_rate / 100 / 12) * bond_value) /
                               (1 - (1 + (bond_rate / 100 / 12)) ** (-bond_months)), 2)

        print(f"The monthly repayment will be {bond_repayment}")

        break

# End of bond option

    else: # if an invalid program is entered then repeat the question
        print("Invalid input.")
        choose_program = input("Enter either 'investment' or 'bond' from "
                               "the menu above to proceed: ").lower()
   
