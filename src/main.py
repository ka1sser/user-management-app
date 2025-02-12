import user
import user_manager


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
