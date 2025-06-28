
import random
random.seed(42)


ids1 = random.sample(range(-10_000_000, 10_000_000), 10_000_000)

ids2 = random.sample(range(-1_000_000, 1_000_000), 2_000)

# print()
# print("ids1:")
# print(ids1[0:5])
# print()
# print("ids2:")
# print(ids2[0:5])

ids1_dict = {}
for num in ids1:
    ids1_dict[num] = True




matches = 0

for i in range(len(ids2)):

    # # # list attempt
    # if ids2[i] in ids1:
    #     matches = matches + 1

    # dict attempt
    if ids2[i] in ids1_dict:
        matches = matches + 1   


    if i % 100 == 0:
        print(f"{round(i/len(ids2)*100,3)} percent complete")

print(f"{matches} matches found")

