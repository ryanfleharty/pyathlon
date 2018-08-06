my_dictionary = {
    "best_movie": "Aguirre, the Wrath of God",
    "best_number": 42,
    "best_running_back": {
        "name": "Le'Veonn Bell",
        "team": "Pittsburgh Steelers"
    },
    "top_five_foods": ["steak","cheeseburgers","ribs","steak","chicken nuggets"]
}

for mystery in my_dictionary:
    print(mystery)

# you can use my_dictionary.values() to loop over the values
# my_dictionary.items() will give you a tuple you can unpack like so:
# for key, value in my_dictionary.items() 