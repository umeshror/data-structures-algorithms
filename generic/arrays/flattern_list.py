sample = [1, 2, 3, 4, [5, [1, 2, 3, 4, 5, [4, [7, 8], 5]]]]


def flattern_list(arr):
    if type(arr) == list:
        # return [ele for i in arr for ele in flattern_list(i)]
        res = []
        for i in arr:
            for ele in flattern_list(i):
                res.append(ele)
        return res
    else:
        return [arr]


print(flattern_list(sample))
