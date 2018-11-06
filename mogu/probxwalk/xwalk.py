
import numpy as np
from collections import defaultdict


def compute_uniformweighted_xwalk(mappings):
    xwalk_dict = {}
    for key in mappings:
        if type(mappings[key]) is not list:
            xwalk_dict[key] = {mappings[key]: 1.0}
        else:
            xwalk_dict[key] = {target: 1./len(mappings[key]) for target in mappings[key]}
    return xwalk_dict


def compute_resultant_xwalk(xwalk1, xwalk2):
    result_xwalk_dict = {}
    for key in xwalk1:
        result_xwalk_dict[key] = defaultdict(lambda : 0)
        for intermediate_key in xwalk1[key]:
            weight = xwalk1[key][intermediate_key]
            for target in xwalk2[intermediate_key]:
                result_xwalk_dict[key][target] += weight*xwalk2[intermediate_key][target]
        result_xwalk_dict[key] = dict(result_xwalk_dict[key])
    return result_xwalk_dict
