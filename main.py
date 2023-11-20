class Book:
    def __init__(self, title):
        self.title = title
        self.authors = []
        self.chapters = []
        self.table_of_contents = "Table"

    def add_author(self, author):
        self.authors.append(author)

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def print(self):
        print("Title:", self.title)
        print("Authors:", self.authors)
        print("Table of contents: ", self.table_of_contents)
        print("Chapters: ", self.chapters)


class Chapter:
    def __init__(self, name):
        self.name = name
        self.subchapters = []

    def add_subchapter(self, subchapter):
        self.subchapters.append(subchapter)

    def print(self):
        print("Name of chapter:", self.name)
        print(self.subchapters)


class Subchapter:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def print(self):
        print("Name of subchapter:", self.name)
        print(self.elements)


class Element:
    def print(self):
        pass


class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name

    def print(self):
        print(self.image_name)


class Paragraph(Element):
    def __init__(self, text):
        self.text = text

    def print(self):
        print(self.text)


class Table(Element):
    def __init__(self, title):
        self.title = title

    def print(self):
        print(self.title)


class TableOfContents:
    def print(self):
        pass


class Author:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


if __name__ == '__main__':
    b1 = Book("Book 1")
    a1 = Author("Author1")
    c1 = Chapter("Chapter 1")
    c2 = Chapter("Chapter 2")
    b1.add_author(a1.name)
    b1.add_chapter(c1.name)
    b1.add_chapter(c2.name)
    sb1 = Subchapter("Sub 1")
    sb2 = Subchapter("Sub 2")
    c1.add_subchapter(sb1.name)
    c1.add_subchapter(sb2.name)
    c1.print()
    # b1.print()

    p1 = Paragraph("Paragraph 1")
    p2 = Paragraph("Paragraph 2")
    t1 = Table("Table 1")
    img1 = Image("Img 1")
    img2 = Image("Img 2")
    sb1.add_element(img1.image_name)
    sb1.add_element(img2.image_name)
    sb1.add_element(p1.text)
    sb1.add_element(p2.text)
    sb1.add_element(t1.title)
    sb1.print()
