def converter(json_array : list[dict]) -> dict[int,dict]:
    mp = {}
    for i in range(len(json_array)):
        mp.setdefault(i,json_array[i])

    return mp