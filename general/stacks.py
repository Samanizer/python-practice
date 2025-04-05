from collections import deque

stack = []
stack.append(10)
stack.append(11)
stack.append(12)
stack.append(13)

print(stack)
print("After pop")
stack.pop()
print(stack)
print("Length: ", len(stack))
print("First Item:", stack[0])
print("Last Item: ", stack[len(stack)-1])

que = deque()
que.append(1)
que.append(2)
que.append(3)
print("Que: ", que)
que.appendleft(0)
que.extendleft([-1,-2])
print("Que: ", que)
que.popleft()
print("Que: ", que)

l = [1,2,3,4,5,6]
l.remove(3)
print(l)

for i in range(1):
    print("i",i)
