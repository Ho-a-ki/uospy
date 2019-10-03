
def func(a):
    print("input number : ", a)


if __name__ == '__main__':
    #직접 실행되었을 때.
    print("direct access")
    func(3)
    func(4)


else:
    #모듈로서 import 되었을 때.
    print('import acesss')