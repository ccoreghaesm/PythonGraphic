#               In The Name Of Allah
#                   1396/06/15
#this Program Writed By : Ghasem Ramezani Manesh .@ASFisher
#From Iran,Esfahan,Math House
#My Teacher's In Python :
#                  ~Ms.Radmanesh
#                  ~Mr.Bagheri
#About This Program:
#   ~Class Simple_Accountant:
#       User's Can Use the Input_Date_AllMoney() to Enter Date And All The Money They Have.
#       And Use the Spend() to Enter the Amount Spend Money And Calculate. weit transaction() they can
#       Register The Spend Money.
#       To Save or Load The File's. User's Can Use the Save_Load() . this Method Have one
#       Parametr ,to Choice Append the new Text to Old File or Create a New File And Store The Date
#   ~Class Calculator
#       A Simple Calculator with:
#                   1-Addition
#                   2-Subtraction
#                   3-Multiplication
#                   4-Division
#                   5-Power
import os.path
import turtle
import random
from time import sleep
import os
##-----------------Class-Definition-----------------
class Simple_Accountant:
    ##Variable-Definition:
    Date="0000/00/00" #To Keep History
    All_the_Money=0.0 #To Keep All The Money
    Remaider_Money=0.0#To Keep Remaider Money
    Transaction=['',] #Strign List User Transaction
    ##End-Variable-Definition-
    ##Method-Definition:
    def Input_Date_AllMoney(self,money,date): #|--> Enter Date . Like : 2017-05-12
        try:
            if (len(date) == 10): #If The Input Data Was Valid
                self.Date = date
            else:
                return -1 #Unsuccessful Operation
            self.All_the_Money = money
            self.Remaider_Money=self.All_the_Money
##            print(str(self.Remaider_Money))
            return 0 #Successful Operation
        except:
            return -1 #Unsuccessful Operation
        #---------------------------------------------------------------
    def Spend(self,spend_money): #Calculate The Amount Spend
        try:
##            print(str(spend_money))
##            print(str(self.Remaider_Money))
            if(spend_money <= self.Remaider_Money):
                self.Remaider_Money = (self.Remaider_Money-spend_money)
                #T_action |--> Generate Output Format On File 
                T_action = str("["+str(self.Date)+"]-["+str(self.All_the_Money)+"]-["+str(spend_money)+"]-["+str(self.Remaider_Money)+"]")
                self.Transaction.append(T_action)
                return 0#Successful Operation
            elif (spend_money > self.Remaider_Money):
                return -2#The Amount Entered is Greate Then The Remainder
            elif (self.All_the_Money == 0):
                return -1#The Remainder Is Zero
            else:
                return -3#Unsuccessful Operation
        except:
            return -4
        
        #---------------------------------------------------------------
    def Save_Load(self,mode):
        try:
            #File |--> Defined For Help
            if(mode==1):
                if(os.path.isfile("Transaction.txt")):#Check If File Exist:(True) Append  (False) Creat
                    File = open("Transaction.txt","a")
                else:
                    File = open("Transaction.txt","w")
                for i in self.Transaction:
                    File.write(i+"\n")
                File.close()
                return 0
            elif(mode==0):
                #Text_In_File |--> Defined For Print File
                lines=['',]
                with open('Transaction.txt') as f:
                    lines = f.readlines()
                print("                             "+str(self.Date))
                print("---------------------------------------------------------------------------------")
                print("      Date             All The Money            Spend            Remaider Money")
                print("------------------   ------------------   ------------------   ------------------")
                for i in range(len(lines)): #Get Line Number for Scrolling
                    _string_1 = lines[i] #Get a Line And Pour in _string_1
                    _string_2 = '' #Auxiliary Variable To Save Words
                    _string_3 = '' #Auxiliary Variable To Print Sorted Words
                    #print('Im Here')
                    for j in range(len(_string_1)): #A Loop To Scroll A Line
                        #print('Im Here_2')
                        if (_string_1[j]=='[' or _string_1[j]==']' or _string_1[j]=='-'): #Check Separating Points
                            #print('Im Here_3')
                            continue
                        else:
                            #print('Im Here_4')
                            _string_2+=_string_1[j] #Save Alphabets
                            #print('Im Here_7')
                        try: #If The Line Is Reached, The Program Error Does Not Appear
                            if (_string_1[j+1]==']'): #If The Word Is Complete, Save It
                               #print('Im Here_5')
                               _string_3 += _string_2+"               " #Save And Organize
                               _string_2 = ''
                               #print('Im Here_6')
                        except:
                            pass
                    print(_string_3) #Print A Regular Line
                return 0#Successful Operation
        except:
            return -1#Unsuccessful Operation
        #---------------------------------------------------------------
