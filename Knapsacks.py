
# Common knapsack algo implementations.
# Includes combinations of the following twists on the knapsack formla :
# - items can be used any number of times / only one time
# - items have a value, and we want to maximise the total value of the items we pack
# - we need to know the combinations of items that allow to fill the sac


# Objects are represented by their weight only,
# and may be used any number of times.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list of bool, describing for every capacity value between 0 and C,
# whether the knapsac of capacity C can be filled.
def knapsacMultiUse(C, objects) :

    sac = [0 for i in range(C+1)]
    sac[0] = 1

    for i in range(C+1) :
        for o in range(len(objects)) :
            if i-objects[o] >= 0 :
                if sac[i - objects[o]] == 1 :
                    sac[i] = 1
                    break

    return sac

# Objects are represented by their weight only,
# and may only be used one time.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list of bool, describing for every capacity value between 0 and C,
# whether the knapsac of capacity C can be filled.
def knapsacSingleUse(C, objects) :

    sac = [0 for i in range(C+1)]
    sac[0] = 1

    for o in range(len(objects)):
        for i in range(C+1)[::-1] :
            if i-objects[o] >= 0 :
                if sac[i - objects[o]] == 1 :
                    sac[i] = 1
    return sac[-1]

# Objects are represented by their weight and their value,
# and may be used any number of times.
# C :       knapsack capacity, positive integer
# objects :  list of every object size and value ((int, int) tuples)
# returns a list of bool, describing for every capacity value between 0 and C,
# the highest value sum that can be packed.
def knapsacMultiUseOpti(C, objects) :

    sac = [0 for i in range(C+1)]

    for i in range(C+1) :
        for o in range(len(objects)) :
            if i-objects[o][0] >= 0 :
                if sac[i - objects[o][0]] + objects[o][1] > sac[i] :
                    sac[i] = sac[i - objects[o][0]] + objects[o][1]

    return sac

# Objects are represented by their weight and their value,
# and may only be used one time.
# C :       knapsack capacity, positive integer
# objects :  list of every object size and value ((int, int) tuples)
# returns a list of bool, describing for every capacity value between 0 and C,
# the highest value sum that can be packed.
def knapsacSingleUseOpti(C, objects) :

    sac = [0 for i in range(C+1)]

    for o in range(len(objects)):
        for i in range(C+1)[::-1] :
            if i-objects[o][0] >= 0 :
                if sac[i - objects[o][0]] + objects[o][1] > sac[i] :
                    sac[i] = sac[i - objects[o][0]] + objects[o][1]
    return sac

# Objects are represented by their weight only,
# and may be used any number of times.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list[set[tuple(int, ...)]], describing for every capacity value between 0 and C,
# all different ways the knapsac of capacity C can be filled (list of object indices).
def knapsacMultiUsePath(C, objects) :

    sac = [set() for i in range(C+1)]

    for i in range(C+1) :
        for o in range(len(objects)) :
            if i-objects[o] >= 0 :
                if i-objects[o] == 0 :
                    sac[i].add(tuple([o]))
                if len(sac[i - objects[o]]) != 0 :
                    for combination in sac[i - objects[o]] :
                        newComb = list(combination)
                        newComb.append(o)
                        sac[i].add(tuple(elt for elt in sorted(newComb)))

    return sac

# Objects are represented by their weight only,
# and may only be used one time.
# C :       knapsack capacity, positive integer
# objects :  list of every object size (positive integers)
# returns a list[set[tuple(int, ...)]], describing for every capacity value between 0 and C,
# all different ways the knapsac of capacity C can be filled (list of object indices).
def knapsacSigneUsePath(C, objects) :

    sac = [set() for i in range(C+1)]

    for o in range(len(objects)):
        for i in range(C+1)[::-1] :
            if i-objects[o] >= 0 :
                if i-objects[o] == 0 :
                    sac[i].add(tuple([o]))
                if len(sac[i - objects[o]]) != 0 :
                    for combination in sac[i - objects[o]] :
                        newComb = list(combination)
                        newComb.append(o)
                        sac[i].add(tuple(elt for elt in sorted(newComb)))

    return sac




# code for testing

C = 10
objets = [1, 2, 4, 7, 12]
objets2 = [[1, 2], [2, 5], [7, 17], [9, 20]]

result = knapsacSigneUsePath(C, objets)
for i in range(len(result)) :
    print("\ncapacity " + str(i) + " :")
    for comb in result[i] :
        print(comb)
