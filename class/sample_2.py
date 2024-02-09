class MyClass:
    class_variable = "これはクラス変数です"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


# クラス変数にアクセス
print(MyClass.class_variable)  # "これはクラス変数です"

# インスタンスを生成して、クラス変数にアクセス
instance1 = MyClass("インスタンス変数1")
instance2 = MyClass("インスタンス変数2")

print(instance1.class_variable)  # "これはクラス変数です"
print(instance2.class_variable)  # "これはクラス変数です"

# クラス変数を変更
MyClass.class_variable = "新しいクラス変数の値"

# 変更後のクラス変数の値を表示
print(instance1.class_variable)  # "新しいクラス変数の値"
print(instance2.class_variable)  # "新しいクラス変数の値"
