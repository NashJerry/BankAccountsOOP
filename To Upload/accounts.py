#the random module will be used when assigning the card number
#the date time module will be used to generate the time
import random
import datetime


class BasicAccount:
    
    '''
    This is the superclass to which both basic and premuim accounts will exist.
    It will have limited functionality, such as having no access to overDrafts
    
    '''
    #A bank would naturally look to store the details of their client’s accounts.
    #A dictionary would be the best way to do this
    #the static variable initial account number is zero and this will be incremented each time a new account is created
    accounts = {}
    accountNumber = 0    

    def __init__(self, theName, theBalance): 
        self.name = theName
        self.balance = theBalance
        #self.acNum assigns the account number
        self.acNum = BasicAccount.accountNumber + 1
        #after account number is assigned, it can be incremented by one to prevent repitition
        BasicAccount.accountNumber += 1
        #card number initially empty as an account without a card is possible. It can then be assigned later.
        self.cardNum = ''
        #Basic accounts will never have an overdraft so will return false. As a result overdraft variables not needed here.
        self.overDraft = False
        #the card details self.cardExp and self.validFrom will return date values of month and year represented in integer form
        self.cardExp = ()
        self.validFrom = ()

        #This then allows us to add accounts by accounts number into the "accounts" dictionary
        BasicAccount.accounts[self.acNum] = self


    def deposit(self,depAmount):
        """
        Allows customers to deposit a float amount of money into their account.
        The amount should be positive to allow money to be added to their balance. 
        If it is negative an informative message will be printed.
        
        Parameters:
            depAmount: float - the amount of money the customer wishes to deposit
        Returns:
            Nothing
        """
        if float(depAmount) >= 0:
            self.balance += float(depAmount)
        else:
            print("You have to deposit a positive amount. You tried to deposit: £", depAmount)


    def withdraw(self, theWithdrawl):
        '''
        Allows customers to withdraw money from their bank account and adjust their balance. 
        No overdrafts allowed for a basic account, so the withdrawal amount must be less than the balance

        Parameters:
            theWithdrawl: float - the amount of money the customer wishes to withdraw
        Returns:
            Nothing

        '''
        if float(theWithdrawl) <= self.balance:
            self.balance -= float(theWithdrawl)
            print(self.name, "has withdrawn", theWithdrawl, "\n New balance is: £", self.balance)
        else:
            float(theWithdrawl) > self.balance
            print("Cannot withdraw £", theWithdrawl, " as it more than your current balance.")


    def getAvailableBalance(self):
        '''
        Gets the customer's current balance.

        Parameters:
            None
        Returns:
            self.balance       
        '''
        return self.balance

    def getBalance(self):
        ''''
        Returns the customers current balance. If the account is overdrawn a negative number is withdrawn.

        Parameters:
            None
        Returns:
            self.balance       

        '''

        return self.balance

    def printBalance(self):
        '''
        prints the customer's current balance.

        Parameters:
            None
        Returns:
            The customer's balance and any overdraft available (always £0 for Basic Accounts.)  

        '''
        print("Current Balance : £", self.balance, "\nOverdraft Available: £0")

    def getName(self):
        '''
        Gets the account name and returns it as a string

        Parameters:
            None
        Returns:
            self.name 

        '''
        return self.name
        

    def getAcNum(self):
        '''
        Returns the accounts number as a string
        Parameters:
            None
        Returns:
            account number as a string        
        '''
        return str(self.acNum)

    def issueNewCard(self):
        '''
        Issues the customer a new card with a unique number
        Parameters:
            None
        Returns:
            Card Number (str). Valid from (int) and Expiry date of the card (int)         

        '''

        cardNumber = ''
        IssueDate = datetime.datetime.now()
        #only the month and year are needed for validity and they are both stored as ints in a tuple
        self.validFrom = (int(IssueDate.month), int(str(IssueDate.year)[-2:]))
        #three years (in days) are added to the validity of the card. Also stored in a tuple
        expiryDate = IssueDate + datetime.timedelta(days=1095)
        self.cardExp = (int(expiryDate.month), int(str(expiryDate.year)[-2:]))
        #the 16 digit card number is randomly assigned
        cardNumber = random.randint(1000000000000000,9999999999999999)    
        return print("Card Number: ", cardNumber, "\nValid From: ", self.validFrom, "\nExpiry Date:", self.cardExp)

    def __str__(self):
        '''
        Displays the account details for when an account is called.

        Parameters:
            None
        Returns:
            Account Number, name as well as their available balance and overdraft details as strings.
        '''
        return "\nBasic Account Number   : " + str(self.acNum) + \
                "\nAcc Surname  : " + self.name + \
                "\nAvailable Balance: £" + str(self.getAvailableBalance())+ \
                "\nOverdraft Balance: £" + str(0)


    def closeAccount(self):
        '''
        closes the account and withdraws the customer's remaining balance.
        (In our case doesn't actually delete the account)

        Parameters:
            None
        Returns:
            self.withdraw(Self.balance) i.e. the remaining balance
            Also returns True as the always positive balance means an account can always be closed
        '''
        self.withdraw(self.balance)
        return True


