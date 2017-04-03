import operator

import functions


def savebooks(books, name):
    sorteddata = sorted(books.items(), key=operator.itemgetter(1), reverse=True)
    functions.savescores(sorteddata, name)


def programmingbooks():
    savebooks("https://www.goodreads.com/shelf/show/programming", 'programmingbooks')


def generalbooks():
    mostread = functions.getBooks("https://www.goodreads.com/book/most_read?category=all&country=all&duration=y")
    morethanmillion = functions.getBooks("https://www.goodreads.com/list/show/35080.One_million_ratings_")
    all = {**morethanmillion, **mostread}
    savebooks(all, 'generalbooks')


def businessbooks():
    savebooks("https://www.goodreads.com/shelf/show/business", 'businessbooks')
