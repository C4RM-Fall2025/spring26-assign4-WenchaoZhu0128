

def getBondPrice_E(face, couponRate, yc):
    pvcfsum = 0
    m = len(yc)

    for i, y in enumerate(yc):
        t = i + 1
        pvm = (1+y)**(-t)
        cf = face * couponRate
        if i == m - 1:
            cf = cf + face
        pvcf = pvm * cf
        pvcfsum = pvcfsum + pvcf
    return(pvcfsum)
