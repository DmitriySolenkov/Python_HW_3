from itertools import combinations

items_weight = {
    'tent': 10,
    'sleeping bag': 5,
    'food': 3,
    'medkit': 4,
    'stove': 7,
    'flashlight': 1
}
max_weight = 14
backpack_items_combinations = []
for i in range(len(items_weight)):
    for combination in combinations(items_weight, i):
        total_weight = sum(items_weight[k] for k in combination)
        if total_weight <= max_weight:
            backpack_items_combinations.append(list(combination))

for i, combination in enumerate(backpack_items_combinations, start=1):
    print(f'{i}: {combination}')
