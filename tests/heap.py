import unittest
from pymsalign.heap import Heap, ExtendedHeap

class HeapTests(unittest.TestCase):
    def test_basic(self):
        myints = [10, 20, 30, 5, 15]

        heap = Heap()

        heap.make_heap(myints)

        self.assertEqual(heap.front(), [2, 0, 30])

        heap.pop_heap()
        heap.pop_back()

        self.assertEqual(heap.front(), [1, 0, 20])

class ExtendedHeapTests(unittest.TestCase):
    def test_basic(self):
        myints = [10, 20, 30, 5, 15]

        heap = ExtendedHeap()
        heap.make_heap(myints)

        print(heap.heap)

if __name__ == "__main__":
    unittest.main()