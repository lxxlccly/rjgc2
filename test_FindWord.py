'''类FindWord的测试代码'''
from unittest import TestCase, mock
from mktest2_optimization import FindWord


class TestFindWord(TestCase):
    '''类FindWord的测试'''
    def setUp(self):
        self.find_words = FindWord()

    def test_find_word(self):
        '''find_word的测试'''
        words = 'query.txt'
        document = 'document.txt'
        result = ['1/3,2/3,4/3', '', '', '1/1']
        self.assertEqual(result, self.find_words.find_word(words, document), "与预期结果不同")
        with mock.patch('builtins.print') as mock1:
            self.find_words.find_word(words, document)
            mock1.assert_has_calls([
                mock.call('1/3,2/3,4/3'),
                mock.call('None'),
                mock.call('None'),
                mock.call('1/1')
            ])
