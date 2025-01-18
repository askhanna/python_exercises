def interlock(word1, word2):
  """
  Checks if two words interlock.

  Args:
    word1: The first word.
    word2: The second word.

  Returns:
    True if the words interlock, False otherwise.
  """

  if len(word1) != len(word2):
    return False

  for i in range(len(word1)):
    if word1[i] != word2[i]:
      return False
  return True

def find_interlock_pairs(words):
  """
  Finds all pairs of words that interlock in a given list of words.

  Args:
    words: A list of words.

  Returns:
    A list of tuples, where each tuple contains a pair of interlocked words.
  """

  word_dict = {}
  for word in words:
    interlock_word = ''.join([word[i] for i in range(1, len(word), 2)])
    if interlock_word in word_dict:
      for other_word in word_dict[interlock_word]:
        yield (other_word, word)
    word_dict.setdefault(interlock_word, []).append(word)

# Example usage
words = ["shoe", "cold", "act", "gumbo", "hoop"]
for pair in find_interlock_pairs(words):
  print(pair)