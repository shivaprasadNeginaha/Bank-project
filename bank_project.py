class User:
    '''
    Parent class
    '''
    def __init__(self, name, age, gender):
        '''
        Initializing the variables using constructor
        '''
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        '''
        Function to show the detalis
        '''
        print("User details are as follows: name is {} and age is {} and gender is {}".format(
            self.name, self.age, self.gender))


class Bank(User):
    '''
    Child class, which is inherting the properties from User class
    '''
    def __init__(self, name, age, gender):
        '''
        Initializing the name age and gender of the user
        '''
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        '''
        Function for deposit the money to bank
        '''
        self.show_details()
        self.amount = amount
        self.balance = self.amount + self.balance
        print("your updated account balance is", self.balance)

    def withdraw(self, amount):
        '''
        Function for Witdraw money from bank
        '''
        self.amount = amount
        if self.amount > self.balance:
            print("Sorry you dont have sufficient balance. Your balance is", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("you have successfully widrawn the amount of RS", self.amount)

    def final_details(self):
        '''
        Function to display remaining balance in the account
        '''
        print("your remaining balance is", self.balance)


customer = Bank('shiva', '30', 'male')
customer.deposit(1000)
customer.withdraw(4555)
customer.final_details()
