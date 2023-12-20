T = {}
bdgt= int(input("enter the budget of the store(NUMERIC INPUT):"))
bdgt1=bdgt
while True:
    a = int(input(" 1 to add items, 2 to re purchase , 3 to sell,4 to delete, 5 to display and 6 to exit:"))
    if a == 1:
        itm = input("Enter the item")
        qunty= int(input("Enter the quantity of te item:"))
        amt= int(input("Enter the price of  a single item:"))
        b = qunty*amt
        bdgt1-=b
        print ("Amount left in the store =", bdgt1)
        T[itm]= {"quanity":qunty,"amount" : b}
        c= qunty
        f= b
        print("Item purchased")
    if a == 2:
        itm = input("Enter the itm")
        if itm in T:
            qunty= int(input("Enter the quantity of the item:"))
            amt= int(input("Enter the price of  a single item:"))
            b = qunty*amt
            bdgt1-=b
            print ("Amount left in the store == ", bdgt1)
            c+= qunty
            f-=b
            T[itm]= {"quanity":c,"amount" : f}
            print("Item purchased")
        else:
            print("Item not found")
    if a == 3:
        itm = input("Enter the itm")
        if itm in T:
            qunty = int(input("Enter the quantity of the item:"))
            amt = int(input("Enter the  sell price of  a single ietm:"))
            b = qunty*amt
            bdgt1+=b
            print ("Amount left in the store == ", bdgt1)
            c-= qunty
            f+=b
            T[itm]= {"quanity":c,"amount" : f}
            print("Item sold")
        else:
            print("Item not found")
    if a == 4:
        itm = input("Enter the item")
        if itm in T:
            del T[itm]
            print("Item Deleted")
    if a == 5:
        f= int(input("Enter 1 to see a particular item otherwise press any other number:"))
        if f== 1:
            itm = input("Enter the item:")
            if itm in T:
                print(T[itm])
        elif a != 1:
            print(T)
        print ("Amount left in the store == ", bdgt1)
    if a == 6:
        print("Thanks for using...exited")
        break
        
            

    

  
