import time
def read_textfile(filename):
    '''Read test dataset and return as a list.'''
    seq = []
    with open(filename) as f:
        for line in f:
           seq.append(int(line.replace('\n','')))
    return seq

def two_sum(seq, start_range, stop_range):
    '''Returns number of target values that are sum of two distinct input numbers.
    
    seq : list
        The sequence of input numbers to sum.
    start_range : int
        The beginning of the target value range, inclusive.
    stop_range : int
        The end of the target value range, inclusive.
    '''
    explored = set()
    targets = {t for t in range(start_range, stop_range + 1)}
    present = set()
    i = 0
    start = time.time()
    for e in seq:
        explored.add(e)
        temp_present = set()
        for t in targets:
            diff = t - e
            if diff != e and diff in explored:
                temp_present.add(t)
        present = present.union(temp_present)
        targets = targets.difference(temp_present)
        i += 1
        if i % 10000 == 0:
            print(f'{i} elements checked, last 10,000 in {time.time() - start:.2f}, {len(targets)} remain.')
            start = time.time()
    return len(present)