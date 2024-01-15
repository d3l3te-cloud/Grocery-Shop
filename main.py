T = {
    1: {"Name": "POTATO", "Quantity": 10},
    2: {"Name": "TOMATO", "Quantity": 15},
    3: {"Name": "ONION", "Quantity": 20},
    4: {"Name": "APPLE", "Quantity": 25},
    5: {"Name": "BANANA", "Quantity": 30},
    6: {"Name": "JACKFRUIT", "Quantity": 50},
    7: {"Name": "CABBAGE", "Quantity": 60},
    8: {"Name": 'CARROT', "Quantity": 34},
    9: {"Name": "CAULIFLOWER", "Quantity": 356},
    10: {"Name": "RADDISH", "Quantity": 930},
    11: {"Name": "WATERMELON", "Quantity": 630},
    12: {"Name": "PAPAYA", "Quantity": 12},
    13: {"Name": "GRAPEFRUIT", "Quantity": 32},
    14: {"Name": "LEMON", "Quantity": 30},
    15: {"Name": "STRAWBERRY", "Quantity": 30},
    16:{"Name": "MELON", "Quantity": 30},
    17: {"Name": "COCONUT", "Quantity": 30},
    18: {"Name": "AVOCADO", "Quantity": 45},
    19: {"Name": "KIWI", "Quantity": 35},
    20: {"Name": "MUSHROOM", "Quantity": 78},
    21: {"Name": "BROCCOLI", "Quantity": 35},
    22: {"Name": "CHILLI", "Quantity": 35},
    23: {"Name": "LEAK", "Quantity": 30},
    24: {"Name": "GARLIC", "Quantity": 37},
    25: {"Name": "CORIANDER", "Quantity": 90},
    26: {"Name": "PEAS", "Quantity": 67},
    28: {"Name": "GREEN BEAN", "Quantity": 780},
    29: {"Name": "CAPSCICUM", "Quantity": 90},
    30: {"Name": "BEETROOT", "Quantity": 360},
    31: {"Name": "CUCUMBER", "Quantity": 30},
    32: {"Name": "MINT", "Quantity": 30},
    33: {"Name": "CHIVE", "Quantity": 34},
    34: {"Name": "CHOKEBEERY", "Quantity": 60},
    35: {"Name": "FENNEL", "Quantity": 320},
    36: {"Name": "LADYFINGER", "Quantity": 130},
    37: {"Name": "OKRA", "Quantity": 308},
    38: {"Name": "TAMARIND", "Quantity": 630},
    39: {"Name": "LICHI", "Quantity": 309},
    40: {"Name": "MANGO", "Quantity": 380},
    41: {"Name": "JAMUN", "Quantity": 50},
    42: {"Name": "DRAGON FRUIT", "Quantity": 30},
    43: {"Name": "PEAR", "Quantity": 34},
    44: {"Name": "CHERRY", "Quantity": 67},
    45: {"Name": "RICE", "Quantity": 87},
    46: {"Name": "JERRA RICE", "Quantity": 63},
    47: {"Name": "BASMATI RICE", "Quantity": 30},
    48: {"Name": "BOILED RICE", "Quantity": 23},
    49: {"Name": "TOOR DAL", "Quantity": 32},
    50: {"Name": "CHICK PEAS", "Quantity": 54},
    51: {"Name": "BLACKGRAM", "Quantity": 40}
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
                    itmcode = int(input("Enter the itemcode:"))
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
                            outstock=int(input("Selling quantity is not is stocks:)  Enter 1 to add all remaining in cart..."))
                            if outstock==1:
                                sp=int(input("Enter the sell price of the item per unit:"))
                                qunty=T[itmcode]["Quantity"]
                                total_sp+=qunty*sp
                                T[itmcode]["Quantity"]=0
                                get= T[itmcode]["Name"]
                                billing_dict[get]=qunty
                                
                                
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
                print("Exiting billing..")
                print("Exited billing")
                break
            else:
                continue


    if choice == 3:
        print("Store closed...")
        break

    else:
        continue

        
            

    

  
