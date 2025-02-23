import user
import user_manager
import group
import group_manager
import config_handler

csv_input_path = config_handler.import_csv_input_path()
csv_output_path = config_handler.import_csv_output_path()


def main():
    p1 = user.User("Kai", "1234", 1, "SHA", "AES")
    p2 = user.User("Jayvee", "4567", 2, "MD5", "DES")
    p3 = user.User("Jev", "bossing", 3, "SHA", "DES")

    manager = user_manager.UserManager()
    manager.display_users()
    print()

    manager.add_user(p1)
    manager.add_user(p2)
    manager.add_user(p3)
    manager.display_users()
    print()

    print(manager.get_user(2))
    print()
    manager.delete_user(3)
    manager.display_users()

    print()
    manager.reset_user(1)
    print(p1.user_password)
    p1.change_password("newPassword!")
    print(p1.user_password)

    manager.lock_user(2)
    manager.disable_user(1)
    manager.display_users()

    p3 = user.User("Jev2", "bossing", 3, "SHA", "DES")
    print()
    g1 = group.Group("CSS", "Admin")
    g1.add_user_to_group(p1)
    g2 = group.Group("HR", "Member")
    g2.add_user_to_group(p2)
    g2.add_user_to_group(p3)

    gr_manager = group_manager.GroupManager()
    gr_manager.add_group(g1)
    gr_manager.add_group(g2)
    gr_manager.display_groups()
    gr_manager.display_group_members("CSS")

    manager.save_users_to_csv(csv_output_path, gr_manager)

    print()
    manager.load_users_from_csv(csv_input_path)
    manager.display_users()


if __name__ == "__main__":
    main()
