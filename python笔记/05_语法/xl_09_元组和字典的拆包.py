def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "xx"}
demo(gl_nums, gl_dict)

# 拆包语法，把gl_nums传入args,把dict传入kwargs
demo(*gl_nums, **gl_dict)

demo(1, 3, name="明")
