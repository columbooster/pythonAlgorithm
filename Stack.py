# 재귀함수
def recursive(data):
    if data<0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned",data)

        recursive(4)


data_stack = list()

data_stack.append(1)
data_stack.append(2)

data_stack

data_stack.pop()

stack_list = list()


def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

    pop()