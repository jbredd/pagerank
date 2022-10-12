

Breakdown: all of the source code is in the pagerank.py file. the "name == main" function contains the functionality for reading system input, and the pagerank function does all of the reading file input, processing file input, and writing the processed output

Description: all of the program is implemented in the pagerank function in pagerank.py. to store the links, i used a hash map with keys being the page title and values being the pages it points to. i also used hashmap for storing the new and old pagerank values for each page. hashmap allows for really quick read/write operations, which is crucial for the pagerank algorithm since it relies on updating page rank valueswith every iteration of the while loop.
to implement the while loop, i followed the textbook. however, i thought of an optimization for the case of a page with no outlinks. since every pagerank value is to be updated by the same amount if there is no outlink, i thought that rather than actually looping back through the whole page rank hash map (which is quite large for large input), i could just store a cumulative number to add indiscrimnately to every page rank value when i update the values. i ended up doing this addition in the convergence function, since the convergence calculation relies on newPR being fully updated (w the cumulative value aforementioned). this optimization dramatically quickened the algorithm since it would no longer have to iterate through every page for every page that has no outlinks.

Libraries:
    - sys for command line input
    - math for sqrt
    - gzip for reading gz file input
    - pprint for pretty-printing hashmaps throughout my code to check correctness

Dependencies: none

Building/Running: running pagerank.py without any command line input defaults to the fallback input values. can alternatively override these defaults by providing arguments in the command line when running pagerank.py




