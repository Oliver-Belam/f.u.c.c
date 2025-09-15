import json, os

SAVE_FILE = "spendings.json"
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r") as f:
        freaks_moneys = json.load(f)
else:
    freaks_moneys = [0,0,0,0] # Oliver, Jacob, Jayce, Eddie

names = ["Oliver", "Jacob", "Jayce", "Eddie"]
updated = True

# Saves the spendings to a json file
def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump(freaks_moneys, f)

# Updates the spendings of the selected freak
def update_spendings(freak, money):
    global updated
    freaks_moneys[freak] += money
    save_data()
    updated = False


# Balances the freak moneys
def balance_spendings():
    global updated
    for n in range(0,3):
        if freaks_moneys[n] != 0:
            highest = max(freaks_moneys)
            freaks_moneys[0] = highest - freaks_moneys[0]
            freaks_moneys[1] = highest - freaks_moneys[1]
            freaks_moneys[2] = highest - freaks_moneys[2]
            freaks_moneys[3] = highest - freaks_moneys[3]
    updated = True

    return freaks_moneys

# Settles all debts
def settle_spendings():
    total = sum(freaks_moneys)
    average = total / len(freaks_moneys)
    return [round(average - spent, 2) for spent in freaks_moneys]

# Displays freak spendings
def display_spendings():
    print(freaks_moneys, "Updated:", updated)

# Reset spendings
def reset_spendings():
    freaks_moneys = [0,0,0,0]
    save_data()
    updated = True


reset_spendings()
display_spendings()
