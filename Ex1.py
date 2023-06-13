friends_items = {
    'John': ('tent', 'sleeping bag', 'backpack', 'stove', 'food'),
    'Max': ('tent', 'sleeping bag', 'map', 'food', 'stove'),
    'Sarah': ('tent', 'sleeping bag', 'backpack', 'food', 'medkit'),
    # 'Alex': ('sleeping bag','tent','flashlight','stove')
}

friends = []
for key in friends_items:
    friends.append(key)

all_items = set(friends_items[friends[0]]).intersection(
    friends_items[friends[1]])
for i in range(2, len(friends)):
    all_items = set(all_items).intersection(friends_items[friends[i]])

print('Items, that all friends have:', all_items)

items = []
unique_items = []
for key in friends_items:
    for item in friends_items.get(key):
        items.append(item)
for item in items:
    if items.count(item) == 1:
        unique_items.append(item)

print('Unique items:', unique_items)

not_one_items = set()
for item in items:
    if items.count(item) == len(friends_items)-1:
        not_one_items.add(item)
for no_item in not_one_items:
    for key in friends_items:
        if no_item not in friends_items.get(key):
            print(f'Only {key} does not have {no_item}')
