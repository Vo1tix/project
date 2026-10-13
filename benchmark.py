import random
import statistics
import time

import matplotlib.pyplot as plt

from history import HalfHistory, OneHistory


ELEMENT_BYTES = 8


def measure(cls, capacity, actions, repeats=5):
    for _ in range(2):
        h = cls(capacity)
        s = 0
        for a in actions:
            h.add(a)
            s += a

    times = []
    last_sum = 0

    for _ in range(repeats):
        h = cls(capacity)
        s = 0

        start = time.perf_counter_ns()
        for a in actions:
            h.add(a)
            s += a
        end = time.perf_counter_ns()

        times.append(end - start)
        last_sum = s

    median_total = statistics.median(times)
    per_add = median_total / len(actions)

    print(
        cls.__name__,
        "capacity =",
        capacity,
        "per_add_ns =",
        round(per_add, 2),
        "sum =",
        last_sum,
    )
    return per_add


def main():
    capacities = [32, 64, 128, 256, 512, 1024, 2048, 4096]
    additions = 50000

    random.seed(123)
    actions = [random.randint(0, 10**9) for _ in range(additions)]

    x_bytes = []
    half_times = []
    one_times = []

    for b in capacities:
        x_bytes.append(b * ELEMENT_BYTES)
        half_times.append(measure(HalfHistory, b, actions))
        one_times.append(measure(OneHistory, b, actions))

    plt.figure(figsize=(10, 6))
    plt.plot(x_bytes, half_times, marker="o", label="отбрасываем половину")
    plt.plot(x_bytes, one_times, marker="s", label="отбрасываем одно старое")
    plt.xscale("log", base=2)
    plt.xlabel("Объём массива истории, байт (b * 8)")
    plt.ylabel("Время на одно добавление, нс")
    plt.title("Амортизированное время добавления действия")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graph.png")
    plt.show()


if __name__ == "__main__":
    main()