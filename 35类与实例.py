# use1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s , hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(use1)

# 定义一个类
class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    # 定义一个方法
    def print_role(self):
        print('%s: %s' % (self.name, self.hp))

# 类的实例化
user1 = Player('tom', 100)
user2 = Player('jerry', 90)
user1.print_role()
user2.print_role()
