#name:Mingnan Su
#macID: sum1


import numpy

def average(lst):
    radius=[]
    for c in lst:
        radius.append(c.r)
    return numpy.average(radius)

def stdDev(lst):
    radius=[]
    for c in lst:
        radius.append(c.r)
    return numpy.std(radius)

def rank(lst):
    radius=[]
    for c in lst:
        radius.append(c.r)
    tuples=list(enumerate(sorted(radius),1))

    #result is stored in ranked
    ranked=[]
    for rd in radius:
        for tp in tuples:
            if tp[1]==rd:
                ranked.append(tp[0])
                break
    return ranked

