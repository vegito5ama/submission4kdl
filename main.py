def min_time_for_meal(test_cases):
    results = []

    for case in test_cases:
        N, K, categories, times = case
        if len(set(categories)) < K:
            results.append(-1)
            continue

        category_to_min_time = {}

        for cat, time in zip(categories, times):
            if cat in category_to_min_time:
                category_to_min_time[cat] = min(category_to_min_time[cat], time)
            else:
                category_to_min_time[cat] = time

        if len(category_to_min_time) < K:
            results.append(-1)
            continue

        min_times = sorted(category_to_min_time.values())
        results.append(sum(min_times[:K]))

    return results


def main():
    input_data = """4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1 
1 1 0 3 5"""

    data = input_data.split()

    index = 0
    T = int(data[index])
    index += 1

    test_cases = []

    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2

        categories = list(map(int, data[index : index + N]))
        index += N

        times = list(map(int, data[index : index + N]))
        index += N

        test_cases.append((N, K, categories, times))

    results = min_time_for_meal(test_cases)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
