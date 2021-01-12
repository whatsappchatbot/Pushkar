## sample code for basic chatbot
# run this on your python compiler
# change the whatsapp number wherever mentioned
# send message to twilio number I sent you today morning 

'''join sandbox by sending "join until-speech" '''

from twilio.rest import Client 
account_sid = 'ACa0240b19312bea7ebb0ad16d5dba1ef1'
auth_token = 'cb5e0f306256b89ac7cdc8c1cc68f83f'
client = Client(account_sid, auth_token) 

def sendtxt(message , person="+919860224038"):      #paste your whatsapp number here
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body= message,      
                                  to='whatsapp:{}'.format(person) 
                              )
def sendimg(url="https://i0.wp.com/indiacanteen.tastyfix.com/wp-content/uploads/2018/11/1-2.png?fit=600%2C400&ssl=1" , person = "7666779269"):
    message = client.messages.create(
             media_url=[url],
             from_='whatsapp:+14155238886',
             body="It's snacks time!,yummy maggie for you😋😋..!!",
             to='whatsapp:+91{}'.format(person)
         )


def hello():
    return "Hello, World!"

def switch0(arg0):
    return switch1("Hi")

def switch1(argument): 
    mydict = {"Hi": 'जी वस्तू मागवायची आहे जस कि जर दूध हवे असेल तर 1 ,बिस्किट्स साठी 3 ,इ. याप्रमाणे आकडे निवडा ..🙂\n\n\n1: Categories \n2: Exit',
              "1": "\n1: milk \n2: Dal\n3: Oil Products\n4: Soap\n'EXIT' to checkout\n'CART' to view cart",
              "2":"code       company       rate(inRs)\n 1            amul milk            56 \n 2            warna milk          56 \n  3            gokul milk           56 \n  4            nandini milk        54 \n\n\n1: To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
               "3":"Code.        Company.          Rate \n 1.             Mug.                  80/kg\n 2.             Masoor.            60/kg\n 3.            Harbhara.          70/kg \n 4.             Toordal.            70/kg \n 5.             Masoordal.       75/kg \n\n\n1: To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
               "4":"Code.         Company.       Price \n  1.               Fortune          130/kg \n 2.               Gemini.          128/kg \n 3.                Safola.          120/kg \n 4.               Star.                120/kg \n 5.                Kirtigold.       115/kg \n\n\n1: To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
               "5":"code       company       rate(inRs) \n 1.         surfexcel soap         10 \n 2         vim soap                  10 \n 3         wheel soap               8 \n 4         tiptop soap               7 \n 5         hamam soap            6 \n\n\n1: To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
             "Hi2.0": " to add next item in your cart,make your next choices \n1: milk \n2:dal\n3:oilProducts\n4: Soap ",
             }    
    
    a = "plz give correct input option number.I am still in learning phase."
    return  (mydict.get(argument, a))
    
def switch2(arg3):
        switcher = {
            "2": "how many litres of milk do you want?\n\n\n 'BACK' go back\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories", 
            "3": "how many grams or KGs of Dal you want to buy?\n\n\n 'BACK' go back\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories", 
            "4": "how many Kgs of oil do you need?\n 'BACK' go back\n\n\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories",
            "5": "how many soaps do you want?\n\n\n 'BACK' go back\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories",
            }
        return switcher.get(arg3)
def switchq(argq):
        switcherq = {
            "2": "litres", 
            "3": "kg", 
            "4": "kg",
            "5": "nos"
            }
        return switcherq.get(argq)

def switch3(arg3):
    switchof="select the correct option-- \n 1. add next  \n 2. no more ,place order"
    return switchof
  
def switch4(arg4):
    dictl = {"1":switch1("Hi"),
             "2":"your order is taken by our side",
            }
    return dictl.get(arg4," I don't understand your response plz make it correct")
  
class sub1():
    flag = 0
    cat = 0
    item = 0
    final = 'Your Cart \nItem   Quantity\n'
    def __init__(self,cust):
        self.cust = cust
        self.cart = {'2':{},'3':{},'4':{},'5':{}}
        
        
    def add_and_show(self,arg):        
        if arg in ["Hi","hi","HI"]:
            return  switch1("Hi")
        elif (self.flag==0 and arg=="1"):
            self.flag+=1
            print(self.flag)
            return switch1("1")
        elif(self.flag==0 and arg =="2"):
            self.flag=0
            return "Thankyou"
        elif(arg=='EXIT'):
            op = self.final+'Thank-you for shopping with us'
            return op
        elif(arg=='CAT'):
            self.flag=1
            return switch1('1')
        elif(arg=='CART'):
            return self.final+"\n\n'EXIT' to checkout\n'CAT' to view categories"
        elif(self.flag==1 and (arg =="1" or arg=="2" or arg=="3" or arg=="4")):
            self.cat = str(int(arg)+1)
            self.flag+=1
            print(self.flag)
            return switch1(str(int(arg)+1))
        elif(self.flag==2 and arg=='1'):
            self.flag+=1
            return switch2(self.cat)
        elif(self.flag==3 and arg=='BACK'):
            self.flag-=1;
            return switch2(self.cat)
        elif(self.flag==3):
            lst = []
            it, qu = arg.split()
            self.final+=it
            self.final+="   "
            self.final+=qu
            self.final+=' '
            self.final+=switchq(self.cat)
            self.final+='\n'
            op = "Succesfully Added to CART\n'EXIT' to checkout\n\n\n'CART' to view cart\n 'CAT' to view categories"
            self.cart[self.cat][it]=qu
            return op

                
        elif(self.flag==3 and arg=='BACK'):
            self.flag-=1;
            return switch2(self.cat)
        elif(self.flag==2 and arg=='BACK'):
            self.flag-=1;
            return switch1("1")
        elif(self.flag==1 and arg=='BACK'):
            self.flag-=1;
            return "Thankyou"
        else:
            self.flag=1
            return switch1('1')
            

            

    #msg = input()
rem = "+919860224038"                   #paste your whatsapp number here

obj = sub1(rem)
def sms_reply(msg):
    am = msg
    api = obj.add_and_show(am)
    
    return sendtxt( api,rem)
 
    
while (True):
    msg = input()
    sms_reply(msg)
    if(msg =='EXIT'):
        break               #run this and give input here but you will see reply on your whatsapp 
    