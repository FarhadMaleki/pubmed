'''Extract article information from PubMed baseline gz (gzipped) files.

'''
import gzip
from lxml import etree

class Corpus:
    '''Extract article information for all records in a PubMed baseline file.

    Args:
         input_address (str): Address of a PubMed baseline gz (gzipped) file.
         config (dict): A dictionary that determines the information
            being extracted.
    '''
    def __init__(self, input_address, config):
        self.config = config
        self.articles = Corpus.collect_articles(input_address, self.config)

    @staticmethod
    def collect_articles(address, config):
        '''Extract article information for all records in a PubMed baseline file.

        Args:
            address: Address of a PubMed baseline gz (gzipped) file.

        Returns:
            list: A list of data items for each article in the PubMed baseline
                gz (gzipped) file. The order of items is defined by the order of content
                in the config object.
        '''
        with gzip.open(address, mode='rt', encoding=config['encoding']) as fin:
            root = etree.parse(fin)
        etree.strip_tags(root, config["striped_tags"])
        elements = root.xpath(config['articles_path'])
        articles = []
        for element in elements:
            pmid = element.findtext('PMID')
            article = element.find(config['article_tag'])
            info = [pmid]
            for tag in config['contents']:
                info.append(article.findtext(tag))
            articles.append(info)
        return articles

    def __iter__(self):
        '''Define an iterator.

        Return:
            iterator: An iterator object for articles in the Corpus.

        '''
        return iter(self.articles)
