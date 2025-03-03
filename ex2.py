class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1) # Correcting positioning.

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        # Reordering heap.
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

tarefas = [(3, "Tarefa A"), (1, "Tarefa B"), (2, "Tarefa C")]

heap = MinHeap()

for i in tarefas:
    heap.insert(i)

while len(heap.heap) > 0:
    prioridade, tarefa = heap.pop()
    print(f"{tarefa} - {prioridade}")
