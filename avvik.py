def printsone(sone):
    gj_priser = []
    min_priser = []
    max_priser = []

    with open(f"data/priser/{sone}.txt", "r") as file:
        gj_priser = [float(x) for x in file.read().split("\n")]

    with open(f"data/priser/min/{sone}.txt", "r") as file:
        min_priser = [float(x) for x in file.read().split("\n")]

    with open(f"data/priser/max/{sone}.txt", "r") as file:
        max_priser = [float(x) for x in file.read().split("\n")]

    print(f"Sone: {sone}")
    
    sum_min_diff = 0
    sum_max_diff = 0

    for i in range(len(gj_priser)):
        sum_min_diff += gj_priser[i] - min_priser[i]
        sum_max_diff += max_priser[i] - gj_priser[i]

    mine = sum_min_diff / len(gj_priser)
    maxe = sum_max_diff / len(gj_priser)

    print(f"max_diff: {maxe}")
    print(f"min_diff: {mine}")

def hovedprogram():
    soner = ["NO1", "NO2", "NO3", "NO4", "NO5"]
    for sone in soner:
        printsone(sone)

hovedprogram()