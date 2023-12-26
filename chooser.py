from collections import Counter

with open("words", "r") as f:
    words = f.read().splitlines()

words = list(filter(lambda w: len(w) == 5 and w.islower(), words))

chars = ''.join(words)

freq = Counter(chars)
max_freq = freq[max(freq, key=freq.get)]
freq = {k: (v / max_freq) - 1 for k, v in freq.items()}


word_dict = {}

for word in words:
    letter_dict = Counter(word)
    max_letter = max(letter_dict, key=letter_dict.get)
    word_dict[word] = len(''.join(set(word))) + freq[max_letter]

word_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1])}
print(word_dict)
