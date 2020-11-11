
# Common knapsack algos implementations.
# Includes combinations of the following twists on the knapsack formula :
# - items can be used any number of times / only one time
# - items have a value, and we want to maximise the total value of the items we pack
# - we need to know the combinations of items that allow to fill the sack


# Objects are represented by their weight only,
# and may be used any number of times.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list of bool, describing for every capacity value between 0 and C,
# whether the knapsack of capacity C can be filled.
def knapsackMultiUse(C, objects) :

    sack = [0 for i in range(C+1)]
    sack[0] = 1

    for i in range(C+1) :
        for o in range(len(objects)) :
            if i-objects[o] >= 0 :
                if sack[i - objects[o]] == 1 :
                    sack[i] = 1
                    break

    return sack

# Objects are represented by their weight only,
# and may only be used one time.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list of bool, describing for every capacity value between 0 and C,
# whether the knapsack of capacity C can be filled.
def knapsackSingleUse(C, objects) :

    sack = [0 for i in range(C+1)]
    sack[0] = 1

    for o in range(len(objects)):
        for i in range(C+1)[::-1] :
            if i-objects[o] >= 0 :
                if sack[i - objects[o]] == 1 :
                    sack[i] = 1
    return sack

# Objects are represented by their weight and their value,
# and may be used any number of times.
# C :       knapsack capacity, positive integer
# objects :  list of every object size and value ((int, int) tuples)
# returns a list of bool, describing for every capacity value between 0 and C,
# the highest value sum that can be packed.
def knapsackMultiUseOpti(C, objects) :

    sack = [0 for i in range(C+1)]

    for i in range(C+1) :
        for o in range(len(objects)) :
            if i-objects[o][0] >= 0 :
                if sack[i - objects[o][0]] + objects[o][1] > sack[i] :
                    sack[i] = sack[i - objects[o][0]] + objects[o][1]

    return sack

# Objects are represented by their weight and their value,
# and may only be used one time.
# C :       knapsack capacity, positive integer
# objects :  list of every object size and value ((int, int) tuples)
# returns a list of bool, describing for every capacity value between 0 and C,
# the highest value sum that can be packed.
def knapsackSingleUseOpti(C, objects) :

    sack = [0 for i in range(C+1)]

    for o in range(len(objects)):
        for i in range(C+1)[::-1] :
            if i-objects[o][0] >= 0 :
                if sack[i - objects[o][0]] + objects[o][1] > sack[i] :
                    sack[i] = sack[i - objects[o][0]] + objects[o][1]
    return sack

# Objects are represented by their weight only,
# and may be used any number of times.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list[set[tuple(int, ...)]], describing for every capacity value between 0 and C,
# all different ways the knapsack of capacity C can be filled (list of object indices).
def knapsackMultiUsePath(C, objects) :

    sack = [set() for i in range(C+1)]

    for i in range(C+1) :
        for o in range(len(objects)) :
            if i-objects[o] >= 0 :
                if i-objects[o] == 0 :
                    sack[i].add(tuple([o]))
                if len(sack[i - objects[o]]) != 0 :
                    for combination in sack[i - objects[o]] :
                        newComb = list(combination)
                        newComb.append(o)
                        sack[i].add(tuple(elt for elt in sorted(newComb)))

    return sack

# Objects are represented by their weight only,
# and may only be used one time.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list[set[tuple(int, ...)]], describing for every capacity value between 0 and C,
# all different ways the knapsack of capacity C can be filled (list of object indices).
def knapsackSingleUsePath(C, objects) :

    sack = [set() for i in range(C+1)]

    for o in range(len(objects)):
        for i in range(C+1)[::-1] :
            if i-objects[o] >= 0 :
                if i-objects[o] == 0 :
                    sack[i].add(tuple([o]))
                if len(sack[i - objects[o]]) != 0 :
                    for combination in sack[i - objects[o]] :
                        newComb = list(combination)
                        newComb.append(o)
                        sack[i].add(tuple(elt for elt in sorted(newComb)))

    return sack




# --- testing code ---

# C = 10
# objects = [2, 4, 7, 12]
# print(knapsackMultiUse(C, objects))
# --- results :
# --- sack = [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]


# C = 10
# objects = [2, 4, 7, 12]
# print(knapsackSingleUse(C, objects))
# --- results :
# --- sack = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]


# C = 10
# objects = [[1, 2], [2, 5], [7, 17], [9, 20]]
# print(knapsackMultiUseOpti(C, objects))
# --- results :
# --- sack = [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25]


# C = 10
# objects = [[1, 2], [2, 5], [7, 17], [9, 20]]
# print(knapsackSingleUseOpti(C, objects))
# --- results :
# --- sack = [0, 2, 5, 7, 7, 7, 7, 17, 19, 22, 24]


# C = 10
# objects = [2, 3, 5, 6]
# result = knapsackMultiUsePath(C, objects)
# for i in range(len(result)) :
#     print("\ncapacity " + str(i) + " :")
    # for comb in result[i] :
    #     print(comb)
# --- results :
# --- capacity 0 : 0 combination
# --- capacity 1 : 0 combination
# --- capacity 2 : 1 combination
# --- capacity 3 : 1 combination
# --- capacity 4 : 1 combination
# --- capacity 5 : 2 combination
# --- capacity 6 : 3 combination
# --- capacity 7 : 2 combination
# --- capacity 8 : 4 combination
# --- capacity 9 : 4 combination
# --- capacity 10 : 5 combination



# C = 10
# objects = [2, 3, 5, 6]
# result = knapsackSingleUsePath(C, objects)
# for i in range(len(result)) :
#     print("\ncapacity " + str(i) + " :")
#     for comb in result[i] :
#         print(comb)
# --- results :
# --- capacity 0 : 0 combination
# --- capacity 1 : 0 combination
# --- capacity 2 : 1 combination
# --- capacity 3 : 1 combination
# --- capacity 4 : 0 combination
# --- capacity 5 : 2 combinations
# --- capacity 6 : 1 combination
# --- capacity 7 : 1 combination
# --- capacity 8 : 2 combinations
# --- capacity 9 : 1 combination
# --- capacity 10 : 1 combination

