import unittest
from _01_classes import BankAccount

# filepath: test_01_classes.py

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Set up test accounts before each test method"""
        self.account1 = BankAccount("John Doe", 1000.0)
        self.account2 = BankAccount("Jane Smith", 500.0)

    def test_initialization(self):
        """Test account initialization"""
        self.assertEqual(self.account1.owner, "John Doe")
        self.assertEqual(self.account1.balance, 1000.0)
        self.assertEqual(len(self.account1.transactions), 0)
        
        # Test default balance
        default_account = BankAccount("Bob Smith")
        self.assertEqual(default_account.balance, 0.0)

    def test_deposit(self):
        """Test deposit functionality"""
        initial_balance = self.account1.balance
        deposit_amount = 500.0
        self.account1.deposit(deposit_amount)
        
        self.assertEqual(self.account1.balance, initial_balance + deposit_amount)
        self.assertEqual(len(self.account1.transactions), 1)
        self.assertEqual(self.account1.transactions[0][1], f"Deposited {deposit_amount}")

    def test_withdraw_sufficient_funds(self):
        """Test withdrawal with sufficient funds"""
        initial_balance = self.account1.balance
        withdrawal_amount = 500.0
        self.account1.withdraw(withdrawal_amount)
        
        self.assertEqual(self.account1.balance, initial_balance - withdrawal_amount)
        self.assertEqual(len(self.account1.transactions), 1)
        self.assertEqual(self.account1.transactions[0][1], f"Withdrawn {withdrawal_amount}")

    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds"""
        initial_balance = self.account1.balance
        withdrawal_amount = 1500.0
        self.account1.withdraw(withdrawal_amount)
        
        # Balance should remain unchanged
        self.assertEqual(self.account1.balance, initial_balance)
        self.assertEqual(len(self.account1.transactions), 0)

    def test_get_balance(self):
        """Test balance retrieval"""
        self.assertEqual(self.account1.get_balance(), 1000.0)

    def test_valid_transfer(self):
        """Test valid transfer between accounts"""
        initial_balance1 = self.account1.balance
        initial_balance2 = self.account2.balance
        transfer_amount = 300.0
        
        self.account1.transfer(transfer_amount, self.account2)
        
        self.assertEqual(self.account1.balance, initial_balance1 - transfer_amount)
        self.assertEqual(self.account2.balance, initial_balance2 + transfer_amount)
        self.assertEqual(len(self.account1.transactions), 1)
        self.assertEqual(len(self.account2.transactions), 1)

    def test_invalid_transfer_amount(self):
        """Test transfer with invalid amount"""
        initial_balance1 = self.account1.balance
        initial_balance2 = self.account2.balance
        
        self.account1.transfer(-100, self.account2)
        
        self.assertEqual(self.account1.balance, initial_balance1)
        self.assertEqual(self.account2.balance, initial_balance2)
        self.assertEqual(len(self.account1.transactions), 0)
        self.assertEqual(len(self.account2.transactions), 0)

    def test_transfer_insufficient_funds(self):
        """Test transfer with insufficient funds"""
        initial_balance1 = self.account1.balance
        initial_balance2 = self.account2.balance
        
        self.account1.transfer(2000, self.account2)
        
        self.assertEqual(self.account1.balance, initial_balance1)
        self.assertEqual(self.account2.balance, initial_balance2)
        self.assertEqual(len(self.account1.transactions), 0)
        self.assertEqual(len(self.account2.transactions), 0)

    def test_invalid_target_account(self):
        """Test transfer to invalid account"""
        initial_balance = self.account1.balance
        
        self.account1.transfer(500, "not_an_account")
        
        self.assertEqual(self.account1.balance, initial_balance)
        self.assertEqual(len(self.account1.transactions), 0)

if __name__ == '__main__':
    unittest.main()