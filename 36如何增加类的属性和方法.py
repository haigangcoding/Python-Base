
# 定义一个类
class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        # 定义一个方法
    def print_role(self):
        print('%s: %s' %(self.name, self.hp))

class Monster():
    # 定义