class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initializes a new instance of the class.

        Args:
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
            year (int): The manufacturing year of the vehicle.
        """
        self.make: str = make
        self.model: str = model
        self.year: int = year

    def describe(self) -> str:
        """
        Returns a string describing the car.

        Returns:
            str: A description of the car in the format 'Year Make Model'.
        """
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2021)


## Creating a bank account

class BankAccount:
    """
    A class to represent a bank account.
    Attributes:
        owner (str): The name of the account owner.
        balance (float): The current balance of the account. Defaults to 0.0.
        transactions (list): A list to store the transaction history.
        counter (int): A counter to track the number of transactions.
    Methods:
        deposit(amount):
            Adds the specified amount to the account balance and records the transaction.
        withdraw(amount):
            Deducts the specified amount from the account balance if sufficient funds are available.
            Records the transaction.
        get_balance():
            Returns the current balance of the account.
        get_transaction_history():
            Prints the transaction history of the account.
        transfer(amount, target_account):
            Transfers the specified amount to another BankAccount instance if sufficient funds are available.
            Records the transaction in both accounts.
    """
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.transactions: list = []
        self.balance: float = balance
        self.counter: int = 0

    def deposit(self, amount: float) -> None:
        # Add the amount to the balance
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        self.counter += 1
        # Record the transaction
        self.transactions.append((self.counter, f"Deposited {amount}"))

    def withdraw(self, amount: float) -> None:
        # Subtract the amount from the balance if there are sufficient funds
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            self.counter += 1
            # Record the transaction
            self.transactions.append((self.counter, f"Withdrawn {amount}"))
    
    def get_balance(self) -> float:
        return self.balance
    
    def get_transaction_history(self):
        print("\nTransaction History : ")
        for transaction in self.transactions:
            print(transaction)


    def transfer(self, amount: float, target_account: 'BankAccount') -> None:
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return
        if not isinstance(target_account, BankAccount):
            print("Invalid target account.")
            return
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append((self.counter + 1, f"Transferred {amount} to {target_account.owner}"))
            target_account.transactions.append((target_account.counter + 1, f"Received {amount} from {self.owner}"))
            self.counter += 1
            target_account.counter += 1
            print(f"Transferred {amount} to {target_account.owner}. New Balance is {self.balance}")
        else:
            print("Insufficient funds for transfer.")
        

# Create an instance and test the methods
account = BankAccount("John Doe", 1000.0)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # This should print a warning message
print(f"Current balance: {account.get_balance()}")
account.get_transaction_history()



# Create instances and test the transfer method
account1 = BankAccount("John Doe", 1000.0)
account2 = BankAccount("Jane Smith", 500.0)

account1.transfer(300, account2)
account1.get_transaction_history()
account2.get_transaction_history()