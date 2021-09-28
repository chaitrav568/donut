import requests

inputItem = input("Enter the Name of Item : ")
response = requests.get('https://opensource.adobe.com/Spry/data/json/donuts.js').text  # creating a response from http
apiText = eval(response)  # converting string (.txt) to dictionary
items = (apiText.get('items'))  # apiText["items"]
item = (items.get('item'))  # items["item"]
inputTopping = ""
isItemAvailable = False
isToppingAvailable = False
for x in item:
    if x.get('name').strip().lower() == inputItem.strip().lower():
        toppingType = x.get('topping')  # storing topping list in toppingType
        isItemAvailable = True
        inputTopping = input("Enter the Name of Toppings : ")
        for y in toppingType:
            if y.get('type').strip().lower() == inputTopping.strip().lower():
                isToppingAvailable = True
                print("This Topping is Available")

if not isItemAvailable:
    print(inputItem + " is Not Available")

if len(inputTopping) > 0 and isToppingAvailable is False:
    print(inputTopping + " is Not Available")
