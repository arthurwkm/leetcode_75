def equalRowsAndColumns(grid):
    arrs = {}
    valid_pairs = 0

    for i, a in enumerate(grid):
        row = str(a)
        col = str([j[i] for j in grid])

        if row in arrs.keys():
            arrs[row] += "c"
        else:
            arrs[row] = "c"
        
        if col in arrs.keys():
            arrs[col] += "r"
        else:
            arrs[col] = "r"
    print(arrs)
    for key in arrs:
        if len(arrs[key]) > 1:
            valid_pairs+=arrs[key].count("r")* arrs[key].count("c")
    
    return valid_pairs


print(equalRowsAndColumns([[3,2,1],[1,7,6],[2,7,7]]))
print(equalRowsAndColumns([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(equalRowsAndColumns([[13, 13], [13, 13]]))
print(equalRowsAndColumns([[13, 13, 13], [13, 13, 13], [13, 13, 13]]))