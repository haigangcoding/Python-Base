
# ����һ����
class Player():
    def __init__(self, name, hp, occu):
        # ��������Ϊ����
        self.name = name
        self.hp = hp
        self.occu = occu

        # ����һ������
        def print_role(self):
            print('%s: %s %s' %(self.name, self.hp, self.occu))

        def updateName(self, newname):
            self.name = newname

    def print_role(self):
        print('%s: %s %s' % (self.name, self.hp, self.occu))

    def updateName(self, newname):
        self.name = newname


class Monster():
    # ���������
    pass


# ���ʵ����
user1 = Player('tom', 100, 'war')
user2 = Player('jerry', 90, 'master')
user1.print_role()
user2.print_role()

user1.updateName('wilson')
user1.print_role()
