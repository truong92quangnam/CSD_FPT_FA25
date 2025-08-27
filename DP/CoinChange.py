if __name__=="__main__":

    Coins=[2,4,6,9]
    Total=38

    Money=[Total]*(Total+1)

    Money[0]=0

    for money in range(Total+1):

        for coin in Coins:

            if money>=coin and Money[money-coin]+1<Money[money]:

                Money[money]=Money[money-coin]+1
                
    print(Money[Total])
