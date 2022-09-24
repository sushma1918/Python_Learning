
import datetime
def wish():
    hour=datetime.datetime.now().hour
    if hour >=0 <= hour < 12:
        print("Good morning")
    elif hour >= 12 and hour < 16:
       print("Good Afternoon !")
    elif hour >= 16 and hour < 20:
       print("Good Evening!")   
    else:
        print("Good Night dear sushma   ")
    print("I'm an AG3 ASSISTANT, can I help you Sushma?.")


if __name__ == "__main__":
     #print(" This Module is made for  wish  to sting of the program  according to time \n ! ")  
    # print("I'm an AG3 ASSISTANT,dear sir, have any orders for me?")
     wish()
         