##-------------END-Class-Definition-----------------
##-----------------Class-Definition-----------------
class Calculator:
    def addition(self,num1,num2):
        return num1+num2
    def subtraction(self,num1,num2):
        return num1-num2
    def multiplication(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        if num2==0:
            return -1
        else:
            return num1/num2
    def Power(self,base,power):
        try:
            if power>1:
                return (base*self.Power(base,power-1))
            else:
                return base
        except:
            return -1
    def quiz(self):
        m=[0,0]
        try:
            m[0]=int(input("Enter First Number: "))
            m[1]=int(input("Enter Second Number: "))
        except:
            return -1
        return m
    def menu(self):
        print("\t>>>[1]-Addition Tow Number ")
        print("\t>>>[2]-Subtraction Tow Number ")
        print("\t>>>[3]-Multiplication Tow Number ")
        print("\t>>>[4]-Division Tow Number ")
        print("\t>>>[5]-Power A Number ")
        print("\t>>>[6]-Exit To Program Menu ")
        Input = int(input())
        if(Input >=1 and Input <= 6):
            return Input
        else:
            return -1
##-------------END-Class-Definition-----------------
Mode_Choice=int(input("\n\t<><><>>[1]-Graphic Mode\n\t<><><>>[2]-Text Mode\n\n\t>>->:"))
if(Mode_Choice == 2):
    os.system('cls')
    ##-----------------Text-Base-Menu-------------------
    def Menu():
        print("\t>>>[1]-Enter Date And All The Money")
        print("\t>>>[2]-Enter The Amount Spend ")
        print("\t>>>[3]-Save The File ")
        print("\t>>>[4]-Load The File\n\t      **The File Must Be In Program Direction ")
        print("\t>>>[5]-Run Calculator ")
        print("\t>>>[6]-Exit ")
        Input = int(input())
        if(Input >=1 and Input <= 6):
            return Input
        else:
            return -1
        
    _SA = Simple_Accountant() # Build An Object From Simple_Accountant
    _CL = Calculator() # Build An Object From Calculator
    while True:
        Choice = Menu()
        if(Choice == 1):
            date=str(input("Enter Date . Like : 2017/05/12 >>>"))
            money=int(input("Enter All The Money  >>>"))
            Error_Exception=_SA.Input_Date_AllMoney(money,date)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Input The Data or All The Money")
                print("      ~:Check >>>1-Data Input Must Be String .Like --> 0000/00/00 (Lentgh=10)")
                print("      ~:Check >>>2-Money Input Must Be Integer or Flowt\n")
            continue
        elif(Choice ==2):
            spend=int(input("Enter The Amount You Spend >>>"))
            Error_Exception=_SA.Spend(spend)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Input Spend Money")
                print("      ~:Check >>>1-The Remainder Is Zero\n")
            elif(Error_Exception==-2):
                print("Error ~: Something Wrong in Input Spend Money")
                print("      ~:Check >>>1-The Amount Entered is Greate Then The Remainder\n")
            elif(Error_Exception==-3):
                print("Error ~: Something Wrong in Input Spend Money")
                print("      ~:Check >>>1-Unsuccessful Operation. Tray Again\n")
            continue
        elif(Choice ==3):
            Error_Exception=_SA.Save_Load(1)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Save")
                print("      ~:Check >>>1-Directory Most Be Exist")
                print("      ~:Check >>>2-Drive Has No Space")
                print("      ~:Check >>>3-Unsuccessful Operation. Tray Again\n")
            continue
        elif(Choice ==4):
            Error_Exception=_SA.Save_Load(0)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Load File")
                print("      ~:Check >>>1-Directory Most Be Exist")
                print("      ~:Check >>>2-File Not Found")
                print("      ~:Check >>>3-Unsuccessful Operation. Tray Again\n")
            continue
        elif(Choice ==5):
            while True: 
                _BackF=[]
                Sub_Choice=_CL.menu()
                if(Sub_Choice==1):
                    _BackF=_CL.quiz()
                    print("Operation Result :>>>"+str(_CL.addition(_BackF[0],_BackF[1])))
                    continue
                elif(Sub_Choice==2):
                    _BackF=_CL.quiz()
                    print("Operation Result :>>>"+str(_CL.subtraction(_BackF[0],_BackF[1])))
                    continue
                elif(Sub_Choice==3):
                    _BackF=_CL.quiz()
                    print("Operation Result :>>>"+str(_CL.multiplication(_BackF[0],_BackF[1])))
                    continue
                elif(Sub_Choice==4):
                    _BackF=_CL.quiz()
                    print("Operation Result :>>>"+str(_CL.division(_BackF[0],_BackF[1])))
                    continue
                elif(Sub_Choice==5):
                    _BackF=_CL.quiz()
                    print("Operation Result :>>>"+str(_CL.Power(_BackF[0],_BackF[1])))
                    continue
                elif(Sub_Choice==6):
                    print("~Caculator Clesed")
                    break
            continue
        elif(Choice ==6):
            exit()
    ##-------------END-Text-Base-Menu-------------------
elif(Mode_Choice == 1):
    os.system('cls')
    ##-----------------Graphic-Base-Menu----------------
    def Calculater_Menu():
        os.system('Calculat.exe')
    _Color_List=['plum','mediumvioletred','purple','limegreen','red','pink','darkgreen','tan','gray','cyan','navy','coral','indigo','magenta','royalblue','blue','darkblue','deepskyblue','seagreen','gold',]
    _Windows=turtle.Screen()  #Initialize _Windows with Screen() a Attribute from Turtle Moudle
    _Windows.setup(800,600)  #Setup the Screen with 800px ~ 600px
    _Windows.title("Simple - Accountant")
    _turtle_1=turtle.Turtle()  #Create a Object From turtle
    ##_turtle_1.hideturtle()
    _turtle_1.speed('fastest')
    _turtle_1.up()
    _turtle_1.goto(-250,250)
    _turtle_1.down()
    _turtle_1.pensize(2)
    for i in range(4):
        _turtle_1.forward(500)
        _turtle_1.right(90)
    _turtle_1.up()
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1_HelpString = "For the first time, the user must enter\n the date and amount of all his money.\n Then you can enter your expenses,\n and save your transactions "
    _turtle_1.goto(-150,125)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write('1-Enter Date And All The Money', move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.goto(-150,100)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write('2-Enter The Amount Spend', move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.goto(-150,75)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write('3-Save The File', move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.goto(-150,50)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write('4-Load The File', move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.goto(-150,25)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write('5-Run Calculator', move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.goto(-150,0)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write('6-Exit', move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.goto(-240,-200)
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.write(_turtle_1_HelpString, move=False, align="left", font=("Chaparral Pro Light", 20, "bold"))
    _turtle_1.color(_Color_List[random.randrange(0,20)])
    _turtle_1.goto(-150,140)
    _SA = Simple_Accountant() # Build An Object From Simple_Accountant
    _CL = Calculator() # Build An Object From Calculator
    while True:
        _User_Choise=_Windows.numinput("Choice Dialog","Enter Your Option's Number :",default=None,minval=1,maxval=6)
        if(_User_Choise == 1):
            money=int(_Windows.numinput("Input","Enter All Money You Have :",default=None,minval=0))
            date=str(_Windows.textinput("Input","Enter Date . Like : 2017/05/12 :"))
            Error_Exception=_SA.Input_Date_AllMoney(money,date)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Input The Data or All The Money")
                print("      ~:Check >>>1-Data Input Must Be String .Like --> 0000/00/00 (Lentgh=10)")
                print("      ~:Check >>>2-Money Input Must Be Integer or Flowt\n")
        elif(_User_Choise ==2):
            spend=int(_Windows.numinput("Input","Enter The Amount You Spend :",default=None,minval=0))
            Error_Exception=_SA.Spend(spend)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Input Spend Money")
                print("      ~:Check >>>1-The Remainder Is Zero\n")
            elif(Error_Exception==-2):
                print("Error ~: Something Wrong in Input Spend Money")
                print("      ~:Check >>>1-The Amount Entered is Greate Then The Remainder\n")
            elif(Error_Exception==-3):
                print("Error ~: Something Wrong in Input Spend Money")
                print("      ~:Check >>>1-Unsuccessful Operation. Tray Again\n")
        elif(_User_Choise ==3):
            Error_Exception=_SA.Save_Load(1)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Save")
                print("      ~:Check >>>1-Directory Most Be Exist")
                print("      ~:Check >>>2-Drive Has No Space")
                print("      ~:Check >>>3-Unsuccessful Operation. Tray Again\n")
        elif(_User_Choise ==4):
            Error_Exception=_SA.Save_Load(0)
            if(Error_Exception==0):
                pass
            elif(Error_Exception==-1):
                print("Error ~: Something Wrong in Load File")
                print("      ~:Check >>>1-Directory Most Be Exist")
                print("      ~:Check >>>2-File Not Found")
                print("      ~:Check >>>3-Unsuccessful Operation. Tray Again\n")
        elif(_User_Choise ==5):
            Calculater_Menu()
            
        elif(_User_Choise ==6):
            exit()
        
    ##-------------END-Graphic-Base-Menu----------------
else:
    print("Worng Input.Exit And Tray Again!")
    exit()
