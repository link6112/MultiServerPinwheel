import random
from datetime import date

class BasicAccount:
    counter = 0
    @classmethod
    
    def acNumber(self):
        """
        This function within the class method defines the account number using the counter which is initialised above

        Parameters:
            None
        Returns:
            int - self.counter - The account number for the class object being created
        """
        self.counter += 1
        return self.counter

    def __init__(self, acName, openingBalance):
        """
        Initialiser function, initialises the account name and openingBalance. It will also
        generate a card number and set the variables cardNum, cardExp and AcNum based on functions
        within the class, while name and balance are set based on the parameters.
        The __init__ function also prints the name and openingBalance of the account.

        Parameters:
            str - acName - The name of the account holder
            float - openingBalance - The amount of money in the account upon opening
        Returns:
            None
        """

        self.name = acName
        self.balance = openingBalance
        self.cardNum = random.randint(0,9999999999999999)
        self.cardExp = self.issueNewCard()
        self.acNum = self.acNumber()
        

        #Giving account name and opening balance:
        print(self.name)
        print(self.balance)

    #definining __str__ so that when the object is printed, it returns only the account name
    def __str__(self):
        """
        Default string function. Will ensure the name and balance is printed upon print(class)

        Parameters:
            None
        Returns:
            The acName(string) and current balance(float).
        """
        return '{self.name}, \n {self.balance}'.format(self=self)

    #Deposits money into the account
    def deposit(self, amount):
        """
        This function will return the new balance once a positive float has been passed
        into it. It will NOT accept floats that are negative.

        Parameters:
            float - amount - Number to deposit
        Returns:
            float - self.balance - the new balance of the account
        """

        if amount > 0:
            self.balance += amount
            return self.balance
    
    #Withdraws money from the account, will not allow basic account to overdraft
    def withdraw(self, amount):
        """
        This will withdraw the amount of money requested. It useses the getAvailableBalance
        function to check the current balance of the account, this takes the premium account
        with overdrafts into consideration. It will then update the balance of the account and
        state how much was withdrawn and then what the new balance is.

        If the amount to withdraw is greater than the the availableBalance then no money will
        be withdrawn and the user will be informed of the error.
        Parameters:
            float - amount - amount to be withdrawn
        Returns:
            None
        
        """

        availableBalance = self.getAvailableBalance()
        if amount <= availableBalance and amount > 0:
            self.balance = self.balance - amount
            print(self.name, " has withdrawn £", amount, ". New balance is £", self.balance)
        elif amount > self.balance:
            print("Can not withdraw £", amount)
        

    #Acquire the available balance, including overdraft.
    def getAvailableBalance(self):
        """
        Will check the available balance for basic accounts by setting a variable
        to equal the balance and returning that. This is done so that the premium
        account version which takes the overdraft into account won't interfere.
        I.e. if I just returned self.balance then I would need to have a two different
        blocks of code with withdrawals, one for BasicAccount and one for PremiumAccount.

        Parameters:
            None
        Returns:
            None
        """
        availableBalance = self.balance
        return availableBalance
    
    #returning the balance
    def getBalance(self):
        """
        This function will return the balance, if negative it will still return this
        Parameters:
            None
        Returns:
            Float - self.balance - the current balance
        """
        return self.balance

    #printing the balance
    def printBalance(self):
        """
        This function will print the balance
        Parameters:
            None    
        Returns:
            None
        """
        print(self.balance)

    #returning the name
    def getName(self):
        """
        This function will return the acName
        Parameters:
            None
        Returns:
            None
        """
        return self.name

    #returning the account number as a string
    def getAcNum(self):
        """
        This function takes the acNum defined in the __INIT__ function and returns
        it as a string
        Parameters:
            None
        Returns:
            str - self.acNum - The account number as a string
        """
        return str(self.acNum)

    #generating a new card with exp date 3 years from now, the date will be given as a tuple, e.g. (03,21)
    def issueNewCard(self):
        """
        issueNewCard will use the datetime module to get the year and the month.
        It will then take the last 2 digits of the year and the month.
        The simplest method of getting the final 2 digits of the year was to
        cast the year to a string, slice it at position -2: and take the final
        two digits from that and cast this back into an int.
        The year and the date are then added to a tuple.
        Parameters:
            None
        Returns:
            tuple - (mm,yy) - The expiration date of the card.
        """

        theDate = date.today()
        theYear = theDate.year + 3
        theYear = str(theYear)
        year = theYear[-2:]
        year = int(year)
        cardExp = (theDate.month, year)

        return cardExp

    #closing account - Housekeeping sets everything to 0
    def closeAccount(self):
        """
        This function when called will do all relevant housekeeping - Setting everything
        to zero or an empty string.
        Parameters:
            None
        Returns:
            Boolean - True - Account closed is true when function is called.
        """

        availableBalance = self.getAvailableBalance()
        self.withdraw(availableBalance)
        self.balance = 0
        self.name = ""
        self.cardExp = (0,0)
        self.acNum = ""
        self.availableBalance = 0
        self.cardNum = 0
        return True




   


