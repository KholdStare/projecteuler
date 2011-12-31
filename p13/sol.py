#!/usr/bin/python
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

def main (filename):
    inputFile = open(filename, 'r')
    # list of lists, indexed like matrix. rows then cols
    grid  = [ [ int(d) for d in list(s.strip()) ] for s in inputFile.readlines() ]

    result = []
    while 1 == 1:
        column = [ line.pop() for line in grid if len(line) > 0 ]
        if len(column) == 0:
            break

        columnSum =  sum(column)
        # get last digit of sum and append it to result
        result.insert(0, str(columnSum)[-1])
        # put remaining digits as another number to be added next time
        grid.append([ int(d) for d in list(str(columnSum)[:-1]) ] )

    return "".join(result)

if __name__ == "__main__":
    print main(thisDir + "/input")
