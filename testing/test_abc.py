#
# a=1
# for i in range(1,10):
#     a=a*i
#     print(a)
class A:
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls, e, f):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


b = A()
A.func1(1)
