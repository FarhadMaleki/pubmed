'''This module includes utility functions.

'''
import time
import os.path
from ftplib import FTP
import multiprocessing as mp
from pub.corpus import Corpus


def downloader(file_links, dest_dir, sleep=2,
               server_address="ftp.ncbi.nlm.nih.gov"):
    ''' Download files from a FTP server.

    Args:
        file_links (str): Address of the file on the FTP server.
            For example "pubmed/baseline/pubmed19n0001.xml.gz".
        dest_dir (str): Address of the directory where the downloaded file
            will be saved.
        sleep (float): Amount of time (in second) between each FTP request.
        server_address (str): The FTP server address.
            The PubMed FTP address is currently "ftp.ncbi.nlm.nih.gov",
            which is the default value.

    '''
    with FTP(server_address) as ftp:
        ftp.login()
        for link in file_links:
            time.sleep(sleep)
            name = os.path.basename(link)
            with open(os.path.join(dest_dir, name), 'bw') as fout:
                ftp.retrbinary('RETR ' + link, fout.write)


def corpra(input_addresses, config, num_proc=1):
    '''Load corpra from several files.

    Args:
        input_addresses (str): A sequence of PubMed baseline gz (gzipped) file
            addresses.
        config (dict):  A dictionary that determines the information
            being extracted.
        num_proc (int): A positive integer determining the number of processes
            used to extract article information from corpra.
    Yields:
        A sequence of data items for each article in the PubMed baseline
            gz (gzipped) files located in the input_addresses. The order of
            articles in the corpra might not be preserved.

    '''
    pool = mp.Pool(processes=num_proc)
    corpra = [pool.apply_async(Corpus, args=(address, config))
              for address in input_addresses]
    for corpus in corpra:
        for article in corpus.get():
            yield article
