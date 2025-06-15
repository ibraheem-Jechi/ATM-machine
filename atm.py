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
             4. Exit""")
    
    option = int(input("What do you want to do: "))

    if option == 1:
        newBalance = balance
        print ("Your current Balance is: " +str(newBalance)+ "$")

    elif option == 2:
       deposit=float(input ("Amount you want to deposit= "))
    #    balance.append(deposit)
       balance += deposit
       print("Your Current balance is "+str(balance)+"$")
    elif option == 3:
        withdraw = float(input("Amount you want to withdraw= "))
        if balance>=withdraw:
         balance -= withdraw
        else:
           print("Not Enough Money")
           print("Your current balance is "+str(balance)+ "$")
          
    elif option == 4:

        print("you added " +str(deposit)+ "$ and withdrawed " +str(withdraw)+"$")
        print("You are welcomed")

    else:
       print("Invalid Option")