The purpose of this project is to show the ability to appropriately use classes and OOP. A basic bank account can be created
without the ability to go into an overdraft, whilst a premium account allows you to go into an overdraft.

Functions:
1) Deposit -> input a deposit amount
2) withdraw -> input a withdrawal amount. If larger than balance for a basic account the program lets the customer know this amount cannot be withdrawn and displays current balance.
	For premium account is allows user to dip into the negative as long as its not more than the withdrawal limit.
3) getAvailableBalance -> returns the current available balance
4) getBalance -> returns balance with the potential for a negative balance
5) printBalance -> displays the balance
6) getName -> returns the name of the account holder 
7) getAcNum -> returns the account number
8) IssueNewCard -> issues a new card
9) closeAccount -> for basic accounts withdraws the whole remaining balance and closes the account. For premium account if first evaluates if the account is in overdraft. If not, the 
	balance is withdrawn and then closed. If not, the system informs them that they cannot close the account as they are £X in debt.
10) setOverdraftLimit -> for premium accounts sets the maximum allowed overdraw

