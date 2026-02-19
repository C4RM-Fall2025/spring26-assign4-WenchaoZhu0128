

def getBondPrice_E(face, couponRate, yc):
    pvcfsum = 0
    m = len(yc)

    for t in range(1, m+1):
        y = yc[t-1]
        pvm = (1+y)**(-t)
        cf = face * couponRate
        if t == m:
            cf = cf + face
        pvcf = pvm * cf
        pvcfsum = pvcfsum + pvcf
    return(pvcfsum)
