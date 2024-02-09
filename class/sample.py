class MyClass:
    def __init__(self, value1):
        self.attribute = value1

    def method(self):
        return "何らかの処理"


my_instance = MyClass(value1="値")
print(my_instance.attribute)  # "値" を出力
print(my_instance.method())   # "何らかの処理" を出力
