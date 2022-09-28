
# 定义一个类
class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

        # 定义一个方法
    def print_role(self):
        print('%s: %s' %(self.name, self.hp))

class Monster():




# 类的实例化
user1 = Player('tom', 100)
user2 = Player('jerry', 90)
user1.print_role()
user2.print_role()
