# YYH 装饰器（decorator）详解
"""
装饰器：包过两个阶段， 函数的装饰和函数的调用
wraps用来装饰内部函数， 使得原函数对象的属性得以保留， 如：__name__，__doc__等

在装饰的过程中， 内部函数对象返回时，带着自身的属性一起返回，
没有wraps(func), 调用原函数就是在调用装饰器中的内部函数，其属性就是内部函数的属性
有wraps(func),表示wraps装饰了内部函数对象，将func带着自身属性返回修改了内部函数的引用和属性，即相当于a,b=b,a
"""
from functools import wraps, partial


# 基本形态
# 以引用的方式进行装饰
def decorator_name(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        f = func(*args, **kwargs)
        return f

    return decorated


@decorator_name
def decorated_func(a, b):
    print(a + b, locals())


# 带参数的装饰器
# 以调用的方式进行装饰， 因此，如果外出函数没有传递参数，那就和基本形态相差无几
def item_it():
    def decorator_n(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            f = func(*args, **kwargs)
            return f

        return decorated

    return decorator_n


def item_it_(auth="vip"):
    def decorator_n(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            print(auth, "Comparing user permissions on the current interface from the database!")
            f = func(*args, **kwargs)
            return f

        return decorated

    return decorator_n


@item_it_("normal")
def decorated_func_it(a, b):
    print(a + b, locals())


decorated_func(1, 2)

"""=================================================================="""


# 在类里面定义装饰器写法


class An:

    def decorator_name(*func_args):
        func = func_args[-1]

        @wraps(func)
        def decorated(*args, **kwargs):
            self = args[0]
            f = func(*args, **kwargs)
            return f

        return decorated

    # def item_it_(auth="vip"):
    #     """
    #         由此可见， 在类中定义的装饰器在装饰阶段不需要self, 但是会造成pycharm对第一个参数的误解
    #     """

    def item_it_(*args, **kwargs):
        """故带参数的装饰器在此对装饰器上的参数进行处理"""
        auth = kwargs["auth"]
        print(args, kwargs)

        def decorator_n(func):
            @wraps(func)
            def decorated(*args, **kwargs):
                """s"""
                print(auth, "Comparing user permissions on the current interface from the database!")
                print(args, kwargs, decorated.__name__)
                f = func(*args, **kwargs)
                return f

            return decorated

        return decorator_n

    @decorator_name
    @item_it_(auth="normal")
    def decorated_method(self, a, b, c=21):
        """sd"""
        print(a + b, self.decorated_method.__name__)


an = An()
an.decorated_method(1, 2, c=3)

"""=================================================================="""


# 类装饰器,
# 由./P2.py可知当实现__call__时就可以让类像函数一样调用，即：类名().()；
# 类的初始化就相当于装饰器装饰函数的过程，类对象的调用就相当于函数的调用过程， 因此实现__call__, 就相当于在定义装饰器


class logit(object):
    def __init__(self, func):
        self.wrapped_func = func
        self.log_file = "log_name.log"

    def __call__(self, *args, **kwargs):
        rl = self.wrapped_func(*args, **kwargs)
        self.write_text(rl)
        return rl

    def write_text(self, content):
        print(content)


@logit
def decorated_function(*args, **kwargs):
    print(*args, **kwargs)
    return True


decorated_function(1, 2, 3)

"""=================================================================="""
# hy@functools.partial
# 通过__new__储存函数及其参数，__call__拓扑参数传递并调用储存的函数


def add(*args, **kwargs):
    # 打印位置参数
    for n in args:
        print(n)
    print("-"*20)
    # 打印关键字参数
    for k, v in kwargs.items():
        print('%s:%s' % (k, v))


add_partial = partial(add, 10, k1=10, k2=20)
add_partial(1, 2, 3, k3=20)

# hy@wraps
# wraps就是利用带参装饰器用法，使用functools模块中的partial函数修改装饰器中函数的命名空间属性
