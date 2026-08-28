import time


def bench(fn, n=1000):
    t0 = time.perf_counter()
    for _ in range(n):
        fn()
    dt = time.perf_counter() - t0
    print("%d calls in %.3fs (%.1f us/call)"
          % (n, dt, dt / n * 1e6))


if __name__ == "__main__":
    bench(lambda: sum(range(100)))
