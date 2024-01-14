
from scipy.stats import norm
from math import sqrt

def dnorm(x,mean=0,sd =1):
    result = norm.pdf(x,loc=mean,scale=sd)
    return result

x= -2
print(dnorm(x,mean=-2,sd =sqrt(0.5)))



from numpy import random

def ExNormale(fMu, fSigma):
    fRet = random.normal((fMu,fSigma,1))
    return fRet