#Creation of a subglass of BasicAccount
class PremiumAccount(BasicAccount):
    #Initialising variables
    def __init__(self, acName, openingBalance, initialOverdraft):
        super().__init__(acName, openingBalance)
        """
        This subclass initialises a new variable, initialOverdraft which gives 
        the user a certain amount of overdraft that can be used.
        This will also set the overdraft to True so that if an overdraft is present
        it can be checked.
        Parameters:
            str - acName
            float - openingBalance
            float - initialOverdraft
        Returns:
            None
        """
        self.overdraftLimit = initialOverdraft
        self.overdraft = True
        print(self.overdraftLimit)

    #Ensuring default string is available
    def __str__(self):
        """
        Default string function, returns the name, balance and, overdraft status and overdraft limit.
        Parameters:
            None
        Returns:
            str - name - Name of the account
            float - balance - balance of the account
            bool - overdraft - if the account has an overdraft or not
        """
        return '{self.name}, \n {self.balance}, \n {self.overdraft}, \n {self.overdraftLimit}'.format(self=self)

    #A function to set an overdraft limit
    def setOverdraftLimit(self, newLimit):
        """
        This function sets a new overdraft limit. First it checks that the new limit
        is NOT a negative integer, as this would have a knock on effect setting the
        availableBalance to the wrong number, essentially withdrawing money. e.g.
        Balance: 500
        New overdraft limit: -600
        available balance = 500 + - 600
        available balance = -100
        Thus breaking the account. This check is necessary.
        Within this first check is a second, if the new limit is 0, it sets the
        value of overdraft to False as there is no longer an overdraft.

        If the newLimit is greater than 0 it then checks that the new limit < balance.
        This is so that I cannot withdraw to -100 then set a limit of -10, breaking the system.
        If this check is passed then it sets the new overdraft limit to the newlimit and 
        sets overdraft to true.
        Parameters:
            float - newLimit
        Returns:
            None
        
        """
        if newLimit > 0:
            if newLimit == 0:
                self.overdraft = False
            elif -abs(newLimit) < self.balance:
                self.overdraft = True
                self.overdraftLimit = newLimit
            else:
                exit
        else:
            exit
        
    #Available balance specifically for premium accounts
    def getAvailableBalance(self):
        """
        This function takes the balance and the overdraftLimit and will give a total
        available balance.
        Parameters:
            None
        Returns:
            float - availableBalance - The total available balance including any overdraft
        """
        availableBalance = self.balance + self.overdraftLimit
        return availableBalance

    #print balance specifically for premium accounts
    def printBalance(self):
        """
        This function will get the balance and tell the user how much money is left
        in the overdraft.
        The conditional block checks what the remainingOverdraft variable will be set to.
        If the balance is in the negative it will calculate the remaining, otherwise
        it will just state the current overdraft limit.
        Parameters:
            None
        Returns:
            None
        """
        print(self.balance)
        if self.balance < 0:
            remainingOverdraft = self.overdraftLimit + self.balance
        elif self.balance > 0:
            remainingOverdraft = self.overdraftLimit 
        print("There is £", remainingOverdraft, " left in the overdraft.")

    #close account specifically for premium account
    def closeAccount(self):
        """
        This function closes the premium account, if there is an overdrawn account
        it will not close. Otherwise it resets everything else.
        Parameters:
            None
        Returns:
            Bool - True - account closed = true
        """
        if self.balance < 0:
            print("Can not close account due to customer being overdrawn by £", self.balance)
            return False
        else:
            self.withdraw(self.balance)
            self.balance = 0
            self.name = ""
            self.cardExp = (0,0)
            self.acNum = ""
            self.availableBalance = 0
            self.overdraftLimit = 0
            self.overdraft = False
            self.cardNum = 0
        return True


if __name__ == "__main__":
    b1 = BasicAccount("Chris", 200.0)
    b1.deposit(-500)
    print(b1.getAvailableBalance())
    b1.withdraw(500)
    b1.withdraw(-500)
    print(b1.getAvailableBalance())
    print(b1.getAcNum())
    print(b1.cardNum)
    print(b1.cardNum)
    print(b1.cardNum)

    print("\n\n\n")
    b2 = PremiumAccount("James Smith", 200.0, 200.0)
    print(b2.getAcNum())
    b2.withdraw(50)
    b2.withdraw(50)
    b2.withdraw(50)
    b2.withdraw(50)
    b2.withdraw(50)
    b2.printBalance()
    print(b2.getAvailableBalance())
    b2.setOverdraftLimit(10)
    print(b2.deposit(250))
    b2.withdraw(400)
    b2.setOverdraftLimit(10)
    print(b2.getAvailableBalance())
    b2.setOverdraftLimit(-500)
    print(b2.getAvailableBalance())
    b2.deposit(150.0)
    b2.printBalance()
    b2.deposit(100.0)
    b2.printBalance()
    b2.closeAccount()
    b1.closeAccount()

