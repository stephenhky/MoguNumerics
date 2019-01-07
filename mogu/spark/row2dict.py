
from pyspark.sql.types import Row


def convertRowToDict(row):
    targetdict = row.asDict()
    for key in targetdict:
        if (targetdict[key])==Row:
            targetdict[key] = convertRowToDict(targetdict[key])
        elif type(targetdict[key])==list and len(targetdict[key])>0 and type(targetdict[key][0])==Row:
            targetdict[key] = convertRowsToDict(targetdict[key])
    return targetdict


def convertRowsToDict(rows):
    targetdicts = [row.asDict() for row in rows if row is not None]
    for targetdict in targetdicts:
        for key in targetdict:
            if type(targetdict[key])==list and len(targetdict[key])>0 and type(targetdict[key][0])==Row:
                targetdict[key] = convertRowsToDict(targetdict[key])
            if type(targetdict[key])==Row:
                targetdict[key] = convertRowToDict(targetdict[key])
    return targetdicts
