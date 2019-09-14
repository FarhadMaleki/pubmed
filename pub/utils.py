'''This module includes utility functions.

'''
import time
import os.path
from ftplib import FTP



def downloader(file_links, dest_dir, logger, sleep=2,
               server_address="ftp.ncbi.nlm.nih.gov"):
    ''' Download files from a FTP server.

    Args:
        file_links (str): Address of the file on the FTP server.
            For example "pubmed/baseline/pubmed19n0001.xml.gz".
        dest_dir (str): Address of the directory where the downloaded file
            will be saved.
        logger (logging.Logger): A Logger object used for logging.
            It can be defined as follows:
            import logging
            logging.basicConfig(filename='pub.log', level=logging.INFO)
            logger = logging.getLogger(__name__)
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
            msg = 'Downloading {} to: {}'.format(link,
                                                 os.path.join(dest_dir, name))
            logger.info(msg)
            with open(os.path.join(dest_dir, name), 'bw') as fout:
                ftp.retrbinary('RETR ' + link, fout.write)
            msg = 'Downloaded to: {}'.format(os.path.join(dest_dir, name))
            logger.info(msg)
