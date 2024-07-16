# -*- coding: utf-8 -*-
"""
knapsack.py - CS6515, Intro to Graduate Algorithms, Spring 2024

Implement a Dynamic Programming Solution to the knapsack problem.   The program will be given a
dictionary of items and an overall weight limit.  It should select the combination of items 
which achieves the highest value without exceeding the weight limit.    

About the Input:

	itemsDict -- a dictionary of items, where the key is an integer 1...N (inclusive),
	             and the value is a tuple (name, weight, value) where
			        name is the text name of the item
				    weight is the item weight
				    value is the item value

	maxWeight -- the maximum weight supported by the knapsack

NOTE:
    Each item may be selected at most one time (non-repeating)
	There is at least one item available to process
	All weights and values are >0
	All test cases will have a solution (at least one item can be inserted in the knapsack)
"""
import argparse  # argparse allows the parsing of command line arguments
import GA_ProjectUtils as util  # utility functions for cs 6515 projects


def initTable(numItems, maxWeight):
    """
    Initialize the table to be used to record the best value possible for given
    item idx and weight
    NOTE : this table must:
              -- be 2 dimensional (i.e. T[x][y])
              -- contain a single numeric value (no tuples or other complicated abstract data types)
    """
    # TODO Replace the following with your code to initialize the table properly

    T = [[0] * (maxWeight+1) for i in range(numItems + 1)]
    return T


def defineItemRange(numItems):
    """
    define the range to iterate through the 'item' axis of your table

        numItems : number of items

    Note: the index (key value) for items are integer values 1..N inclusive
    """
    # TODO Replace the following with your code to define the range of values

    return range(1, numItems + 1)


def defineWeightRange(maxWeight):
    """
    define the range to iterate through the 'weight' axis of your table

        maxWeight : maximum weight available
    """
    # TODO Replace the following with your code to define the range of values

    return range(1, maxWeight + 1)


def subProblem(T, weight, itemIDX, itemWeight, itemValue):
    """
    Define the subproblem to solve for each table entry
        T : the table being populated
        weight : the current max weight from iterating through all possible weight values
        itemIDX : the index (key value) of the current item from iterating through all items
        itemWeight : the weight of the item
        itemValue : the value of the item
    """
    # TODO Replace the following with your code to solve the subproblem appropriately
    if itemWeight > weight:
        return T[itemIDX- 1][weight]
    else:
        return max(T[itemIDX -1][weight], T[itemIDX - 1][weight - itemWeight] + itemValue)


def buildResultList(T, itemsDict, maxWeight):
    """
    Construct list of items that have been selected.
        T : the populated table of subproblems, indexed by item idx and weight
        itemsDict : dictionary of items   Note: items are indexed 1..N
        maxWeight : maximum weight allowed

    	result: a list composed of item tuples
    """
    result = []
    weight = maxWeight

    for i in range(len(itemsDict), 0, -1):
        if T[i][weight] != T[i-1][weight]:
            idx, idx_weight, idx_value = itemsDict[i]
            result.append((idx, idx_weight, idx_value))
            weight = weight - idx_weight
        else:
            continue

    # TODO Your code goes here to build the list of chosen items

    return result

######## Do not modify any of the lines below #######

def knapsack(itemsDict, maxWeight):
    """
    Solve the knapsack problem for the passed list of items and max allowable weight
    DO NOT MODIFY THE FOLLOWING FUNCTION
    NOTE : There are many ways to solve this problem.  You are to solve it
            using a 2D table, by filling in the function templates above.
            If not directed, do not modify the given code template.
    """
    numberItems = len(itemsDict)
    # initialize table properly
    table = initTable(numberItems, maxWeight)
    itemRange = defineItemRange(numberItems)
    weightRange = defineWeightRange(maxWeight)

    for itemIdx in itemRange:
        # query item values from list
        item, itemWeight, itemValue = itemsDict[itemIdx]
        for weight in weightRange:
            # expand table values by solving subproblem
            table[itemIdx][weight] = subProblem(table, weight, itemIdx, itemWeight, itemValue)

    # build list of results - chosen items to maximize value for a given weight
    return buildResultList(table, itemsDict, maxWeight)


def main():
    """
    The main function
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    # You may change default values, but any values you set will be overridden when autograded
    parser = argparse.ArgumentParser(description='Knapsack Coding Quiz')
    parser.add_argument('-i', '--items', help='File holding list of possible Items (name, wt, value)',
                        default='defaultItems.txt', dest='itemsListFileName')
    parser.add_argument('-w', '--weight', help='Maximum (integer) weight of items allowed', type=int, default=400,
                        dest='maxWeight')

    # args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-a', '--autograde', help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2],
                        default=1, dest='autograde')
    args = parser.parse_args()

    # DO NOT MODIFY ANY OF THE FOLLOWING CODE
    itemsDict = util.buildKnapsackItemsDict(args)
    itemsChosen = knapsack(itemsDict, args.maxWeight)
    util.displayKnapSack(args, itemsChosen)


if __name__ == '__main__':
    main()
