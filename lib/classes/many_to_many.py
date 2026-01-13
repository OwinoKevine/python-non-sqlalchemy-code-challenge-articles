class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        return list(set(a.magazine for a in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set(m.category for m in self.magazines()))


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
           self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
           self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        return list(set(a.author for a in self.articles()))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        result = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author is author])
            if count > 2:
                result.append(author)
        return result if result else None


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            return
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise Exception("Title must be 5–50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be Magazine")
        self._magazine = value