import random
import asyncio
from collections import defaultdict

L = eval(input())
LL = L.copy()

async def merge(b0, b1, e1, event, eventleft, eventright):
    await eventleft.wait()
    await eventright.wait()
    b = b0
    e0 = b1
    i = b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    event.set()

async def joiner():
    events = defaultdict(asyncio.Event)
    tasks = []
    for p in range(4):
        b = 2**(p + 1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, events[f'{i}-{i + b}'], events[f'{i}-{i + b // 2}'], events[f'{i + b // 2}-{i + b}'])))
    for i in range(16):
        events[f'{i}-{i + 1}'].set()
    await asyncio.gather(*tasks)

asyncio.run(joiner())
print(L)
