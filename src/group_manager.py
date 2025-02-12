"""This module contains the GroupManager Class"""


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
