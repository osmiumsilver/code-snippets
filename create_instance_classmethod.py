class Document:
    def __init__(self, content):
        self.content = content

    @classmethod
    def from_string(cls, text):
        """一个工厂方法，从字符串创建 Document 实例"""
        return cls(text)

    @staticmethod
    def create_empty():
        """staticmethod 需要显式指定类名"""
        return Document("")

doc1 = Document.from_string("This is some text.")
doc2 = Document.create_empty()