class ParentCounter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        print(f"Parent's count: {cls.count}")

    @staticmethod
    def increment_static():
        ParentCounter.count += 1
        print(f"Parent's static count: {ParentCounter.count}")

class ChildCounter(ParentCounter):
    count = 100

ChildCounter.increment()      # 输出: Parent's count: 101 (操作的是 ChildCounter 的 count)
ParentCounter.increment()      # 输出: Parent's count: 1

ChildCounter.increment_static() # 输出: Parent's static count: 2 (始终操作的是 ParentCounter 的 count)
ParentCounter.increment_static() # 输出: Parent's static count: 3