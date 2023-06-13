#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        t  = (0, None)
    else:
        t = (len(sentence), sentence[:1])
    return(t)
