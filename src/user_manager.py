"""This module contains UserManager Class"""


class UserManager:
    """This class manages the users"""

    def __init__(self):
        self.users = []

    def add_user(self, user):
        """
        This function adds a user to the users list.

        Args:
            user (dict): user input is a dictionary container user details.
        """

        self.users.append(user)

    def display_users(self):
        """
        This function will display users in the users list using the .to_dict() function from
        User Class
        """

        for user in self.users:
            print(user.to_dict())
