"""This module contains the GroupManager Class"""

import csv


class GroupManager:
    """This class manages the groups"""

    def __init__(self):
        self.group_list = []

    def add_group(self, group):
        """
        This function adds the input group to the group_list

        Args:
            group (dict): Dictionary containing group details
        """
        self.group_list.append(group)

    def display_groups(self):
        """
        This function displays the groups in the group_list
        """
        for group in self.group_list:
            print(group.group_dict())

    def display_group_members(self, groupname):
        """
        This function displays the group members

        Args:
            groupname (str): Input should be a string for the group_name
        """
        for group in self.group_list:
            if group.group_name == groupname:
                group.display_members()

    def assign_users_to_groups_from_csv(self, filename, user_manager):
        """
        This function will assign users to their groups while loading the CSV

        Args:
            filename (str): Directory where the csv file is located
            user_manager (class UserManager): UserManager class to handle the users
        """
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Gets the group name
                group_name = row["Group"]
                if group_name != "None":
                    for group in self.group_list:
                        # Checks if group name is equal to the existing group names
                        if group.group_name == group_name:
                            user = next(
                                (
                                    u
                                    for u in user_manager.users
                                    if u.user_name == row["Name"]
                                ),
                                None,
                            )
                            if user:
                                group.add_user_to_group(user)
