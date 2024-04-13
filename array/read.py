def read(n: int, book: [int], target: int) -> str:
    seen = {}
    for i in range(n):
        potential = target - book[i]
        if potential in seen:
            return "YES"
        seen[book[i]] = True
    return "NO"


print(read(5, [3, 1, 3, 3, 1], 5))