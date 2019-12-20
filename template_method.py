from abc import ABC, abstractmethod
#This module provides the infrastructure for defining abstract base classes (ABCs) in Python


class AbstractUser(ABC):
    def template_registration(self):
        self.get_login()
        self.get_email()
        self.get_id()
        self.get_password()
        self.send_data()

    def get_login(self):
        print("Login is suitable!")

    def get_email(self):
        print("Email is suitable!")

    def get_password(self):
        print("Password is suitable!")

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def send_data(self):
        pass

class GeneralUser(AbstractUser):
    def get_id(self):
        pass

    def send_data(self):
        print("Data sent to users table!")

class Authority(AbstractUser):
    def get_id(self):
        print("Your ID is confirmed!")

    def send_data(self):
        print("Data sent to authority table!")

def do_registration(user: AbstractUser):
    user.template_registration()


do_registration(GeneralUser())
print("")
do_registration(Authority())
