'''This module helps to download PubMed baseline files in parallel.
'''
import json
import argparse
import os.path
import multiprocessing as mp
from pub.utils import downloader


def main(args):
    with open(args.config) as fin:
        config = json.load(fin)
    links = []
    #Read links to PubMed baseline files
    with open(args.link_file, 'r') as fin:
        for link in fin:
            link = link.strip()
            if link != '':
                links.append(link)
    #Split links to chunks of almost equal size
    chunk_size = len(links) // args.proc
    chunks = []
    i = 0
    while i < len(links):
        chunks.append(links[i:i+chunk_size])
        i += chunk_size
    #Download links in parallel
    pool = mp.Pool(processes=args.proc)
    results = [pool.apply_async(downloader, args=(file_links,
                                                  args.output_dir,
                                                  args.sleep,
                                                  config['server_address']))
               for file_links in chunks]
    results = [p.get() for p in results]



if __name__ == '__main__':
    parser = argparse.ArgumentParser('PubMed data downloader.')
    msg = ('Config file address. A JSON file that determine the data items '
           'to be extracted from each PubMed baseline file')
    parser.add_argument('--config', type=str, required=True, help=msg,
                        metavar='<JSON file path>')

    msg = ('Sleep time between each file download; default 2 seconds. '
           'It must be a positive integer.')
    parser.add_argument('--sleep', type=int, default=2, help=msg,
                        metavar='<positive integer>')

    msg = 'PubMed baseline gz (gzipped) file addresses'
    parser.add_argument('--link_file', type=str, required=True, help=msg,
                        metavar='<file path>')

    msg = ('Number of processes, The default value is 1. Use larger number '
           ' while considering your bandwidth and number of processors')
    parser.add_argument('--proc', type=int, default=1, help=msg,
                        metavar='<positive integer>')

    msg = 'Output directory address'
    parser.add_argument('--output_dir', type=str, required=True, help=msg,
                        metavar='<directory path>')
    args = parser.parse_args()
    #Check if the output directory exists
    if  not (os.path.exists(args.output_dir) and
             os.path.isdir(args.output_dir)):
        msg = 'Output directory does not exists: {}'.format(args.output_dir)
        raise FileNotFoundError(msg)
    main(args)
