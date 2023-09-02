MILK=200
WATER=400
COFFEE=100
MONEY=0
def process_coins():
    global MONEY
    penny=int(input("enter the no of pennies"))
    dime=int(input("enter the no. of dimes"))
    nickel=int(input("enter the no of dimes"))
    quarter=int(input("enter the no. of quarters"))
    
    MONEY=penny*0.01+dime*0.10+nickel*0.05+quarter*0.25
    print(MONEY)



def print_resources():
    global MONEY
    print(f"avalable milk {MILK}ml\navailable water {WATER}ml\navailable coffee {COFFEE} grams ")
    print(f"{MONEY}")
    
    
    
    
def espresso():
     global MILK
     global WATER
     global COFFEE
     global MONEY

     print("here is your Espresso.\nEnjoy!!!")
     MILK=MILK-0
     WATER=WATER-50
     COFFEE=COFFEE-18
     MONEY=MONEY-1.5
     print(f"here is your change {MONEY} ")
        
def latte():
        global MILK
        global WATER
        global COFFEE
        global MONEY

        print("here is your latte.\nEnjoy!!!")
        MILK=MILK-150
        WATER=WATER-200
        COFFEE=COFFEE-124
        MONEY=MONEY-2.5
        print(f"here is your change {MONEY} ")        

def capuccino():
        global MILK
        global WATER
        global COFFEE
        global MONEY
    
        print("here is your capuccino.\nEnjoy!!!")
        MILK=MILK-100
        WATER=WATER-250
        COFFEE=COFFEE-24
        MONEY=MONEY-3.0
        print(f"hear is your change {MONEY} ")



def check_resources_Espresso():
    global MILK
    global WATER
    global COFFEE
    global MONEY
    process_coins()
    
    if MONEY>=1.5 and WATER>=50 and COFFEE>=18:
        espresso()
    
    else:    
    
        if MONEY<1.5:
            print("insuffient coins to get Espresso")
        if WATER<50:
            print("insufficient water to make Espresso")
        if COFFEE<10:
            print("insufficient coffee to make Espresso")
            
        print(f"here is your refund{MONEY}")
        
        
        
def check_resources_latte():
    global MILK
    global WATER
    global COFFEE
    global MONEY
    process_coins()
    
    if MONEY>=2.5 and WATER>=200 and COFFEE>=24 and MILK >=150:
        latte()
    
    else:    
    
        if MONEY<2.5:
            print("insuffient coins to get Latte")
        if WATER<200:
            print("insufficient water to make Latte")
        if COFFEE<24:
            print("insufficient coffee to make Latte")
            
        print(f"here is your refund{MONEY}")
        
       

def check_resources_capuccino():
    global MILK
    global WATER
    global COFFEE
    global MONEY
    process_coins()
    
    if MONEY>=3.0 and WATER>=250 and COFFEE>=24 and MILK >=100:
        capuccino()
    
    else:    
    
        if MONEY<1.5:
            print("insuffient coins to get capuccino")
        if WATER<250:
            print("insufficient water to make capuccino")
        if COFFEE<10:
            print("insufficient coffee capuccino")
            
        if MILK<100:
            print("insufficient milk for capuccino")
        print(f"here is your refund{MONEY}")
        
       
        



choice=input("enter your choioce\n E: for espresso, L: latte, : for capucinno Q: to quit")
while not choice=="q".lower():

    if choice=="E".lower():
        check_resources_Espresso()
    elif choice=="L".lower():
        check_resources_latte()
    
    elif choice=="C".lower():
        check_resources_capuccino()
        
print("please shutdown the machine")



