
def facesiter(simplex):
    for i in range(len(simplex)):
        yield simplex[:i]+simplex[(i+1):]

def flattening_simplex(simplices):
    for simplex in simplices:
        for point in simplex:
            yield point

def get_allpoints(simplices):
    return set(flattening_simplex(simplices))

from .abssimcomplex import SimplicialComplex
from .alphacomplex import AlphaComplex