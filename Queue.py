# 큐 Queue

# 줄을 서는 행위와 유사 FIFO, LILO 방식으로 스택과 꺼내는 순서가 반대

import queue

data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)

data_queue.qsize()

data_queue.get()

data_queue.qsize()

data_queue.get()

data_queue.qsize()

# LifoQueue() 로 큐 만들기 (LIFO)

data_queue1 = queue.LifoQueue()

data_queue1.put("funcoding")
data_queue1.put(1)

data_queue1.qsize()

data_queue1.get()

# PriorityQueue()로 큐 만들기

data_queue2 = queue.PriorityQueue()

data_queue2.put((10,"korea"))
data_queue2.put((5,1))
data_queue2.put((15,"china"))

data_queue2.qsize()

data_queue2.get()

# 어디에 큐가 많이 쓰일까?
# 멀티 태스킹을 위한 프로세스 스케줄링 방식을 구현하기 위해 많이 사용된다(운영체제 참조)

# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

len(queue_list)

dequeue()