class PremiumAccount(BasicAccount):
    '''
    Premium Accounts are basic accounts except with the possibility to overdraw
    to varying amounts.
    '''


    def __init__(self, theName, theBalance, initialOverdraft):
        '''
        The same functionality as the Basic account but initialOverDraft is the amount by which
        the customer can overdraw their account

        Parameters:
            theName: string, theBalance : string, initialOverdraft : float
        Returns:
            None        
        '''
        super().__init__(theName, theBalance)
        #initialOverdraft being a required parametre means premium account holder will always have an onverdraft available so 'True' 
        self.overDraft = True
        #the set overDraft limit
        self.overdraftLimit =  initialOverdraft
        #how much money is still left in their overdraft
        self.overDraftBalance = initialOverdraft

    def setOverdraftLimit(self, theLimit):
        '''
        Allows the  bank to alter how much overdraft the customer can have.

        Parameters:
            theLimit : float
        
        Returns:
            None  
    
        '''
        self.overDraft = True
        self.overDraftBalance = theLimit


    def withdraw(self, theWithdrawl):
        '''
        allows customers to withdraw money from their balance and potentially from their overdraft balance

        Parameters:
            theWithdrawl : float
        Returns:
            self. balance after the withdrawl          
        '''
        #if the withdrawal is smaller than the balance, directly withdraw the balance
        if float(theWithdrawl) < self.balance:
            self.balance -= float(theWithdrawl)
            print(self.name, "has withdrawn £", theWithdrawl, ".\nNew balance amount is: £", self.balance)

            #but if the withdrawl is within the range of the balance + overDraft, the withdrawl should be allowed. The overdraft balance should be suitably adjusted
        elif float(theWithdrawl) > self.balance and float(theWithdrawl) < self.balance + self.overDraftBalance:
            self.balance = self.balance - theWithdrawl 
            self.overDraftBalance = self.overDraftBalance +  self.balance
            print(self.name, "has with drawn £", float(theWithdrawl), "\nNew Balance including overdraft is: £", self.overDraftBalance)
            
        #if the requested withdrawl is bigger than the balance and overdraft balance, the withdrawl is denied and the program exits
        elif float(theWithdrawl) > self.balance + self.overDraftBalance:
            print("Cannot withdraw £", theWithdrawl)
        return self.balance

    def getAvailableBalance(self):

        '''
        Gets the customers current balance while factoring in the overdraft.

        Parameters:
            None
        Returns:
            self.maxAvailable       
        '''        
        #the self.maxAvaiable combines the balance and the overdraft balance
        if self.balance > 0:
            self.maxAvailable = self.overDraftBalance + self.balance
        else:
            self.maxAvailable = self.overDraftBalance
        return self.maxAvailable

    def printBalance(self):
        '''
        prints the customer's current balance.

        Parameters:
            None
        Returns:
            The customer's balance and any overdraft available (always £0 for Basic Accounts.)  

        '''
        print("Current Balance : £", self.balance, "\nOverdraft Available: £", self.overDraftBalance)


    def __str__(self):

        return "Premium Account Number   : " + str(self.acNum) + \
            "\nAccount Name  : " + self.name + \
            "\nAvailable Balance: £" + str(self.getAvailableBalance())+ \
            "\nOverdraft Balance: £" + str(self.overDraftBalance)


    def closeAccount(self):
        if self.balance < 0:
            print("Cannot close account due to customer being overdraw by £", self.balance*-1)
            return False
        else:
            self.withdraw(self.getAvailableBalance())
            return True
