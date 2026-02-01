from user_manager import UserManager

manager = UserManager()

manager.add_user("Ali", "ali@mail.com", "Admin")
manager.add_user("Ayan", "ayan@mail.com", "User")

manager.update_user("ayan@mail.com", role="Admin")
manager.remove_user("ali@mail.com")
