print("Amount of your money: ")
Amount = float(input())
print("Price of an apple: ")
Price = float(input())
Quantity = Amount//Price
Change = Amount-Quantity*Price
print(f"You can buy {Quantity} apples and your change is {Change} pesos.")