class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print("%s 玩家开始游戏" % self.player_name)

    @staticmethod
    def show_help():
        print("帮助信息")

    @classmethod
    def show_top_score(cls):
        print("历史最高分 %d" % cls.top_score)


Game.show_help()
Game.show_top_score()
xiaoMin = Game("小明")
xiaoMin.start_game()
