from asyncore import write


print("Coin = £2 Bag value = £20")
print("Coin = £1 Bag value = £20")
print("Coin = 50p Bag value = £10")
print("Coin = 20p Bag value = £10")
print("Coin = 10p Bag value = £5")
print("Coin = 5p Bag value = £5")
print("Coin = 2p Bag value = £1")
print("Coin = 1p Bag value = £1")

print("Coin = £2 weight = 12.00")
print("Coin = £1 weight = 8.75")
print("Coin = 50p weight = 8.00")
print("Coin = 20p weight = 5.00")
print("Coin = 10p weight = 6.50")
print("Coin = 5p weight = 2.35")
print("Coin = 2p weight = 7.12")
print("Coin = 1p weight = 2.56")



name = input("What is your Name")
coin = input("What is the Coin")
weight = input("weight of bag")


if coin == "£2":
    if float(weight) > (12.00 * 10):
       amountToChange = float(weight) - (12.00 * 10)
       print("You are ", amountToChange, " over the needed amount")

       acc = float(weight) / (12.00 * 10) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write(name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (12.00 * 10):
       amountToChange = (12.00 * 10) - float(weight)
       print("You are ", amountToChange, " under the needed amount")

       coincount = open("CoinCount.txt","a")
       coincount.write(name + "," + coin + "," + str(weight))
       coincount.close()

    else:
        print("ADDED")

        coincount = open("CoinCount.txt","a")
        coincount.write( name + "," + coin + "," + str(weight))
        coincount.close()




if coin == "£1":
    if float(weight) > (8.75 * 20):
       amountToChange = float(weight) - (8.75 * 20)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (8.76 * 20) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write(name + "," + coin + "," + str(weight ))
       coincount.close()

    elif float(weight) < (8.75 * 20):
       amountToChange = (8.75 * 20) - float(weight)
       print("You are ", amountToChange, " under the needed amount")

       coincount = open("CoinCount.txt","a")
       coincount.write(name + "," + coin + "," + str(weight ))
       coincount.close()

    else:
       print("ADDED")

       coincount = open("CoinCount.txt","a")
       coincount.write(name + "," + coin + "," + str(weight ))
       coincount.close()




if coin == "50p":
    if float(weight) > (8.00 * 20):
       amountToChange = float(weight) - (8.00 * 20)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (8.00 * 10) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (8.00 * 20):
       amountToChange = (8.00 * 20) - float(weight)
       print("You are ", amountToChange, " under the needed amount")

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    else:
       print("ADDED")

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()      




if coin == "20p":
    if float(weight) > (5.00 * 50):
       amountToChange = float(weight) - (5.00 * 50)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (5.00 * 50) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (5.00 * 50):
       amountToChange = (5.00 * 50) - float(weight)
       print("You are ", amountToChange, " under the needed amount")
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    else:
       print("ADDED")

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()




if coin == "10":
    if float(weight) > (6.50 * 50):
       amountToChange = float(weight) - (6.50 * 50)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (6.50 *50) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (6.50 * 50):
       amountToChange = (6.50 * 50) - float(weight)
       print("You are ", amountToChange, " under the needed amount")

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    else:
       print("ADDED")
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()




if coin == "5p":
    if float(weight) > (3.35 * 100):
       amountToChange = float(weight) - (12.00 * 100)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (3.35 *100) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (12.00 * 100):
       amountToChange = (12.00 * 100) - float(weight)
       print("You are ", amountToChange, " under the needed amount")

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    else:
       print("ADDED") 
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()




if coin == "2p":
    if float(weight) > (7.12 * 50):
       amountToChange = float(weight) - (7.12 * 50)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (7.12 *50) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (7.12 * 50):
       amountToChange = (7.12 * 50) - float(weight)
       print("You are ", amountToChange, " under the needed amount")
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    else:
       print("ADDED")
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close() 




if coin == "1p":
    if float(weight) > (3.56 * 100):
       amountToChange = float(weight) - (3.56 * 100)
       print("You are ", amountToChange, " over the needed amount")

       acc = weight / (3.56 *100) * 100

       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    elif float(weight) < (3.56 * 100):
       amountToChange = (3.56 * 100) - float(weight)
       print("You are ", amountToChange, " under the needed amount")
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()

    else:
       print("ADDED")
       coincount = open("CoinCount.txt","a")
       coincount.write( name + "," + coin + "," + str(weight))
       coincount.close()      

list = ["1p","2p","5p","10p"]

test =input("enter coin:")

if test in list:
   print("found")
else:
   print("not found")

   
##if name == "-show list":


