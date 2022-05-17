class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        while True:
            self.name = input('Please give us a new name: ').strip()
            if len(self.name) < 2 or len(self.name) > 10:
                print("Error! Name has to be between 2 or 10 characters long.")
            elif ' ' in self.name:
                print("Error! Name cannot contain spaces!")
            else:
                print(f'Name successfully updated to {self.name}')
                break

    def change_pin(self):
        while True:
            self.pin = input('Please give us a new pin: ')
            if len(self.pin) != 4:
                print('Error! Pin can only be 4 characters long!')
            elif ' ' in self.pin:
                print("Error! Pin cannot contain spaces!")
            else:
                print(f'PIN successfully updated!')
                break

    def change_password(self):
        while True:
            self.password = input('Please give us a new password: ')
            if len(self.password) < 5:
                print('Error! Password cannot be less than 5 characters long!')
            elif ' ' in self.password:
                print("Error! Password cannot contain spaces!")
            else:
                print(f'Password successfully updated!')
                break


class BankUser(User):
    def __init__(self, name, pin, password, balance=0.00):
        super().__init__(name, pin, password)
        self.balance = balance
        self.on_hold = False

    def place_hold(self):
        self.on_hold = True

    def check_for_holds(self):
        if self.on_hold == True:
            print(f'{self.name} has a hold on their account, and cannot perform any transations. Please call 555-555-5555 to remove the hold.')
            return True
        else:
            return False

    def show_balance(self):
        print(f"Your current balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        self.balance -= amount

    def withdraw_workflow(self):
        if self.check_for_holds():
            return None
        while True:
            try:
                amount = float(input(
                    f'How much would you like to withdraw?\nDollar Amount: '))
            except ValueError:
                print("You can only use numbers.")
            else:
                if amount <= 0:
                    print("You need to give a positive dollar amount.")
                else:
                    break
        self.withdraw(amount)

    def deposit(self, amount):
        self.balance += amount

    def deposit_workflow(self):
        if self.check_for_holds():
            return None
        while True:
            try:
                amount = float(input(
                    f'How much would you like to deposit?\nDollar Amount: '))
            except ValueError:
                print("You can only use numbers.")
            else:
                if amount <= 0:
                    print("You need to give a positive dollar amount.")
                else:
                    break
        self.deposit(amount)

    def transfer_money(self, receiving_user):
        self.check_for_holds()
        receiving_user.check_for_holds()
        while True:
            try:
                transfer_amount = float(input(
                    f'How much would you like to transfer to {receiving_user.name}\nDollar Amount: '))
            except ValueError:
                print("You have to give a number to transfer.")
            else:
                if transfer_amount <= 0:
                    print("You need to give a positive dollar amount.")
                else:
                    break

        if self.balance < transfer_amount:
            print(
                f'Error! {self.name} does not have the funds to complete this transfer! Canceling Transfer request.')
            return None
        print(
            f'{self.name} is trying to transfer ${transfer_amount:.2f} to {receiving_user.name}')
        pin_check = input(f"Please enter the pin for {self.name}: ")
        if pin_check == self.pin:
            receiving_user.deposit(transfer_amount)
            self.withdraw(transfer_amount)
            print(
                f"Transfer Authorized\nTransferring ${transfer_amount}\n{self.name} has a new balance of ${self.balance:.2f}\n{receiving_user.name} has a new balance of ${receiving_user.balance:.2f}")
            return True
        else:
            print(
                f"PIN is invalid. Transaction canceled.\n{self.name} has a balance of ${self.balance:.2f}\n{receiving_user.name} has a balance of ${receiving_user.balance:.2f}")
            return False

    def request_money(self, sending_user):
        self.check_for_holds()
        sending_user.check_for_holds()
        while True:
            try:
                transfer_amount = int(input(
                    f'How much would you like to request from {sending_user.name}\nDollar Amount: '))
            except ValueError:
                print("You have to give a number to transfer.")
            else:
                if transfer_amount <= 0:
                    print("You need to give a positive dollar amount.")
                else:
                    break
        if sending_user.balance < transfer_amount:
            print(
                f'Error! {sending_user.name} does not have the funds to complete this transfer')
            return None
        print(
            f'{self.name} is requesting ${transfer_amount} from {sending_user.name}')
        pin_check = input(f"Please enter the PIN for {sending_user.name}: ")
        password_check = input(
            f"Please enter the password for {self.name}: ")
        if pin_check == sending_user.pin and password_check == self.password:
            self.deposit(transfer_amount)
            sending_user.withdraw(transfer_amount)
            print(
                f"Transfer Authorized. . .\nTransferring ${transfer_amount}\n{sending_user.name} has a new balance of ${sending_user.balance}\n{self.name} has a new balance of ${self.balance}")
            return True
        else:
            print(
                f"You have entered an invalid PIN or Password. Transaction canceled.\n{sending_user.name} has a balance of ${sending_user.balance}\n{self.name} has a balance of ${self.balance}")
            return False

# Driver Code
# user1 = User("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password)
# user1 = BankUser("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name()
# user1.change_pin()
# user1.change_password()
# print(user1.name, user1.pin, user1.password)

# Driver Code
# user1 = BankUser("Bob", "1234", "password", 0)
# print(user1.name, user1.pin, user1.password, user1.balance, user1.on_hold)
# user1.check_for_holds()
# user1.show_balance()
# user1.deposit_workflow()
# user1.show_balance()
# user1.withdraw_workflow()
# user1.show_balance()

# Driver Code
# user1 = BankUser("Bob", "1234", "password")
# user2 = BankUser("Alice", "9999", "lastpass", 400)
# user2.transfer_money(user1)
# print(user1.name, user1.balance, user2.name, user2.balance)
# user2.request_money(user1)
# print(user1.name, user1.balance, user2.name, user2.balance)
