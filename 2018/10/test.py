from scipy import stats

nums = [1, 2, 3, 1, 2, 3, 1, 4, 1, 1, -1, 2, 1]
result = stats.mode(nums)

item = result.mode[0]
item_n_occurences = result.count[0]
print(item, item_n_occurences)
