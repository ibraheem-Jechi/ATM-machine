balance = 1000

option = 0

password = 2332

deposit = 0

withdraw = 0

code = int(input("Enter Your Password: "))
if code !=password:
   print("Password is incorrect, try again: ")
   exit()

while option !=4:

    print ("""
           Welcome to the ATM:
             1. Check Balance
             2. Deposit Money
             3. Withdraw Money
             4. Exit
           """)
    
    option = int(input("How Can I Hwlp You: "))

    if option == 1:
        newBalance = balance
        print ("Your current Balance is: " +str(newBalance)+ "$")

    elif option == 2:
       deposit=float(input ("Please Enter the Amount you need to Deposit:  "))
    #    balance.append(deposit)
       balance += deposit
       print("Your Current balance is "+str(balance)+"$")
    elif option == 3:
        withdraw = float(input("Please Enter the Amount you need to Withdraw: "))
        if balance>=withdraw:
         balance -= withdraw
        else:
           print("Sorry, No Enough Money")
           print("Your current balance is "+str(balance)+ "$")
          
    elif option == 4:

        print("Amount added= " +str(deposit)+ "$" )
        print("Amount withdrawed= " +str(withdraw)+"$")
        print("You are welcomed")

    else:
       print("Invalid Option")
