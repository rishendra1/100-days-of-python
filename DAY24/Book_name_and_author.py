class BooK:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @classmethod
    def from_string(cls, string):
        title, author = string.split("-")
        return cls(title, author)
    def print_names(self):
        print(f"Title of the book: {self.title}")
        print(f"Author of the book: {self.author}")


s1 = BooK.from_string("Wings of fire - APJ Abdul Kalam")
print(s1.print_names())