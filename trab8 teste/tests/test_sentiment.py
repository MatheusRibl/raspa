import unittest
from unittest.mock import patch
from app import analisar_sentimento


class SentimentTests(unittest.TestCase):
    @patch('app.GoogleTranslator')
    def test_positive(self, mock_trans):
        # mock translator to return a clear positive English sentence
        mock_trans.return_value.translate.return_value = 'this is great and wonderful'
        s = analisar_sentimento('Isso é ótimo e maravilhoso')
        self.assertEqual(s, 'positivo')

    @patch('app.GoogleTranslator')
    def test_empty(self, mock_trans):
        mock_trans.return_value.translate.return_value = ''
        s = analisar_sentimento('')
        self.assertEqual(s, 'neutro')

    @patch('app.GoogleTranslator')
    def test_none(self, mock_trans):
        mock_trans.return_value.translate.return_value = ''
        s = analisar_sentimento(None)
        self.assertEqual(s, 'neutro')


if __name__ == '__main__':
    unittest.main()
