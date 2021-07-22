l = ['a', 'b', 'c', 'd']

# i:int = 0
# for item in l:
#     if i & 1:
#         print(item)
#     i += 1


for i, item in enumerate(l):
    if i & 1:
        print(item)


