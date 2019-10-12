
class Heap:
    """
        A Python implementation of the C++ Stack.
    """
    def __init__(self):
        self.heap = []

    def _standard_comp(a, b):
        return a[2] >= b[2]

    def _heapify(self, heap_size, x, comp=_standard_comp):
        right = 2 * (x + 1)
        left = right - 1

        largest = x

        if left < heap_size and comp(self.heap[left], self.heap[x]):
            largest = left
        if right < heap_size and comp(self.heap[right], self.heap[largest]):
            largest = right
        if largest != x:
            self.heap_swap(x, largest)
            self._heapify(heap_size, largest, comp)

    def front(self):
        return self.heap[0]

    def make_heap(self, values, comp=_standard_comp):
        for index, value in enumerate(values):
            self.heap.append([index, 0, value])

        _size = self.size()

        for index in reversed(range(0, _size // 2)):
            self._heapify(_size, index, comp)


    def pop_heap(self, comp=_standard_comp):
        pv = self.heap[0]

        self.heap_swap(0, len(self.heap)-1)
        self._heapify(len(self.heap) -1, 0, comp)

        return pv

    def sort_heap(self):
        raise Exception("heap.Heap.sort_heap() :: Not implemented.")

    def heap_swap(self, a, b):
        _a = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = _a

    def top(self):
        return self.heap[0]

    def empty(self):
        return self.heap == []

    def size(self):
        return len(self.heap)

    def pop_back(self):
        self.heap = self.heap[:-1]


    def push_heap(self, value, comp=_standard_comp):
        """
         Given a heap in the range [first,last-1), this function extends the range considered a heap to [first,last)
         by placing the value in (last-1) into its corresponding location within it.

        """
        self.heap.append(value)

        current = len(self.heap) - 1

        while current > 0:
            parent = (current - 1) // 2
            if comp(self.heap[current], self.heap[parent]):
                self.heap_swap(parent, current)
                current = parent
            else:
                break

class ExtendedHeap(Heap):

    def pop_and_feed(self, peak):
        if self.empty():
            raise Exception("heap.ExtendedHeap.pop_and_feed() :: The heap must not be empty.")

        returned_peak = self.top()

        self._standard_comp = lambda a,b: a <= b

        s_indx = returned_peak[0]
        peak_indx = returned_peak[1] + 1 # Next available peak

        self.pop_heap()

        spectra = peak[s_indx]

        if peak_indx < len(spectra):
            self.push_heap(spectra[peak_indx])
        else:
            self.pop_back()

        return returned_peak