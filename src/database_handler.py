import group
import group_manager
import user
import user_manager
import pandas as pd


def get_group_data():
    groups = group_manager.GroupManager().display_groups()
    print(groups)


get_group_data()
