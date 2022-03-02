import collections

list_of_words = ['hi', 'there', 'hi', 'hello', 'hi']

word_counts = collections.Counter(list_of_words)

print(word_counts)