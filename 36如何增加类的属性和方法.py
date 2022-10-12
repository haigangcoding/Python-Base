
# 定义一个类
class Player():
    def __init__(self, name, hp, occu):
        # 变量被称为属性
        self.name = name
        self.hp = hp
        self.occu = occu

        # 定义一个方法
        def print_role(self):
            print('%s: %s %s' %(self.name, self.hp, self.occu))

        def updateName(self, newname):
            self.name = newname

    def print_role(self):
        print('%s: %s %s' % (self.name, self.hp, self.occu))

    def updateName(self, newname):
        self.name = newname


class Monster():
    # ' 定义怪物类'
    pass


# 类的实例化
user1 = Player('tom', 100, 'war')
user2 = Player('jerry', 90, 'master')
user1.print_role()
user2.print_role()

user1.updateName('wilson')
user1.print_role()
