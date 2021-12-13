import random
import asyncio

L = list(range(16))
random.shuffle(L)
LL = L.copy()

async def merge(b0, b1, e1, n):
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
    print(f'    {n}')
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]

async def joiner():
    tasks = []
    n = 0
    for p in range(4):
        b = 2**(p + 1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n)))
            n += 1
        await asyncio.gather(*tasks)
        tasks.clear()

asyncio.run(joiner())
print(L)

async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task

asyncio.run(main())
