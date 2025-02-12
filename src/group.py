"""This module contains the Group Class"""


class Group:
    """This class handles all operations related to individual group"""

    def __init__(self, group_name, group_category):
        self.group_name = group_name
        self.group_category = group_category
        self.members = []

    def group_dict(self):
        """
        This function creates a dictionary containing the group details

        Returns:
            dict: Returns a dictionary containing the group details
        """
        return {"Group": self.group_name, "Category": self.group_category}

    def add_user_to_group(self, user):
        """
        This function adds a user to the group instance calling the function

        Args:
            user (dict): Dictionary containing user details
        """
        self.members.append(user)

    def display_members(self):
        """
        This function displays the members present in the group.
        """
        print(f"{self.group_name} members:")
        for member in self.members:
            print(member.to_dict())
