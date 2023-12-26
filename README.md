# Wordle Board Game Chooser
### Running
`git clone https://github.com/IRawal/wordle-chooser`

`cd wordle-chooser`

`cp /usr/share/dict/words .`

`python3 chooser.py`

The output is a dictionary of every word with its associated
score, sorted from best to worst.
### Motivation
In the Wordle board game, one player is allowed to
choose the word that the other players guess. This script attempts
to pick the hardest words for people to guess
### General Strategy
We assume words are hard to guess based on two
criteria:
1. There are repeated letters
2. The letters are uncommon 

The first criterion ensures that to properly
determine letter positions, guessers must sacrifice
a place in their guess to try an already known letter
instead of a new one.
The second criterion ensures that many of the letters
used in the word are not found together in other words and
are thus difficult to initially find. This will also likely
result in non-trivial words. 
### Algorithm
For every word W and letter l:
1. Let L(w) return the number of distinct letters in the word
2. Let R(w) return the most repeated letter in the word
3. Let f(l) return the frequency of a letter in english

The word that minimizes L(w) + (f(R(w)) / max(f) - 1)
is optimal by the imposed assumptions.