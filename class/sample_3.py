class MyClass:
    def __init__(self):
        self.__private_method()

    def __private_method(self):
        print("これはプライベートメソッドです")


# クラスの外部からプライベートメソッドにアクセスしようとするとエラーになる
instance = MyClass()
try:
    instance.__private_method()
except AttributeError as e:
    print(e)  # 'MyClass' object has no attribute '__private_method'

# 名前マングリングに従ってアクセス
instance._MyClass__private_method()
