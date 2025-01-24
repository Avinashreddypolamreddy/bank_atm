#Creating users along with their passwords/pins and stored in the dictionaries
users={"avinash":2407,"anjani":1106,"aravind":1508,"bhanu":1234,"sai":5678}

#Imporing neccessary modules 
from datetime import datetime

#Assigning amounts for each individual
amount={"avinash":15000,"anjani":11000,"aravind":1800,"bhanu":1200,"sai":50000}




print (f"{" "*10} {"Welcome to the Atm":<40}{datetime.now()}")
print(f"_"*40)
while True:
 a=input("Enter your username:")
 b=int(input("Enter your password:"))
 if a in users:
    if users[a]==(b):
     print(f"hi,{a}")
     break
    else:
     print("Incorrect credentias")
 else:
  print("There was no such user") 


while True:
 print("Here are your options")
 options="""
 1.Credit
 2.Debit
 3.Check the balance
 4.Exit

"""
 print(options)
 c=int(input("Enter the options:"))
 if c==1:
     credit=float(input("Enter the credit amount:"))
     amount[a]=float(amount[a])+credit
     print(f"Rupees of {credit} credited in your account and total balance is {(amount[a])}")
   
 elif c==2:
    debit=float(input("Enter the debit amount:"))
    if debit<=amount[a]:
       amount[a]-=debit
       print(f"Rupees of {debit} has been debited from your account and updated balance is {amount[a]}")
    else:
     print("Dont have sufficient balance")
 elif c==3:
    print(f"here is your updated balance {amount[a]} at {datetime.now()}")
 elif c==4:
    print("Thank you")
 else:
   print("incorrect input")
