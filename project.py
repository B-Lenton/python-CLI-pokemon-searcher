# a pokemon character finder using pokeapi.co:
from datetime import datetime
import requests

while True:
# take user input, convert to lowercase, check it's only letters, give 'quit' option
    user_choice = input("(type 'quit' to quit) Enter your Pokemon of choice: ")
    user_choice = user_choice.lower()
    
    if not user_choice.isalpha():
        print("invalid input")
        quit()
    elif user_choice.lower() == "quit":
        print("goodbye")
        quit()
    else:
        pass

    # put user input into api url, request the data, convert to python dictionary, display search choice
    dynamic_url = f"https://pokeapi.co/api/v2/pokemon/{user_choice}"

    search = requests.get(dynamic_url)
    if search.status_code == 200:
        data = search.json()

        print("You have searched for", data["name"].capitalize())

        # loop through each item in the 'moves' list from the data dictionary & display every move's name
        print("Moves:\t")
        for move in data["moves"]:
            print(move["move"]["name"])

        # create list of options, loop through them to display as list
        stat_list = ["abilities", "base experience", "forms", "height", "held items", "moves", "species", "stats"]

        print("Choose from the list below:")
        for index, stat in enumerate(stat_list):
            print(index +1, stat)

        # take user choice of stat numbers and reformat
        choose_stats = input("Enter the numbers of the stats you wish to see (e.g. 1, 3, 7) ")
        choose_stats = choose_stats.replace(",", "")
        choose_stats = choose_stats.replace(" ", "")

        # if there are only numbers in the string, convert it to a list
        if choose_stats.isnumeric():
            # convert to list and remove duplicates
            choose_stats = list(dict.fromkeys(choose_stats))
            # loop through each user choice
            for stat in choose_stats:
                # convert to number and minus one (base indexing), put new number into stat list 
                choice = stat_list[(int(stat) -1)]
                # format choice (no spaces) then put the result into the search request from earlier
                choice = choice.replace(" ", "_")
                result = data[choice]
                # print results
                print(choice.capitalize(), ":", result)
                # write results to file for record
                with open("record.txt", "a") as file:
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    try:
                        file.write(f"{current_time}: {user_choice}, {choice, result}\n\n")
                    except:
                        file.write(f"{current_time}: unsuccessful search\n\n")
        else:
            print("invalid entry")

    else:
        print("Pokemon not found")

