# Portaone task analysis and decision description

<!--toc-->
- [Analysis](#analysis)
    * [Optimisations implemented](#optimisations-implemented)
        * [Performance](#performance)
        * [Optimisations which may be suggested](#optimisations-which-may-be-suggested)
- [To run the program](#to-run-the-program)
<!-- tocstop -->

## Analysis

The problem provided (an array of strings of 6 numbers which are connected with first-last 2 digits to find longest sequence of such numbers) is in it's core a [longest path problem on a graph](https://en.wikipedia.org/wiki/Longest_path_problem).

In general terms such problems NP-hard and basically require checking of all variants of paths through the possible paths in the graph. There is a faster algorythm for graphs which are directed and acyclic. This problem is on a directed but not acyclic graph.

Solution is based on building and sifting through possible solutions. 

The algorythms selects each number (a node in graph terms) in the list as a starting node of the graph and then builds tree of possible paths through other nodes. The paths are forming a virtual tree structure, so recursive tree traversing algorythm seems to be appropriate for this case. Possible recursion limitation of python as runtime environment will be eliminated (to the extent) by setting [sys.setrecursionlimit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit) call (tenfold the number of numbers/nodes).

### Optimisations implemented

Fragment class which represents single number/node is optimizing algorythm by parsing the number into 3 parts (tail - leftmost part, body - mid part, head - rightmost part of the number) and converts those strings into python integer, so lookup and comparison operations run quite faster than string comparison operations.

Main optimization implemented is a MOB (MapOfBuckets) structure. MOB is a map where keys are tail parts, so lookup of next node in the path is done in constant time and buckets are arrays of numbers, which has the same tail and iteration is done through such arrays (map key and array represent a possible tree level which has to be iterated to form paths).

### Performance

For the problem list of 142 numbers the program runs for approx. **300** seconds on notebook AMD Ryzen 7 processor (Windows 10, CPython 3.10.9 standard distibution).

It finds 49900000+ valid paths of which it selects 640 paths of max length of 67 numbers each (resulting paths are in "640 longest lists [67].txt" file). 


### Optimisations which may be suggested

* To check if node is included into current path a scanning of the path is performed. This may be replaced with some constant time (e.g. array lookup)
* The problem can trivially parallelized (as checks of separate nodes as tree roots are independent)


## To run the program

The program does not require any 3rd party libraries and was tested with python 3.10.9

Just run in terminal

`python main.py`

in the directory of the solution.

In globs.py file there are two global settings, which turn on debugging and checking of solution correctness.

Extended information and results are printed to stdout. To save them redirect to a file may be used e.g.:

`python main.py > result.txt`





