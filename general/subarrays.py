def print_subarrays(arr):
    N = len(arr)
    for i in range(N):
        for j in range(i+2, N):
            print(arr[i:j])


def permutations(arr, path):
    if len(path) == 3:
        print(path)
        return
    for num in arr:
        if path:
            if num > path[-1]:
                path.append(num)
                permutations(arr, path)
                path.pop()
        else:
            path.append(num)
            permutations(arr, path)
            path.pop()


    

a = [1,2,3,4,5]
permutations(a, [])
