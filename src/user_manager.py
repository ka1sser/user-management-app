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

    def get_user(self, user_id):
        """
        This function retrieves the user containing the input user_id

        Args:
            user_id (int): Input should be an int containing the user_id
        """
        for user in self.users:
            if user.user_id == user_id:
                return user.to_dict()

    def delete_user(self, user_id):
        """
        This function deletes the user containing the user_id input

        Args:
            user_id (int): Input should be an int containing the user_id
        """

        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)

    def reset_user(self, user_id):
        """
        This function resets the user password to default

        Args:
            user_id (int): Input should be an int containing the user_id
        """
        for user in self.users:
            if user.user_id == user_id:
                user.reset()

    def lock_user(self, user_id):
        """
        This function changes the user's permission to locked in boolean False.

        Args:
            user_id (int): Input should be an int containing the user_id
        """
        for user in self.users:
            if user.user_id == user_id:
                user.lock()

    def unlock_user(self, user_id):
        """
        This function changes the user's permission to unlocked in boolean True.

        Args:
            user_id (int): Input should be an int containing the user_id
        """
        for user in self.users:
            if user.user_id == user_id:
                user.unlock()

    def enable_user(self, user_id):
        """
        This function changes the status of the user to "Enabled".

        Args:
            user_id (int): Input should be an int containing the user_id
        """
        for user in self.users:
            if user.user_id == user_id:
                user.enable()

    def disable_user(self, user_id):
        """
        This function changes the status of the user to "Disabled".

        Args:
            user_id (int): Input should be an int containing the user_id
        """
        for user in self.users:
            if user.user_id == user_id:
                user.disable()
