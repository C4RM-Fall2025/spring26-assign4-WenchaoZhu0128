
def getBondDuration(y, face, couponRate, m, ppy = 1):
    couponRate = couponRate / ppy
    m = m * ppy
    y = y / ppy
    pvcfsum = 0
    weightedTimeSum = 0

    for t in range(1, m+1):
        pvm = (1+y)**(-t)
        cf = face * couponRate
        if t == m:
            cf = cf + face
        pvcf = pvm * cf
        pvcfsum = pvcfsum + pvcf
        weightedTimeSum = weightedTimeSum + pvcf * t

    BondDuration = (weightedTimeSum / pvcfsum) / ppy
    return(BondDuration)
