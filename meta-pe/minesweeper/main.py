import random

# grid size m x n k=no of points
def generate_random_points(m, n, k):
    result = set()
    while len(result) < k:
        r = random.randrange(m)
        c = random.randrange(n)
        point = (r,c)
        if point not in result:
            result.add(point)
    
    return list(result)

def generate_random_points_v2(m: int, n: int, k: int) -> List[Tuple[int, int]]:
    all_points = [(i, j) for i in range(m) for j in range(n)]
    return random.sample(all_points, k)

