import user
import user_manager


p1 = user.User("Kai", "1234", 1, "SHA", "AES")
p2 = user.User("Jayvee", "4567", 2, "MD5", "DES")
print(p1.to_dict())
print(p2.to_dict())

p1.disable()
p2.lock()
print()
print(p1.to_dict())
print(p2.to_dict())

print()
print(p1.user_password)
print(p2.user_password)
p1.change_password("hahaha")
p2.reset_user_pw()
print()
print(p1.user_password)
print(p2.user_password)
