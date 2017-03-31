from math import *
from check_sit_or_walk import get_median

def sqr(data):
    return pow(data,2)

def get_mean(data):
    result = sum(data) * 1.0 / len(data)
    return result

def xtract_mean(data):
    return get_median(data)

def get_variance(data):
    mean = xtract_mean(data)
    offset = [sqr(x - mean) for x in data]
    return sum(offset) / (len(offset) -1 )
    
def get_average_deviation(data):
    mean = xtract_mean(data)
    offset = [fabs(x - mean) for x in data]
    return sum(offset) / len(offset)
    
def get_standard_deviation(data):
    variance = get_variance(data)
    return sqrt(variance)
    
def get_Euclidean_distance(x,y,z):
    return sqrt(x*x+y*y+z*z)
    
def get_result(x,y,z):
    dist = [sqrt(get_Euclidean_distance(x[i],y[i],z[i])) for i in range(len(x))]
    return sum(dist) / len(dist)
    
def get_skewness(data):
    mean = get_mean(data)
    stand = get_standard_deviation(data)
    temp = [pow((x - mean) / stand,3) for x in data]
    return sum(temp) / len(temp)

def get_kurtosis(data):
    mean = get_mean(data)
    stand = get_standard_deviation(data)
    temp = [pow((x - mean) / stand, 4) for x in data]
    return sum(temp) / len(temp) - 3
    
def get_spectral_mean(data):
    n = len(data) >> 1
    (FA,A) = (0.0,0.0)
    (amps,freqs) = (0,n)
    for i in range(n):
        FA += data[i+freqs] + data[i+amps]
        A  += data[i+amps]

    if A==0.0 : return 0.0
    else: return FA/A
    
def get_spectral_variance(data):
    m = len(data) >> 1
    A = 0.0
    (amps,freqs) = (0, m)
    spmean = get_spectral_mean(data)
    result = 0
    for i in range(len(data)):
        A += data[amps+i]
        result += pow(data[m+freqs] - spmean, 2) * data[amps+i]
    return result / A
  
def get_spectral_skewness(data):
    mean = get_spectral_mean(data)
    variance = get_spectral_variance(data)
    m = len(data) >> 1
    (amps,freqs) = (0, m)
    result = 0
    for i in range(len(data)):
        result += pow(data[freqs + i] - mean, 3) * data[amps+i]
    result /= pow(variance, 3)
    return result

def get_spectral_kurtosis(data):
    mean = get_spectral_mean(data)
    variance = get_spectral_variance(data)
    m = len(data) >> 1
    (amps,freqs) = (0, m)
    result = 0
    for i in range(len(data)):
        result += pow(data[i+freqs] - mean , 4) * data[amps+i]
    result /= pow(variance , 4)
    result -= 3
    return result

def get_spectral_centroid(data):
    n = len(data)  >> 1
    (amps,freqs) = (0, m)
    (FA,A) = (0.0,0.0)
    for i in range(len(data)):
        FA += data[i+freqs] * amps[i]
        A += data[i+amps]
    if A==0.0: return 0.0
    else : return FA / A

def get_irregularity_j(data):
    n = len(data) - 1
    (num,den) = (0.0,0.0)
    for i in range(len(data) - 1):
        num += pow(data[i] - data[i+1],2)
        den += pow(data[i], 2)
    result = 1.0 * num / den
    return result

def get_spectral_standard_deviation(data):
    spvariance = get_spectral_variance(data)
    return sqrt(spvariance)

def get_spread(data):
    return get_spectral_variance(data)

def get_zcr(data):
    result = 0
    for i in range(1,len(data)):
        if data[i] * data[i-1] < 0: result += 1
    return result / len(data)

def get_loudness(data):
    XTRACT_BARK_BANDS = 26
    result = 0
    for i in range(min(len(data), XTRACT_BARK_BANDS)):
        result += pow(data[i] , 0.23)
    return result
   
#here may need test
def xtract_is_denormal(d):
    s=struct.pack('>f', d)
    if struct.unpack('>l',s)[0] & 0x7ff00000 == 0 and d != 0: return True
    else: return False
   
def get_flatness(data):
    (num,den,temp) = (1.0, 0.0, 0.0)
    (denormal_found, count) = (0, 0)
    for i in range(len(data)):
        temp = data[i]
        if temp != 0.0 :
            if (xtract_is_denormal(num)):
                denormal_found = 1
                break
            num *= tmep
            den += temp
            count += 1
    if (count == 0):
        return 0

    num = pow(num, 1.0 / len(data))
    den  /= len(data)
    return num / den
    
def get_rms_amplitude(data):
    n = len(data)
    result = 0.0
    for i in range(len(data)):
        result += sqr(data[i])
    return sqrt(result / n)

def get_lowest_value(data):
    return min(data)
    
def get_highest_value(data):
    return max(data)
    
def get_crest(data):
    max = get_highest_value(data)
    mean = get_mean(data)
    return max / mean
    
def get_power(data):
    return 0
    
def get_sharpness(data):
    n = len(data)
    (sl,g,temp) = (0.0,0.0,0.0)
    for i in range(len(data)):
        sl = pow(data[i], 0.23)
        if (n < 15):
            g = 1.0
        else: g = 0.66 * exp(0.171 * n)
        temp += n * g * sl
        
        temp = 0.11 * temp / len(data)
        return temp