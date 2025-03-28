costprice = int(input("Enter the cost price: "))
sellingprice = int(input("Enter the selling price: "))

if(sellingprice > costprice):
    print("profit")
    profit = sellingprice - costprice
    print("profit is", profit)
else:
    print("No Profit")
    