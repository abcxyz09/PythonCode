import re
def get_words(text):
	return re.compile('[A-Za-z]+').findall(text)

if __name__ == '__main__':
	text = raw_input()
	wordsList = get_words(text)
	print wordsList