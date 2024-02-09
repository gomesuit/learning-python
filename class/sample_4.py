class MyClass:
    def repeat(self, value: str, times: int) -> str:
        """指定された文字列を指定された回数繰り返す"""
        return value * times


# クラスのインスタンスを作成
my_instance = MyClass()

# repeatメソッドを呼び出し
result = my_instance.repeat(value="Python", times=3)

# 結果を表示
print(result)  # 出力: PythonPythonPython
