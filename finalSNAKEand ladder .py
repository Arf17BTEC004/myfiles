#SN  AKE and LADDER
import random
count=0
while int(count < 100) :
    i=input("press r to roll a dice")
    if i=="r" :
        a=random.randint(1,6)
        count=count+a
    print("your random is",a)
    print("your position is",count)
    if count==8 :
        count=37
        print("you climb the ladder",count)
    elif count==13 :
                   count=2
                   print("you get a snake bite",count)
    elif count==13  :
                   count=34
                   print("you climb the ladder",count)
    elif count==25 :
                   count=4
                   print("you get a snake bite",count)
    elif count==38:
                    count=9
                    print("you get a snake bite",count)
    elif count==40:
                    count=68
                    print("you climb the ladder",count)
    elif count==52:
                    count=81
                    print("you climb the ladder",count)
    elif count==65:
                     count=46
                     print("you get a snake bite",count)
    elif count==76 :
                    count=97
                    print("you climb the ladder",count)
    elif count==89 :
                    count=70
                    print("you get a snake bite",count)
    elif count==93 :
                    count=64
                    print("you get a snake bite",count)
    
    elif count>=100 :
        print("you win")
                  
          


