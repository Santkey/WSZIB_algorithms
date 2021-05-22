def PI_15(n_15):
    pi_15 = 0  
    for i_15 in range(1, n_15):
        x_15 = 4 * (i_15 ** 2)
        y_15 = x_15 - 1
        z_15 = float(x_15)/float(y_15)
        if (i_15 == 1):
            pi_15 = z_15
        else:
            pi_15 *= z_15
    pi_15 *= 2
    return pi_15
print("Wynik PI obliczony metodą Willisa: ", PI_15(1000000))