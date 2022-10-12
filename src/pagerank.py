from math import sqrt
import gzip
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter()

def pagerank():
    links = {}
    num_inlinks = {}
    pages = set([])
    with gzip.open(inputFile,'rt') as f:
        for line in f:
            l = line.strip().split('\t')
            pages.add(l[0])
            pages.add(l[1])
            links[l[0]] = links.get(l[0], []) + [l[1]]
            num_inlinks[l[1]] = num_inlinks.get(l[1], 0) + 1
    #print(links)
    pages = list(pages)
    #print(pages)
    numPages = len(pages)

    oldPR = {}
    newPR = {}
    for p in pages:
        oldPR[p] = 1/numPages
        newPR[p] = 0 # arbitrary placeholder value
    #print(oldPR, newPR)
    def neighbors(page):
        return links.get(page, [])
    def converged(addEvery):
        d = 0
        for p in pages:
            newPR[p] += addEvery
            d += abs(oldPR[p] - newPR[p]) ** 2
        return sqrt(d) <= tau

    while True:
        #print('ITERATION')
        for p in pages:
            newPR[p] = lambda_val/numPages
        addEvery = 0
        for p1 in pages:
            outlinks = neighbors(p1)
            if len(outlinks) > 0:
                for p2 in outlinks:
                    newPR[p2] += ((1-lambda_val)*oldPR[p1]) / len(outlinks)
            else:
                addEvery += ((1-lambda_val)*oldPR[p1]) / len(pages)

        if converged(addEvery): # addEvery happens during convergence
            break
        for p in pages:
            oldPR[p] = newPR[p]
    # pp.pprint(newPR)
    ranksList = []
    ranksMap = {}
    for p in newPR:
        ranksList.append((p, newPR[p]))
    ranksList.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(ranksList)):
        ranksMap[ranksList[i][0]] = i + 1
    ranksList = ranksList[:k]

    with open(pagerankFile, 'w') as f:
        for i in range(len(ranksList)):
            f.write(f'{ranksList[i][0]}\t{i+1}\t{ranksList[i][1]}\n')

    inlinksList = []
    for p in pages:
        inlinksList.append((p, num_inlinks.get(p, 0)))
    inlinksList.sort(key=lambda x: x[1], reverse=True)
    inlinksList = inlinksList[:k]

    with open(inLinksFile, 'w') as f:
        for i in range(len(inlinksList)):
            f.write(f'{inlinksList[i][0]}\t{ranksMap[inlinksList[i][0]]}\t{inlinksList[i][1]}\n')
    # pp.pprint(ranksMap)
    # pp.pprint(ranksList)

    return newPR



if __name__ == '__main__':
    # Read arguments from command line; or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "links.srt.gz"
    lambda_val = float(sys.argv[2]) if argv_len >=3 else 0.2
    tau = float(sys.argv[3]) if argv_len >=4 else 0.005
    inLinksFile = sys.argv[4] if argv_len >= 5 else "inlinks.txt"
    pagerankFile = sys.argv[5] if argv_len >= 6 else "pagerank.txt"
    k = int(sys.argv[6]) if argv_len >= 7 else 100
    pagerank()
    # python3 pagerank.py links.srt.gz 0.20 0.005 inlinks.txt pagerank.txt 100


'''
Since others may benefit from an answer to this. The problem is that you created a zip file that has a folder in it called Submission and put everything inside that. Instead, you want to create a zip file that has three files plus a src folder that contains your code and then upload that -- no top-level folder in the zip file. To verify that that was right, I downloaded your submission, converted it to that format, and re-uploaded on your behalf. It works fine and the autograder says that all of the files are there. (It does complain about other problems, so you should look at the output.)

To be explicit, I created a zip file called P2submission.zip. I dragged the inlinks, pagerank, and README files into that. I then dragged the src folder and its included pagerank source code there. The resulting structure is:

P2submission.zip
inlinks.txt
pagerank.txt
README
src
pagerank.java

Note that could also accomplish the goal by dragging the three text files directly into gradescope (outside of a zip folder) and then creating a zip folder that has within it a src folder that contains pagerank.java. Again, no folder outside of the src folder.
'''