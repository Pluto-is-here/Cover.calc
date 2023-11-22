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

    print(conversion[to_unit] * from_unit, units[to_unit])


var_dist()