'''This module contains unittests for Corpus class.

'''
import os
import json
import logging
import unittest
from pub import utils


class TestUtils(unittest.TestCase):

    @unittest.skip('Takes too much time to run')
    def test_downloader(self):
        logging.basicConfig(filename='pub.log', level=logging.INFO)
        logger = logging.getLogger(__name__)
        config_file_address = 'test/data/config.json'
        with open(config_file_address) as fin:
            config = json.load(fin)
        file_links = ["pubmed/baseline/pubmed19n0001.xml.gz"]
        dest_dir = 'test/data'
        utils.downloader(file_links, dest_dir, logger, sleep=2,
                         server_address=config['server_address'])
        dest_address = os.path.join(dest_dir, "pubmed19n0001.xml.gz")
        self.assertTrue(os.path.exists(dest_address))
        self.assertTrue(os.path.isfile(dest_address))
        os.remove(dest_address)
