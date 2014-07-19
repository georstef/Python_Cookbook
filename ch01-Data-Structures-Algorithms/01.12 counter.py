words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
    ]

from collections import Counter

# creates a dictionary like object with items as keys and counter as values
word_counts = Counter(words)
print(word_counts)

# get a list with the most common values
top_three = word_counts.most_common(3)
print(top_three)

# since word_counts is a dictionary like object
# we can add more words
morewords = ['why','are','you','not','looking','in','my','eyes']
# word_counts.update(morewords) # or use for loop ->
for word in morewords:
    word_counts[word] += 1
top_three = word_counts.most_common(3)
print(top_three)


# math operations with Counter objects
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
c = a - b
print(c)
