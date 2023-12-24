#editedfilehere
T = {}
#Creating the item code in loop
a=10000
c=0

while True:
    choice= int(input(" 1 for administration, 2 for billing, 3 to close store:"))
    if choice == 1:
        while True:
            a = int(input(" 1 to add stocks,2 to display and 3 to exit administration:"))
            if a==1:
                Itms= input("Enter the item")
                qunty= int(input("Enter the quantity of te item:"))
                amt= int(input("Enter the price of  a single item:"))
                total= qunty*amt
                if Itms not in T:
                    itmcode=a
                    a+=c
                    c+=1
                print("Itemcode:",itmcode)
                T[itmcode]= {"Name":Itms,"Quantity":qunty}
                 
            if a == 2:
                f= int(input("Enter 1 to see a particular item otherwise press any other number:"))
                if f== 1:
                    itm = int(input("Enter the itemcode:")
                if itm in T:
                    print(T[itm])
                elif a != 1:
                    print(T)
            if a ==3:
                print("Exiting administration:")
                break
        

    if choice == 2:
