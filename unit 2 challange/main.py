class bankaccount:
  def __init__(self,account_number,account_holder, initial_bankbalance=0.0):
     self.__account_number = account_number
     self.__account_holder = account_holder
     self.__account_balance = initial_bankbalance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("deposited ₹{}. New Balance:₹{}".format(amount,
                                                self.__account_balance))
    else:
      print("Invalid deposit amount.please deposit a positive amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdraw ₹{}. New Balance: ₹{}".format(amount,
                                                self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
        self.__account_holder, self.__account_number,
        self.__account_balance))





account = bankaccount(account_number=int(input("enter account no: ")),account_holder=input("enter the account holder name: "),initial_bankbalance=float(input("enter the balance amount in your account: ")))

account.display_balance()
account.deposit(4000.0)
account.withdraw(2000.0)
account.display_balance()
