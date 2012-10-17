"""Module for determinant computation over GF(p).

Usage:

>>> import gfp
>>> F = gfp.GFp(11)         # Galois field with 11 elements
>>> F.det( [[1,0],[0,1]] )  # Matrices are lists of lists
1
>>> F.det( [[10,9],[1,2]] ) # Nonsingular over R, singular over F
0


"""

import copy

class GFp:
    """ Determinant computation in GF(p) using Gaussian elemination. """

    def __init__(self, p = 599):
        self.p = p
        self.rec = [(x ** (p-2)) % p for x in range(0, p)]  # rec[x] = 1/x

    def det_laplace(self, A):
        """ Determinant of A computed as the Lacplace expansion along the first row.
            This takes exponential time and is used only for validation.
        """
        sign = +1
        sum = 0
        if len(A) == 1:
            return A[0][0]
        for col in range(len(A)):
            subdet = self.det_laplace([ row[:col] + row[col+1:] for row in A[1:] ])
            sum = (sum + A[0][col]*subdet*sign) % self.p
            sign *= -1
        return sum

    def det(self, B):
        """ Determinant of B computed using Gaussian elemination"""
        det = 1
        A = copy.deepcopy(B) # otherwise B would be destroyed
        n = len(A)
        for j in range(n):
            # find row with nonzero entry below diag in column j and swap that row with jth row
            found = False
            for i in range(j,n):
                if A[i][j] != 0:
                    found = True
                    if i != j:
                        (A[i],A[j]) = (A[j], A[i])
                        det *= -1
                    break
            if not found: return 0 #  singular
            assert(A[j][j] != 0)
            det = ( det *  A[j][j] ) % self.p
            # multiply jth row with 1/A[j][j]
            reciprocal = self.rec[A[j][j]]
            for k in range (j,n):
                A[j][k] = ( A[j][k] * reciprocal ) % self.p
            assert(A[j][j] == 1)
            for i in range(j+1,n):
                # eliminate col j in row i for i > j:
                c = A[i][j]
                for k in range(j,n):
                    A[i][k] = ( A[i][k] - c*A[j][k] ) % self.p
        return det

if __name__ == "__main__":
    p = 599
    gfp = GFp(p)

    assert (gfp.det([[1,0],[0,1]]) == 1)

    matrices = [
        [[0,1],[1,0]],
        [[0,1],[0,1]],
        [[0,1],[1,3]],        
        [[0,1],[1,6]],
        [[1,1],[2,3]],
        [[0,1],[1,0]],
        [[0,1],[0,-1]],
        [[0,1],[1,-3]],        
        [[0,1],[1,-6]],
        [[1,1],[-2,-3]],
        [[0,2],[2,0]],
        [[2,0],[0,2]],
        [[0,10],[0,10]],
        [[0,10],[10,3]],        
        [[0,10],[10,6]],
        [[10,10],[23,3]],
        [[0,10],[10,0]],
        [[0,10],[0,-10]],
        [[0,10],[10,-3]],        
        [[0,10],[10,-6]],
        [[10,10],[-23,-3]],
        [[p-1,p-2],[1,2]] # nonsingular over the reals
        ]

    for A in matrices:
        assert(gfp.det_laplace(A) == gfp.det(A))

        # wild west testing: random 8x8 matrix   
    import random
    A = [
        [random.randrange(599) for i in range(8)]
        for i in range(8)
        ]
    assert(gfp.det_laplace(A) == gfp.det(A))

