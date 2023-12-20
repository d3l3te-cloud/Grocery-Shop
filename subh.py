T={}
a=int(input('Enter what to do'))
price=0
TOM=1000
POT=1000
MOS=109
if a=='CODE':
    print('TOMATO :1 Price:10rs/kg'
           'POTATO :2 Price:20RS/kg'
           'Mosturizer:3 Price:100/unit')
while True:
    
    #for billing
    
    if a==1:
        total=0
        while True:
            
            inp=int(input('press 1 for billing/continue billing , 2 for showing bill , 3 for exiting to main menu'))
            if inp==1:
                b=int(input('Enter Item CODE'))
                qty=int(input('Enter qty in unit'))
                if b==1:
                    price=10
                    TOM=TOM-qty
                if b==2:
                    price=20
                    POT=POT-qty
                if b==3:
                    price=100
                    MOS=MOS-qty

                z=(qty*price)
                total=total+z
            if inp==2:
                print(total)
            if inp==3:
                a=int(input('Enter what to do'))
                total=0
                break
                
            


            
            

    if a==2:
        print('Welcome to administrator ! Choose Service-')
        adm=int(input('press 1 to show stock // press 2 to restock '))
        if adm==1:
            print('TOMATO: ',TOM,'POTATO: ',POT,'MOSTURIZER: ',MOS)
        if adm==2:
            while True:
                code=int(input('ITEM code(Press OK to administrator setting'))
                refill=int(input('enter refill amount'))
                if code==1:
                    TOM=TOM+refill
                if code==2:
                    POT=POT+refill
                if code==3:
                    MOS=MOS+refill
                if code=='OK':
                    adm=int(input('press 1 to show stock // press 2 to restock '))
                    
                    break
            if adm==3:
                
                break
                
