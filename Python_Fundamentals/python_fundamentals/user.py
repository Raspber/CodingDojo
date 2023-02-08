class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
    #1
    def display_info(self):
        print(self.first_name, self.last_name, self.last_name, self.email, self.is_reward_member, self.gold_card_points)

    def enroll(self):
        if self.is_reward_member != False:
            print('Already a member')
            return False
        self.is_reward_member = True
        if self.is_reward_member == True:
            self.gold_card_points = 200
        print(self.is_reward_member, self.gold_card_points)

    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print ('you do not have enough')
            return False
        self.gold_card_points -= amount

#1
new_user= User('Hauvert', 'Pacheco', 'dojo@gmail.com', 48)


new_user.display_info()
new_user.enroll().spend_points(25)

