# 通过as给导入的模块起个别名，别名用大驼峰命名法
import xl_12_模块1 as DogModule

# 通过from。。import。。 从某个模块导入某个工具
# 可以直接使用工具，不需要模块名
# 如果从两个不同的模块中导入了 同名的函数 后导入的会覆盖前导入的
from xl_12_模块1 import Dog

# 导入一个模块所有工具
# 不推荐使用，如果覆盖其他函数，很难查找
from xl_12_模块1 import *

DogModule.say_hello()


# 导入工具后，不再需要模块名
dog = Dog("1")
dog.dark()

