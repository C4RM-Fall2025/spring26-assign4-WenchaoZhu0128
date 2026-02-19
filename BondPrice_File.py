

def getBondPrice(y, face, couponRate, m, ppy=1):
    y = y / ppy
    couponRate = couponRate / ppy
    m = m * ppy
    pvcfsum = 0

    for t in range(1, m+1):
        pvm = (1+y)**(-t)
        cf = face * couponRate
        if t == m:
            cf = cf + face
        pvcf = pvm * face
        pvcfsum = pvcfsum + pvcf
    return pvcfsum
