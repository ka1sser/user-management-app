"""This module contains the User Class"""


class User:
    """This class handles all operations related to individual user"""

    def __init__(self, user_name, user_password, user_id, auth_algo, priv_algo):

        self.user_name = user_name
        self.user_password = user_password
        self.user_id = user_id
        self.auth_algo = auth_algo
        self.priv_algo = priv_algo
        self.status = "Enabled"
        self.permission = True

    def to_dict(self):
        """
        This functions creates a dictionary of the user details

        Returns:
            (dict): Returns all the variables of user in form of a dictionary.
        """

        return {
            "Name": self.user_name,
            "ID": self.user_id,
            "Auth_Algo": self.auth_algo,
            "Priv_Algo": self.priv_algo,
            "Status": self.status,
            "Permission": self.permission,
        }

    def change_password(self, new_password):
        """
        This function changes the user password

        Args:
            new_password (str): New password input by user

        Returns:
            self.user_password (str): Returns the new password
        """
        self.user_password = new_password

        return self.user_password

    def enable(self):
        """
        This function changes the user status to "Enabled".

        Returns:
            self.status (str): Returns "Enabled" as a status.
        """
        self.status = "Enabled"

        return self.status

    def disable(self):
        """
        This function changes the user status to "Disabled".

        Returns:
            self.status (str): Returns "Disabled" as a status.
        """
        self.status = "Disabled"

        return self.status

    def lock(self):
        """
        This function changes the user permission to False.

        Returns:
            self.permission (bool): Returns a boolean value False
        """
        self.permission = False

        return self.permission

    def unlock(self):
        """
        This function changes the user permission to True.

        Returns:
            self.permission (bool): Returns a boolean value True
        """
        self.permission = True

        return self.permission

    def reset(self):
        """
        This function resets the user password to default value "123456"

        Returns:
            self.user_password: Returns the default password string "123456"
        """
        self.user_password = "123456"

        return self.user_password
