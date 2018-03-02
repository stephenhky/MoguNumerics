
from itertools import combinations
from numba import jit


@jit(cache=True)
def facesiter(simplex):
    for i in range(len(simplex)):
        yield simplex[:i]+simplex[(i+1):]


@jit(cache=True)
def flattening_simplex(simplices):
    for simplex in simplices:
        for point in simplex:
            yield point


@jit(cache=True)
def get_allpoints(simplices):
    return set(flattening_simplex(simplices))


@jit(cache=True)
def faces(simplices):
    faceset = set()
    for simplex in simplices:
        numnodes = len(simplex)
        for r in range(numnodes, 0, -1):
            for face in combinations(simplex, r):
                faceset.add(tuple(sorted(face)))
    return faceset

from .abssimcomplex import SimplicialComplex
from .alphacomplex import AlphaComplex
from .vrcomplex import VietorisRipsComplex