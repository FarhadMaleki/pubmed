'''This module contains unittests for Corpus class.

'''
import json
import unittest
import collections
from pub.corpus import Corpus


class TestCorpus(unittest.TestCase):
    def setUp(self):
        config_address = 'test/data/config.json'
        self.corpus_file_address = 'test/data/PubMedSampleFile.xml.gz'
        articles_file_address = 'test/data/PubMedSampleFile.csv'
        with open(config_address, 'r') as fin:
            self.config = json.load(fin)
        self.corpus_articles = []
        with open(articles_file_address, 'r', encoding='utf-8') as fin:
            for line in fin:
                article = line.strip().split('\t')
                self.corpus_articles.append(article)

    def test_collect_articles(self):
        corpus = Corpus(self.corpus_file_address, self.config)
        self.assertListEqual(corpus.articles, self.corpus_articles)

    def test__iter__(self):
        corpus = Corpus(self.corpus_file_address, self.config)
        self.assertTrue(isinstance(iter(corpus), collections.Iterator))
