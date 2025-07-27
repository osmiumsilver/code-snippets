class Config:
    settings = {"debug": True}

    @classmethod
    def update_setting(cls, key, value):
        if key not in cls.settings:
            raise KeyError(f"Invalid key: {key}")
        print(f"Updating setting {key} to {value}")
        cls.settings[key] = value


c = Config()
c.settings = {"debug": False}
print(c.settings)


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, name_str):
        return cls(name_str.strip())

# 创建实例
p = Person.from_string(" Alice ")
print(p.name)  # 输出：Alice
