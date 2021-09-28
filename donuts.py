import requests
inputItem = input("Enter the Name of Item : ")
response = requests.get('https://opensource.adobe.com/Spry/data/json/donuts.js').text  #creating a response from http
apiText = eval(response)           # converting string .txt to dictionary
items = (apiText.get('items'))
item = (items.get('item'))
inputTopping = ""
isItemAvailable = False
isToppingAvailable = False
for x in item:
    if x.get('name').strip().lower() == inputItem.strip().lower():
        toppingType = x.get('topping')
        isItemAvailable = True
        inputTopping = input("Enter the Name of Toppings : ")

if isItemAvailable:
    isToppingAvailable = False
    for y in toppingType:
        if y.get('type').strip().lower() == inputTopping.strip().lower():
            print("This Topping is Available")
            isToppingAvailable = True

if not isItemAvailable:
    print(inputItem + " is Not Available")

if len(inputTopping) > 0 and isToppingAvailable == False:
    print(inputTopping + " is Not Available")