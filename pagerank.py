import sys







if __name__ == '__main__':
    # Read arguments from command line; or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "links.srt.gz"
    lambda_val = float(sys.argv[2]) if argv_len >=3 else 0.2
    tau = float(sys.argv[3]) if argv_len >=4 else 0.005
    inLinksFile = sys.argv[4] if argv_len >= 5 else "inlinks.txt"
    pagerankFile = sys.argv[5] if argv_len >= 6 else "pagerank.txt"
    k = int(sys.argv[6]) if argv_len >= 7 else 100
    # python3 pagerank.py links.srt.gz 0.20 0.005 inlinks.txt pagerank.txt 100