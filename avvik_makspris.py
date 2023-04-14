def hent_maks_priser(sone):
    priser = []

    with open(f"data/priser/max/{sone}.txt", "r") as file:
        priser = file.read().split("\n")
        priser = [float(x) for x in priser]
        return priser

    return None

def hent_gj_priser(sone):
    priser = []
    
    with open(f"data/priser/{sone}.txt", "r") as file:
        priser = file.read().split("\n")
        priser = [float(x) for x in priser]
        return priser
    
    return None

def hent_min_priser(sone):
    priser = []
    with open(f"data/priser/min/{sone}.txt", "r") as file:
         priser = file.read().split("\n")
         priser = [float(x) for x in priser]
         return priser
    return None

def hovedprogram():
    sonee = {
        "NO1": 1,
        "NO2": 2,
        "NO3": 3,
        "NO4": 4,
        "NO5": 5
    }
    for sone in sonee:
        print(f"Sone: {sone}")
        
        maks_priser = hent_maks_priser(sone)
        gj_priser = hent_gj_priser(sone)
        min_priser = hent_min_priser(sone)

        s_diff_min_gj = 0
        s_diff_max_gj = 0

        for i in range(len(maks_priser)):
            s_diff_min_gj += maks_priser[i] - gj_priser[i]
            s_diff_max_gj += gj_priser[i] - min_priser[i]

        s_diff_min_gj = s_diff_min_gj / len(gj_priser)
        s_diff_max_gj = s_diff_max_gj / len(gj_priser)

        print(s_diff_min_gj)
        print(s_diff_max_gj)

hovedprogram()