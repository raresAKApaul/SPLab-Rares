class Element:
    def __init__(self, name):
        self.name = name
        self._parent = None
        self.children = []

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def add(self, element):
        self.children.append(element)
        element.set_parent(self)

    def remove(self, element):
        self.children.remove(element)


class Section(Element):
    def __init__(self, title):
        super().__init__(title)


class TableOfContents(Element):
    def __init__(self, content):
        super().__init__(content)


class AlignmentStrategy:
    def align(self, text):
        pass


class LeftAlign(AlignmentStrategy):
    def align(self, text):
        return f"{text}"


class RightAlign(AlignmentStrategy):
    def align(self, text):
        return f"{text.rjust(len(text) + 4)}"


class Paragraph(Element):
    def __init__(self, text, alignment_strategy=None):
        super().__init__(text)
        self.text = None
        self.alignment_strategy = alignment_strategy or LeftAlign()

    def set_alignment_strategy(self, alignment_strategy):
        self.alignment_strategy = alignment_strategy

    def render(self):
        aligned_text = self.alignment_strategy.align(self.text)
        # Other rendering logic
        return f"<p>{aligned_text}</p>"


class Picture:
    def __init__(self, url):
        self.url = url

    def getsize(self, dim=None):
        return dim

    def getcontent(self, content=None):
        return content

    def display(self):
        pass


class Image(Element):
    def __init__(self, url):
        super().__init__(url)

    def display(self):
        print(self)


class ImageProxy(Picture):
    def __init__(self, url):
        self.url = super().__init__(url)
        self.content = super().getcontent()

    def loadImage(self):
        if self.url is not None:
            self.url = Image(self.url)
        super().display()


class Author:
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print("Author:", self.name)


class Book:
    def __init__(self, name: str):
        self.name = name
        self.authors = []
        self.content = []

    def add_author(self, author: Author):
        self.authors.append(author)

    def add_content(self, element: Element):
        self.content.append(element)

    def print(self):
        print("Name:", self.name)
        print("Authors:")
        for a in self.authors:
            a.print()


if __name__ == '__main__':
    book = Book("carte")
    a1 = Author("autor 1")
    a2 = Author("autor 2")
    book.add_author(a1)
    book.add_author(a2)
    book.print()
