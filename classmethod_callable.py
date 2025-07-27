class Calculator:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def add(x, y):
        Calculator.increment_count()  # staticmethod 需要用类名
        return x + y

    @classmethod
    def add_and_log(cls, x, y):
        cls.increment_count()       # classmethod 可以用 cls
        result = cls.add(x, y)      # classmethod 可以用 cls 调用 staticmethod
        print(f"Added {x} and {y}, result: {result}")
        return result

Calculator.add_and_log(5, 3)