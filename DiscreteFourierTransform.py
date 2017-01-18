## HW 4 Number 1
## Billy Babis
## October, 2015

##This is my implementation of the popular Discrete-Fourier Transform (DFT)
## DFT converts a finite continous sequence with n intervals into a more discrete
## distribution to illuminate trends. The common idiom to describe what DFT does is
## "Given a smoothie, it finds the recipe". In context, it can refer to digital
## signal processing of audio or visuals.

## Python does not have an easy way to deal with complex numbers
## so my simple implementation simply seperates the real and complex numbers
## thus, the X_n value will be realNumInputs[n] + complexNumInputs[n]

import math

def dft(realNumInputs, complexNumInputs):
    N = len(realNumInputs)
    ## N must also equal len(complexNumInputs)

    realNumOutputs = []
    complexNumOutputs = []

    for k in range(N):
        ##for a give X(k) value, we will find the Sums from n=0-->n=N-1
        realSum = 0
        imaginarySum = 0
        for n in range(N):
            xn_real = realNumInputs[n]
            xn_im = complexNumInputs[n]
            
            exp = (-2.0*math.pi*k*n)/N
            
            ## find values for real input
            ## e**(exponent*i) = cos(exponent) + isin(exponent)
            exp_real = math.cos(exp)
            exp_im = math.sin(exp)
            
            output_real = xn_real*exp_real - xn_im*exp_im
            output_im = xn_real*exp_im + xn_im*exp_real
            
            realSum += output_real
            imaginarySum += output_im

        realNumOutputs.append(realSum)
        complexNumOutputs.append(imaginarySum)

    return [realNumOutputs, complexNumOutputs]

def dft_inverse(realNumInputs, complexNumInputs):
    N = len(realNumInputs)
    realNumOutputs = []
    complexNumOutputs = []
    for n in range(N):
        realSum = 0
        imSum = 0
        for k in range(N):
            Xk_real = realNumInputs[k]
            Xk_im = complexNumInputs[k]

            exp = (2*math.pi*k*n)/float(N)

            exp_real = math.cos(exp)
            exp_im = math.sin(exp)

            output_real = Xk_real*exp_real - Xk_im*exp_im
            output_im = Xk_real*exp_im + Xk_im*exp_real

            realSum += output_real
            imSum += output_im
        realNumOutputs.append(realSum*(1.0/float(N)))
        complexNumOutputs.append(imSum*(1.0/float(N)))
    return (realNumOutputs, complexNumOutputs)


