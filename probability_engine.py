import yaml
import random

def first_roll_check(roll): 
    if roll > 80: 
        return "uneventful"
    elif roll > 35:
        return "possible"
    elif roll > 10:
        return "unlikely"
    elif roll > 0: 
        return "rare"
    else:
       return "First roll error"

first_roll = random.randint(1, 100)
event_type = first_roll_check(first_roll)

with open("events.yaml", "r") as f:
    data = yaml.safe_load(f)

options = data["events"]

categories = {
    20: "possible",
    10: "unlikely",
    5: "rare"
}

sorted_options = {
    "possible": [],
    "unlikely": [],
    "rare": []
}

for opt in options:
    prob = opt["probability"]
    if prob in categories:
        category = categories[prob]
        sorted_options[category].append(opt)

print("First roll:", first_roll)
print("Event type:", event_type)

if event_type == "uneventful":
    print("Nothing eventful happened.")
else: 
    descriptions = [opt["description"] for opt in sorted_options[event_type]]
    choice = random.choices(descriptions, k=1)[0]
    print("Number of ", event_type, "events:", len(sorted_options[event_type]))
    print("Event chosen:", choice)





# Rather than doing a roll system, I could impliment a choice statically? With probabilities as allowed in random.library

# The k=1 and array selection are unnecessary, but educational

# The alt code for the dictionary is sorted_options = {cat: [] for cat in categories.values()}

"""
Just thinking out loud here. I need to create a way to store the options into three different categories. I could use an if
loop, where I say if probability is Unlikely but that doesn't seem like the right way to do this. The problem with amazing
solutions is that because i didn't enginner them I remember them less though... Ok, there is indeed an if way to do this. I'm 
gonna write it out for training purposes.

possible = []
unlikely = []
rare = []

for opt in options:
    if opt["probability"] == 20:
        possible.append(opt)
    elif opt["probability"] == 10:
        unlikely.append(opt)
    elif opt["probability"] == 5:
        rare.append(opt)
"""
