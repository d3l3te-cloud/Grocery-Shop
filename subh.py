T = {}
#Creating the item code in loop
a=10000
x=1

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
                    itmcode=x
                    x+=1
                    
                    
                print("Itemcode:",itmcode)
                T[itmcode]= {"Name":Itms,"Quantity":qunty,"Price":amt}
                 
            if a == 2:
                f= int(input("Enter 1 to see a particular item otherwise press any other number:"))
                if f== 1:
                    itm = int(input("Enter the itemcode:"))
                    print(T[itm])
                    
                
                elif f != 1:
                    print(T)
                    
                    
            if a ==3:
                print('Exiting Admininstrator...')
                break
                      
        

    if choice == 2:
        #see and correct below code
        #niche ek billing system banao jisme mujhe T wale tuple se ek Tuple T[itemcode] wala uthana hai , usmein se uski PRICE ki value jankr(access krke) quantity(billing me input hone wali) ko multiply krke total banana hai .
        #usko ek loop me ghumado taki multiple item ki billing ek sath ho ske, aur last me total print krdo  
        
        while True:
            type=int(input("enter 1 to continue billing , 2 to show bill and exit"))
            
            if type==1:
                total=0
                #billing procedure
                billitm=int(input("enter item code"))
                qnt=int(input('Enter quantity'))
                
                for amt in T[billitm]:
                    
                    c=amt*qnt
                    total=total+c

            if type==2:
                print(total)
                break
                    
                    
                
                





        
        #Delete below line
        print('Bill')
        print(total)
        #Deleteaboveline
