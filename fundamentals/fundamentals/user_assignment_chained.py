class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
        return self
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
        return self

    def spend_points(self,amount):
        if amount > self.gold_card_points:
            print("Insufficient reward points.")
        else:
            self.gold_card_points -= amount
        return self




user_kurt = User("Kurt", "Clausen", "email@email.org", "31")
user_kurt.display_info().enroll().spend_points(50).display_info().enroll()
user_aubrey = User("Aubrey", "Clausen", "aubrey@email.com", "29")
user_christian = User("Christian", "Clausen", "christian@email.com", "70")
user_aubrey.enroll().spend_points(80).display_info()
user_christian.display_info().spend_points(40)


