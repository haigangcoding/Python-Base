
# ����һ����
class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        # ����һ������
    def print_role(self):
        print('%s: %s' %(self.name, self.hp))

class Monster():
    # ����