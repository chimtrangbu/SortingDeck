# SortingDeck
Implement known sorting algorithms, and discover the world of algorithm analysis.

# Core project
Notions: sorting algorithms and algorithm complexity
## Introduction
This subject is an algorithm project.

It will initiate you to a fundamental category of algorithms -sorting algorithms-, as well as theoretical notions revolving around algorithm analysis, such as the big O notation. In this project, your understanding of the theoretical notions is as important as your code, so spend enough time doing your research and synthesizing it.

## Your mission
Your mission is to implement different sorting algorithms and to visualise those algorithms. 

When given a series of numbers as input, your program will sort them using the algorithm specified on the command line. It will output the different steps of the sorting operation on stdout, or display them in the GUI if the GUI option is specified.

In the core part of the project, you will implement the following algorithms:

- bubble sort
- insertion sort
- quick-sort
- merge sort

Because understanding algorithms and their complexity is essential to become a well-rounded engineer (... you will also need it to pass technical interviews!), you also need to research the complexity of those algorithms. During the code review, you must be able to describe the worst/average/best cases of those algorithms.

Note: Obviously you won't get any skill points if you don't understand perfectly what you have implemented.

## Directions
Your program must be called `sorting_deck.py` and be present at the root of your git repository.

The arguments to the `--algo` option are bubble, insert, quick and merge. If the option `--algo` is not specified, the default algorithm will be bubble sort.

A `--gui` option will display a graphical representation of the sort with the pyglet library that you know already. You must be able to display inputs of up to 15 integers in the core part of the project (you can handle larger inputs as a bonus). This limit is only for the GUI mode, the default mode should of course handle inputs of all sizes.

In non-GUI mode, the outputs on stdout will be as follow:

- Bubble sort: you will output the list after each swap of integers
- Insertion sort: you will output the list after each insertion operation placing a number at its right place in the sorted list
- Quick sort: you will output the pivot and the list after each partition operation (you can choose the pivot however you want)
- Merge sort: you will output the merged list after each merge of two sublists. The Sentinel will assume that you recursively sort the left half of a list first.

You have to respect those output directions strictly, otherwise the Sentinel won't be able to assess that you correctly implemented your algorithm.

```sh
$ ./sorting_deck.py -h
usage: sorting_deck.py [-h] [--algo ALGO] [--gui] N [N ...]

positional arguments:
  N            an integer for the list to sort

optional arguments:
  -h, --help   show this help message and exit
  --algo ALGO  specify which algorithm to use for sorting among
               [bubble|insert|quick|merge], default bubble
  --gui        visualise the algorithm in GUI mode
  
# in GUI mode, you need to handle input of size between 1 and 15 integers
$ ./sorting_deck.py --gui 23 8 9 0 1 -93 3 -2 19 4 54 5 33 -34 55 -3
Input too large

# an error message is displayed if no integers are supplied
$ ./sorting_deck.py
usage: sorting_deck.py [-h] [--algo ALGO] [--gui] N [N ...]
sorting_deck.py: error: the following arguments are required: N

# by default, the sorting algorithm will be bubble sort. You will output the list after each swap of integers
$ ./sorting_deck.py 23 9 -8 7 3
9 23 -8 7 3
9 -8 23 7 3
9 -8 7 23 3
9 -8 7 3 23
-8 9 7 3 23
-8 7 9 3 23
-8 7 3 9 23
-8 3 7 9 23

# if the input provided for bubble sort is already sorted, nothing should be printed (you didn't do any swapping, right?)
$ ./sorting_deck.py 1 2 3 6 90
$

# for insertion sort, you will display the list after each insertion operation placing an integer at its right place in the sorted list
$ ./sorting_deck.py --algo insert 1 3 8 -7 10 4 2
-7 1 3 8 10 4 2
-7 1 3 4 8 10 2
-7 1 2 3 4 8 10

# equally, when the input is already sorted, there shouldn't be any insertion operation
$ ./sorting_deck.py --algo insert 1 2 3 6 90
$

# for quick sort, you will print the pivot, and the state of the list after each partition operation
$ ./sorting_deck.py --algo quick 23 10 9 -8 20 7 3
P: -8
-8 10 9 3 20 7 23
P: 3
-8 3 9 23 20 7 10
P: 20
-8 3 9 10 7 20 23
P: 10
-8 3 9 7 10 20 23
P: 9
-8 3 7 9 10 20 23

# is quicksort efficient on already sorted arrays...?
$ ./sorting_deck.py --algo quick 1 4 6 9 70
P:  6
1 4 6 9 70
P:  1
1 4 6 9 70
P:  9
1 4 6 9 70

# for merge sort, you will output the resulting list after each merge of two sublists, assuming that you recursively sort the left half of a list first.
$ ./sorting_deck.py --algo merge 23 4 9 -8 20 7 3
4 9
4 9 23
-8 20
3 7
-8 3 7 20
-8 3 4 7 9 20 23

$ ./sorting_deck.py --algo merge 1 4 6 9 70
1 4
9 70
6 9 70
1 4 6 9 70

```

## The algorithm visualisator
The GUI must display the list of integers and the different changes leading to the list being sorted. You are free to represent the list the way you want, to have animations for moving around the integers, etc - be creative, as long as the different steps of the algorithm are perfectly understandable!

It will also showcase which element the algorithm is at, at any moment. For example the bubble sort will run over the whole list as long as it finds at least one element unsorted. This passing over the list must be visualised (for example, you can have each element highlighted as the algorithm loops over it).

Your GUI must have a step by step mode where hitting a keyboard key moves the algorithm to the next step.

All those elements will be checked manually during the review, as the Sentinel is GUI-blind!

Important note: all your code related to the GUI should be imported only if the --gui option is specified. First, to respect clean design principles (don't import useless modules!), and secondly because importing pyglet in the Sentinel will make it crash.

## The Sentinel
The Sentinel will only review the algorithms on stdout.

However, don't forget to run the Sentinel at the end of your project, to check that you still pass pycodestyle (you should never push on your remote repository dirty code anyway!) and the basic tests. Don't allow regressions to ruin your early work!

# BONUS: in-place merge sort
## Just for fun!
This is more of a textbook algorithm that you wouldn't use in real life, but it's still worth thinking about for the exercice.

Implement an in-place version of merge sort that doesn't require creating new lists, and its corresponding visualisation in the GUI.

How does this memory-efficient implementation affect the algorithm complexity of the merge sort? How significant is then the difference between the worse and best cases? Is it worth it?

# BONUS: simultaneous visualisation
## Let's compare them
Add a mode to your program to visualise simultaneously two algorithms performing on the same dataset.

You might have to use generators! (You can also use threads, if you feel particularly adventurous.)

