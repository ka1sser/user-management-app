"""This module contains UserManager Class"""

import csv
from user import User


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

    def save_users_to_csv(self, filename, group_manager):
        """
        This function will save users to the csv

        Args:
            filename (str): Directory to output the csv file
            group_manager (class GroupManager): GroupManager class as an input
        """

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Writing the header
            writer.writerow(["Name", "ID", "Group"])

            # Loops through the users list
            for user in self.users:
                # Default value if user is not included in any group
                group_name = "None"
                # Loops through the group list
                for group in group_manager.group_list:
                    if user in group.members:
                        group_name = group.group_name
                        break

                writer.writerow([user.user_name, user.user_id, group_name])

    def load_users_from_csv(self, filename):
        """
        This function will load users from a csv file to the database

        Args:
            filename (str): Directory of the file where the users to be imported is located
        """
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Reads the data on the csv
                user = User(
                    row["Name"],
                    "default_password",
                    int(row["ID"]),
                    "auth_algo",
                    "priv_algo",
                )
                # Appends the user data to the users list
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
