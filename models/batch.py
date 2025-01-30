from itertools import combinations

def batch(items, bsize):
    for i in range(0,len(items),bsize):
        yield items[i:i+bsize]
