

def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    for t, y in zip(times, yc):
        pvm = (1+y)**(-t)
        cf = face * couponRate
        if t == times[len(times)-1]:
            cf = cf + face
        pvcf = pvm * cf
        pvcfsum = pvcfsum + pvcf
    return(pvcfsum)
