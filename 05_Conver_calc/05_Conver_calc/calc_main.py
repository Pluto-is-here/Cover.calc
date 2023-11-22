

def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def num_check(question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) {}".format(low)

        try:
            # asks user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("This calculator will let you convert between any two related units (eg, mm, cm, m, km)")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    statement_generator('Note: When choosing unit, please enter the corresponding number.','*')
    print()
    statement_generator('-', '-')
    return ""


def user_choice():

    valid = False

    while not valid:

        response = input("Hello! would you like to convert distance, time, or weight? ").lower()
        dist_ok = ["dist", "distance", "d", "1"]
        time_ok = ["time", "t", "2"]
        weight_ok = ["weight", "w", "3"]
        if response in dist_ok:
            return "distance"

        elif response in time_ok:
            return "time"

        elif response in weight_ok:
            return "weight"

        else:
            # if response is not valid, out put error
            print("Please choose a valid measurement type!")
            print()


def var_dist():

    units = {'1': 'mm',
             '2': 'cm',
             '3': 'm',
             '4': 'km'
            }
    conversion = {'1': 0.001,
                  '2': 0.01,
                  '3': 1,
                  '4': 1000}

    user_input = ''

    # print list

    for unit_key in units:
        print(unit_key + ". " + units[unit_key])

    # choose a unit one

    user_input = input('Your choice: ')

    while user_input.lower() not in units.keys():
        user_input = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[user_input])

    input_num = int(input('How many? '))

    # convert to m

    from_unit = (conversion[user_input] * input_num)

    to_unit = input('Choose a value to convert to: ')

    while to_unit.lower() not in units.keys():
        to_unit = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[to_unit])

    print("{} {} to {} = ".format(input_num, units[user_input], units[to_unit]))

    answer_num = conversion[to_unit] * from_unit

    print('{:.1f} {}'.format(answer_num, units[to_unit]))


def var_time():

    units = {'1': 'seconds',
             '2': 'minutes',
             '3': 'hours',
             '4': 'days'
            }
    conversion = {'1': 0.000277778,
                  '2': 0.0166667,
                  '3': 1,
                  '4': 24}

    user_input = ''

    # print list

    for unit_key in units:
        print(unit_key + ". " + units[unit_key])

    # choose a unit one

    user_input = input('Your choice: ')

    while user_input.lower() not in units.keys():
        user_input = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[user_input])

    input_num = int(input('How many? '))

    # convert to m

    from_unit = (conversion[user_input] * input_num)

    to_unit = input('Choose a value to convert to: ')

    while to_unit.lower() not in units.keys():
        to_unit = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[to_unit])

    print("{} {} to {} = ".format(input_num, units[user_input], units[to_unit]))

    answer_num = conversion[to_unit] * from_unit

    print('{:.1f} {}'.format(answer_num, units[to_unit]))

def var_weight():

    units = {'1': 'gram',
             '2': 'kilogram',
            }
    conversion = {'1': 0.001,
                  '2': 1,
                  }

    user_input = ''

    # print list

    for unit_key in units:
        print(unit_key + ". " + units[unit_key])

    # choose a unit one

    user_input = input('Your choice: ')

    while user_input.lower() not in units.keys():
        user_input = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[user_input])

    input_num = int(input('How many? '))

    # convert to m

    from_unit = (conversion[user_input] * input_num)

    to_unit = input('Choose a value to convert to: ')

    while to_unit.lower() not in units.keys():
        to_unit = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[to_unit])

    print("{} {} to {} = ".format(input_num, units[user_input], units[to_unit]))

    answer_num = conversion[to_unit] * from_unit

    print('{:.1f} {}'.format(answer_num, units[to_unit]))





# main routine

statement_generator('Welcome to the conversion calculator!', '*')


first_time = input("To display instructions, press <enter>, or press any key to continue")

if first_time == "":
    instructions()

keep_going = ""

while keep_going == "":

    measurement_type = user_choice()
    print("You chose", measurement_type)

    if measurement_type == "distance":
        var_dist()

    if measurement_type == "time":
        var_time()

    if measurement_type == "weight":
        var_weight()

    print()
    keep_going = input("Press <enter> to keep going or any key to quit")
    print()

print()
print("Thanks for using the conversion calculator")









