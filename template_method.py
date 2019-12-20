from abc import ABC, abstractmethod
#This module provides the infrastructure for defining abstract base classes (ABCs) in Python


class AbstractUser(ABC):
    def template_registration(self) -> None:
        self.get_login()
        self.get_email()
        self.get_id()
        self.get_password()
        self.send_data()

    def get_login(self) -> None:
        print("Login is suitable!")

    def get_email(self) -> None:
        print("Email is suitable!")

    def get_password(self) -> None:
        print("Password is suitable!")

    @abstractmethod
    def get_id(self) -> None:
        pass

    @abstractmethod
    def send_data(self) -> None:
        pass

class GeneralUser(AbstractUser):
    def get_id(self) -> None:
        pass

    def send_data(self) -> None:
        print("Data sent to users table!")

class Authority(AbstractUser):
    def get_id(self) -> None:
        print("Your ID is confirmed!")

    def send_data(self) -> None:
        print("Data sent to authority table!")

def do_registration(user: AbstractUser):
    user.template_registration()


do_registration(GeneralUser())
print("")
do_registration(Authority())
