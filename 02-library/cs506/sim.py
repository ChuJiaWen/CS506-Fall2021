def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    intersection = len(set(x).intersection(set(y)))
    union = len(set(x).union(set(y)))
    if union == 0:
        return ValueError("lengths must not be zero")
    return 1-(float(intersection)/union)

def cosine_sim(x, y):
    dot = sum(a*b for a, b in zip(x, y))
    norm_x = sum(a*a for a in x) ** 0.5
    norm_y = sum(b*b for b in y) ** 0.5
    if norm_x*norm_y == 0:
        return ValueError
    return dot / (norm_x*norm_y)

# Feel free to add more