'''This module contains unittests for Corpus class.

'''
import os
import json
import glob
import unittest
from pub import utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        '''Set up the configuration for Corpus objects.
        '''
        config_file_address = 'test/data/config.json'
        with open(config_file_address) as fin:
            self.config = json.load(fin)

    @unittest.skip('Takes too much time to run')
    def test_downloader(self):
        '''Test if the downloader method is working.

        This test depends on the availability of the PubMed FTP server. Also,
            the name and content of the file changes on the FTP server from
            time to time. Therefore, this test must be skipped. Running this
            test requires updating the links and their corresponding files.

        '''
        # Make sure that such a link is still available
        file_links = ["pubmed/baseline/pubmed19n0001.xml.gz"]
        dest_dir = 'test/data'
        utils.downloader(file_links, dest_dir, sleep=2,
                         server_address=self.config['server_address'])
        # THe following line must be updated if you update the FTP link.
        dest_address = os.path.join(dest_dir, "pubmed19n0001.xml.gz")
        self.assertTrue(os.path.exists(dest_address))
        self.assertTrue(os.path.isfile(dest_address))
        os.remove(dest_address)

    def test_corpra(self):
        '''Test if corpra read a collection of PubMed baseline gz (gzipped) files.

        The aggregated version of the sample corpus files is located in
        PubMedSampleFile.csv. The order of the loaded articles might not be the
            same as the aggregated version.
        '''
        articles_file_address = 'test/data/PubMedSampleFile.csv'
        corpus_articles = []
        with open(articles_file_address, 'r', encoding='utf-8') as fin:
            for line in fin:
                article = line.strip().split('\t')
                corpus_articles.append(article)
        input_addresses = glob.glob('test/data/sample_corpra/*.gz')
        articles = list(utils.corpra(input_addresses, self.config, num_proc=2))
        self.assertEqual(len(articles), 11)
        self.assertListEqual(sorted(articles), sorted(corpus_articles))
