import tracemalloc
import time

tracemalloc.start()

def snapshot(label):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{label} | Current: {current / 1024:.2f}KB | Peak: {peak / 1024:.2f}KB")

snapshot("Start")

leaky = []
for _ in range(10_000):
    leaky.append("x" * 10_000)

snapshot("After allocations")
