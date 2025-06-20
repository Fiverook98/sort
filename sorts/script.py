import utils # type: ignore
import sorts

bookshelf = utils.load_books('sorts/books_small.csv')

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']


sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)


def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

bookshelf_v1 = bookshelf.copy()

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf) - 1, by_author_ascending)

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

long_bookshelf = utils.load_books('sorts/books_large.csv')

#sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)