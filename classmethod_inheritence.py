class ParentCounter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        print(f"{cls.__name__}'s count: {cls.count}")

    @staticmethod
    def increment_static():
        ParentCounter.count += 1
        print(f"ParentCounter's static count: {ParentCounter.count}")

class ChildCounter(ParentCounter):
    count = 100

ParentCounter.increment()  # 输出: ParentCounter's count: 1
ChildCounter.increment()   # 输出: ChildCounter's count: 101 (cls 绑定到 ChildCounter)

ParentCounter.increment_static() # 输出: ParentCounter's static count: 2
ChildCounter.increment_static()  # 输出: ParentCounter's static count: 3 (仍然操作 ParentCounter 的 count)