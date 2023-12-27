T = {
    1: {"Name": "POTATO", "Quantity": 10},
    2: {"Name": "TOMATO", "Quantity": 15},
    3: {"Name": "ONION", "Quantity": 20},
    4: {"Name": "APPLE", "Quantity": 25},
    5: {"Name": "BANANA", "Quantity": 30},
    # Add more items in a similar way
    # ...
    100: {"Name": "ORANGE", "Quantity": 40}
}
s = {}
total_cp,total_sp=0,0
loop,loop1=1000,0
#Creating the item code in loop

while True:
    choice= int(input(" 1 for administration, 2 for billing, 3 to close store:...entering alphabets causes error"))

    #ADMINISTRATION ENTERING
    if choice == 1:
        while True:
            a = int(input(" 1 to add items,2 to add stocks,3 to display and 4 to exit administration:"))
            if a==1:
                #ONLY ITEMS ADDING
                Itms= input("Enter the item")
                if Itms not in s:
                    loop+=loop1
                    loop1+=1
                    itmcode=loop
                    qunty= 0                    
                    T[itmcode]= {"Name":Itms,"Quantity":qunty}
                    print("Itemcode for",Itms,"=",itmcode)
                    s[Itms]=0
                    
                elif Itms in s:
                    print("Items already present:")
                
            if a == 2:
                #ONLY STOCKS ADDING
                
                while True:
                    a = int(input("Do you want to continue stocks? if yes press 1 otherwise any number:"))
                    if a == 1:
                        itmcode = int(input("Enter the itmcode):"))
                        if itmcode in T:
                            qunty= int(input("Enter the quantity of the item:"))
                            amt= int(input("Enter the price of  a single item:"))
                            total_cp+=qunty*amt
                            
                            T[itmcode]["Quantity"]+=qunty
                            print("Item added to stock_")
                        else:
                            print("Item not found:)")
                    print("TOTAL COST PRICE_",total_cp)
                    if a!=1:
                        break
                    else:
                        continue
            if a == 3:
                #PRINTING STOCKS
                f= int(input("Enter 1 to see a particular item otherwise press any other number:"))
                if f== 1:
                    itmcode = input("Enter the itemcode:")
                    if itmcode in T:
                        print(T[itmcode])
                    else:
                        print(" Item not found:)")
                if f != 1:
                    print(T)
                    print("Till now profit=",total_sp-total_cp)
                else:
                    continue
                    
            if a ==4:
                #CODES FOR ADMINISTRATION CLOSING:
                print("Exiting administration:")
                print("Administration exited_")
                break
            else:
                continue
    #BILLING ENTERING
    if choice == 2:
        while True:
            a=int(input('1 for billing/continue billing , 2 for showing bill , 3 to exit billing'))
            if a==1:
                billing_dict={}
                
                while True:
                    #INFINITE LOOP TO DO INFINITE BILLING
                    itmcode = int(input("Enter the itmcode:"))
                    if itmcode in T:
                        qunty=int(input("Enter the quantity of the item:"))
                        if T[itmcode]["Quantity"]-qunty >=0:                          
                            sp= int(input("Enter the sell price of the item per unit:"))
                            total_sp+=qunty*sp
                            T[itmcode]["Quantity"]-=qunty
                            get= T[itmcode]["Name"]
                            billing_dict[get]=qunty
                        else:
                            print("Selling quantity is not is stocks:)")
                    else:
                        print("Item not found:)")
                        
                    choose=int(input("Do you want to continue billing? if yes press 1 otherwise any number:"))
                    if choose==1:
                        continue
                    else:
                        break
            if a == 2:
                #PRINTING BILLS
                print(billing_dict)
                print("TOTAL SELL PRICE:",total_sp)
                
                
            if a == 3:
                print("Exiting billing_")
                print("Exited billing")
                break
            else:
                continue
                
                            
    if choice == 3:
        print("Store cloesd_")
        break
    
    else:
        continue