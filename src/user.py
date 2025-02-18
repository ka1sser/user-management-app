"""This module contains the User Class"""

import log_handler
import config_handler

log_path = config_handler.import_log_path()
logger = log_handler.initialize_logger(log_path, "user_mgmt", "file_logger")


class User:
    """This class handles all operations related to individual user"""

    def __init__(self, user_name, user_password, user_id, auth_algo, priv_algo):

        try:
            if not isinstance(user_name, str) or not user_name.strip():
                raise ValueError("User name must be a non-empty string")
            if not isinstance(user_password, str) or not user_password:
                raise ValueError("Password cannot be empty")
            if not isinstance(user_id, int) or user_id <= 0:
                raise ValueError("User ID must be a positive integer")
            if not isinstance(auth_algo, str) or not auth_algo.strip():
                raise ValueError("Authentication algorithm must be a non-empty string")
            if not isinstance(priv_algo, str) or not priv_algo.strip():
                raise ValueError("Privary algorithm must be a non-empty string")

            self.user_name = user_name
            self.user_password = user_password
            self.user_id = user_id
            self.auth_algo = auth_algo
            self.priv_algo = priv_algo
            self.status = "Enabled"
            self.permission = True

            logger.info(f"User {self.user_name} has been created!")

        except ValueError as e:
            logger.error(f"ValueError occured in User initialization: {e}")
            raise

        except TypeError as e:
            logger.error(f"TypeError occured in User initialization: {e}")
            raise

        except Exception as e:
            logger.error(f"An error occured in User initialization: {e}")
            raise

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

    def update_auth_algo(self, new_auth_algo):
        """
        This function updates the auth_algo of the user

        Args:
            new_auth_algo (str): New auth_algo to be assiged
        """
        self.auth_algo = new_auth_algo

    def update_priv_algo(self, new_priv_algo):
        """
        This function updates the priv_algo of the user

        Args:
            new_priv_algo (str): New priv_algo to be assiged
        """
        self.priv_algo = new_priv_algo
