### Code to calculate the total cost of a holiday based on inputs from a user

# List of destinations
city_list = ['rome', 'paris', 'madrid', 'athens', 'vienna', 'copenhagen']

# Dictionary of flight costs for each destination
flight_cost = {'rome': 135,
               'paris': 110,
               'madrid': 120,
               'athens': 150,
               'vienna': 140,
               'copenhagen': 180
               }

# Define functions that are used to calculate costs
def hotel_cost(num_nights, hotel_per_night=125):
    return num_nights * hotel_per_night

def plane_cost(flight_cost):
    return flight_cost.get(city_list[city_flight])

def car_rental(rental_days, rental_per_day=70):
    return rental_days * rental_per_day

def holiday_cost():
    total_cost = hotel_cost(num_nights) + plane_cost(flight_cost) + car_rental(rental_days)
    return total_cost

# Data validation function that checks if the user input is an integer
def get_valid_integer():
    while True:
        user_input = input(f"{input_text}")
        try:
            user_integer = int(user_input)
            if user_integer >= 0:
                return user_integer
        except ValueError:
            print("Enter a valid number.")

# Display destination list in a user-friendly format
print("Please select a destination from the list below:")

for num in range(len(city_list)):
    print(f"{num + 1} - {city_list[num].capitalize()}")

# Data validation to ensure a valid destination option is selected
while True:
    try:
        city_flight = int(input("Please enter the number of your destination: "))
        if 1<= city_flight <= len(city_list):
            break
        else:
            print(f"Please enter a number between 1 and {len(city_list)}.")
    except ValueError:
        print("Please enter a valid number.")

# Print destination selected
city_flight -= 1
print(f"You selected: {city_list[city_flight].capitalize()}")

# Request user input for number of nights and check is an integer
input_text = "How many nights will you be staying? "
num_nights = get_valid_integer()

# Request user input for number rental car days and check is an integer
input_text = "How many days will you be hiring a rental car? "
rental_days = get_valid_integer()

## Output a breakdown of the holiday cost
print("\nHere is the breakdown of your holiday cost:")
print(f"£{plane_cost(flight_cost)}\tFlights")
print(f"£{hotel_cost(num_nights)}\tHotel")
print(f"£{car_rental(rental_days)}\tCar Rental")
print("----")
print(f"£{holiday_cost()}\tTOTAL COST\n")
