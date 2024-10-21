'''
Munch App Start
by AGIndustries ( Akshobhya Gupta )

The purpose of this app is to plan your shopping list from your dinner menu for this week
'''

# -------   Imports  -----------

from random import choice

# -------  Functions  ----------
# 1)  Choose Dishes

def ChooseDishes(days):
    while len(YourMenu) < int(days):
        ChosenDish = choice(FoodYouLike)
        if ChosenDish not in YourMenu :
            YourMenu.append(ChosenDish)
    print("Phew! Here is your dinner Menu")
    print()
    print("Your Menu :- ")
    print()
    for dish in YourMenu:
        print(dish)
    print()
    print ("Out of all these my favourite has to be... " + choice(YourMenu) + " : )")

# 2)  Build Shopping List


def BuildShoppingList():
    YourShoppingList = []
    YourShoppingList.append(Essentials)
    if "Puri Bhaji" in YourMenu:
        YourShoppingList.append(PuriBhaji) 
    if "Veg Pizza" in YourMenu:
        YourShoppingList.append(VegPizza)
    if "Gulab Jamun" in YourMenu:
        YourShoppingList.append(GulabJamun)        
    if "Dal Rice" in YourMenu:
        YourShoppingList.append(DalRice)
    if "Paneer Roti" in YourMenu:
        YourShoppingList.append(PaneerRoti)
    if "Paneer Tikka" in YourMenu:
        YourShoppingList.append(PaneerTikka)
    if "Veg Frankie" in YourMenu:
        YourShoppingList.append(VegFrankie)
    for dish in YourShoppingList:
        for ingredient in dish:
            print(ingredient)
        


        
# -------  Lists  ---------
YourMenu = []
FoodYouLike = ["Puri Bhaji", "Gulab Jamun", "Dal Rice", "Paneer Roti", "Paneer Tikka", "Veg Frankie", "Veg Pizza"]
VegPizza = ["Pizza Bread", "Tomato Sauce", "Minced Cheese", "Toppings"]
PuriBhaji = ["Whole Wheat Flour", "Potatoes", "Curry Masala"]
GulabJamun = ["Gulab Jamun Mixture", "Oil", "Sugar Syrup", "Rose Essence"]
DalRice = ["Rice", "Pulses", "Turmeric Powder"]
PaneerRoti = ["Indian Cheese (Paneer)", "Whole Wheat Flour"]
PaneerTikka = ["Indian Cheese (Paneer)", "Tikka Masala"]
VegFrankie = ["Potatoes", "Vegetables of your choice", "Lettuce", "Corriander Sauce","Soya Sauce"]
Essentials = ["Onions", "Spices", "Salt", "Seasonings", "Garlic", "Chillies (for essence)", "Ginger"]


# 1) How Many Days To Plan

print("Hello !!! This is Munch, I will help you plan your Dinner Menu")
answer=input("How many days do you want me to plan ? (upto 7) ")
print("Ok! I am going to plan " + answer + " dinner(s) for you. ")



# 2) Choose Dishes

ChooseDishes(answer)
print()
answer=input("Would you like a Shopping List for this menu ? ")

if answer == 'yes':
    print("There you go....")
    print()
    print()
    BuildShoppingList()
    print()
    print("Happy journey to the grocery store !!!  : )")
    print("Hope to see you again soon !!!")
    print
 

#end the program

else:
    print()


#end the program


bie=input("Ok then, Hope you enjoyed.... Please visit again!!!  : ) ")

    

# 3) Build Shopping List

