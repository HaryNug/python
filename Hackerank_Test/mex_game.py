def get_max_mex(arr):  # ?/15
    print(f"initial: {arr}")
    arr.sort()
    for i, num in enumerate(arr):
        for x in range(0, num):
            if x not in arr:
                arr[i] = x
                # break
    print(f"reduced: {arr}")
    mex = max(arr) + 1
    print(f"mex    :  {mex}\n")