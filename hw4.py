"""
======================================================================
Homework 4

Released: 2017-10-17
Due Date: 2017-10-24, EoD

They told me I could be anything...
...so I became void*.
======================================================================
"""

# is unique
def is_unique(word):
	"""
	Given a string, return true if the string's characters are unique.

	Args:
		(str) word: the input string.
	
	Returns:
		(bool) True if the string's characters are unique, False otherwise.
	"""
	listWord = list(word)
	for i in len(listWord) - 1 :
		if listWord[i] == listWord[i + 1] :
			return False
	return True

	print(is_unique('g'))

# Counting Anagrams
def count_anagrams(arr, uniq):
	"""
	Given a list of strings, returns the exact anagrams of uniq in the list.
	
	Args:
		(List[str]) arr:  a list of strings.
		(str)       uniq: a string.
	
	Returns:
		(int) the number of anagrams of uniq in arr.
	"""
	count = 0
	uniqList = list(unig)
	for i in len(arr) :
		if (len(uniq) == len(arr[i])) :
			arrList = list(arr[i])
			for i in len(arrList) :
				if uniqList[i] == arrList[j] :
					del arrList[j]
			if (len(arrList) == 0) :
				count += 1
	return count


# Anagram of Palindrome
def anagram_of_palindrome(word):
	"""
	Given a string, return true if the string is an anagram of a palindrome.

	Args:
		(str) word: the input string
	
	Returns:
		(bool) whether or not the input string is an anagram of a palindrome.
	"""
	NUM_CHARS = 256
	count = [0 for i in range(NUM_CHARS)]
	for i in len(word):
		count[ord(i)] += 1
	odd = 0
	for i in range(NO_OF_CHARS):
		if (count[i] & 1):
			odd += 1
		if (odd > 1):
			return False
		return True


# Reverse Dictionary
def reverse_dictionary(d):
	"""
	Given a dictionary d, reverse its keys and values.
	The values will all be unique.
	
	Args:
		(Dict[Any, Any]) d: the dictionary.

	Returns:
		(Dict[Any, Any]) a dictionary where the keys of d are its values and vice-versa. 
	"""
	pass


# Alphabet Finder
def alphabet_finder(sentence):
	"""
	Given a string, returns the shortest substring that:
		1. starts from the beginning of the string
		2. contains all the letters of the alphabet (case insensitive)
	If this is never true, return None.
	
	Args:
		(str) sentence: the input string

	Returns:
		(str) the shortest substring of sentence that satisfies both (1) and (2).
	"""
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m" "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	for i in range(len(sentence) - 1) :
		for j in range(len(letters)) :
			if (sentence[i : i + 1] == letters[j]) :
				del letters[j]
				break
			if (len(letters) == 0) :
				return sentence[0 : i + 1]
	return None
	
	print(alphabet_finder("hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!"))
	print(2)

# Happy Numbers
def happy_numbers(n):
	"""
	Given n, return the number of happy numbers between 1 and n (inclusive).
	https://en.wikipedia.org/wiki/Happy_number

	Args:
		(int) n: the upper bound.
	
	Returns:
		(int) the number of happy numbers from 1 to n.
	"""
	pass
	''' count = 0
	a = 1
	visited = set()
	while 1:
    	if a == 1:
        	print "Number is happy!"
        	break
    	a = sum(int(c) ** 2 for c in str(a))
    	if a in visited:
        	print "Number is sad!"
        	break
    	visited.add(a) '''