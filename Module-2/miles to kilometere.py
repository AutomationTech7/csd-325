#Converting miles to kilometers.

def convert_to_kilometers():
    while True:
        try:
            number_of_miles = float(input("How many miles are you driving ?"))
            number_of_kilometers = number_of_miles * 1.60934
            print("You are driving",number_of_miles,"miles.")
            print("Which converts to", number_of_kilometers, "kilometers")
            break
        except ValueError:
            print("Only numbers can be used here. Please try again.")


convert_to_kilometers()

