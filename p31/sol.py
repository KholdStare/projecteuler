#!/usr/bin/env python

class Solver(object):
    """Solves how many combinations of denominations can add up to a target.
    The difficult part is that order doesn't matter- ie. 2 + 1 == 1 + 2,
    so a straightforward fibonacci approach does not work."""

    def __init__(self, denominations, target):
        self.denominations = denominations
        # cache[i][j]. i = max denomination to be used (index into list of denoms)
        # j = target
        self.cache = [ [ 1 for i in xrange(0, target+1) ] ]

        for i in xrange(1, len(denominations)):
            denom = denominations[i]

            # initialize row of cache
            self.cache.append( [1] + [ 0 for j in xrange(0, target) ])

            for t in xrange(1, target+1):
                # add the number of combinations when not using this
                # denomination at all
                self.cache[i][t] += self.cache[i-1][t]

                if t >= denom:
                    self.cache[i][t] += self.cache[i][t-denom]

    def getCombinations(self, target):
        return self.cache[-1][target]

    def __str__(self):
        return str(self.cache)

if __name__ == "__main__":
    target = 200
    solver = Solver( [1, 2, 5, 10, 20, 50, 100, 200], target )
    print solver.getCombinations(target)
