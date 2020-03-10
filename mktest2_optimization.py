'''从一个txt文档中找出某些单词所在的位置'''
#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import re
import sys


class FindWord(object):
    def __init__(self):
        self.query = 'query.txt'
        self.document = 'document.txt'

    def find_word(self, query, document):
        '''找出单词在文档中的位置。

        以问号、句号、感叹号为句子分隔符，输出第几句/第几个词。'''
        self.query = query
        self.document = document
        sentence = 0
        words = []
        with open(self.query) as query_file:
            for word in query_file:
                words.append((word.strip("\n")).lower())
        length_words = len(words)
        with open(self.document) as document_file:
            all_line = []
            for line in document_file:
                all_line.append(line)
        word_amount = [0] * length_words
        word_position = [''] * length_words
        word_punctuation = []
        length_all_line = len(all_line)
        for i in range(length_all_line):
            line_list = re.findall(r'\w+|\.|\?|\!', all_line[i])
            word_punctuation += line_list
            while 1:
                has_punctuation = 0
                length_word_punctuation = len(word_punctuation)
                for j in range(length_word_punctuation):
                    if word_punctuation[j] in {'.', '!', '?'}:
                        has_punctuation = 1
                        sentence += 1
                        for k in range(0, j):
                            word1 = word_punctuation[k].lower()
                            for x in range(0, length_words):
                                if word1 == words[x]:
                                    word_amount[x] += 1
                                    if word_amount[x] > 1:
                                        word_position[x] += ',{0}/{1}'.format(sentence, k + 1)
                                    else:
                                        word_position[x] += '{0}/{1}'.format(sentence, k + 1)
                        for k in range(j, -1, -1):
                            del word_punctuation[k]
                        break
                if has_punctuation == 0:
                    break
        for i in range(length_words):
            if word_amount[i] == 0:
                print('None')
            else:
                print(word_position[i])
        return word_position


if __name__ == '__main__':
    ARGS = sys.argv[1:]
    DOCUMENT = ARGS[0]
    QUERY = ARGS[1]
    fw = FindWord()
    fw.find_word(QUERY, DOCUMENT)
