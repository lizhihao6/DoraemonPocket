import unittest
from DoraemonPocket import multiprocessing

def son_func(id0, id1):
    return id0, id1

class Test(unittest.TestCase):
    def test_multiprocessing():
        ids = multiprocessing(son_func, [i for i in range(10)], 1)
        for i, id in enumerate(ids):
            assert id[0]==i
            assert id[1]==1 

if __name__ == '__main__':
    unittest.main()