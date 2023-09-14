class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化方法
    init_flag = False

    # # 重写new方法，在创建对象时，new方法会被自动调用
    # def __new__(cls, *args, **kwargs):
    #     print("创建对象")
    #     # 为对象分配空间
    #     instance = super().__new__(cls)
    #     # 返回对象的引用
    #     return instance

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:

            cls.instance = super().__new__(cls)

        return cls.instance

    # 让初始化只被执行一次
    def __init__(self):
        if not MusicPlayer.init_flag:
            print("播放器初始化")
            MusicPlayer.init_flag = True
        return


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

