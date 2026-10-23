def medyanHesaplama(arr: list):
    uzunluk = len(arr)
    if uzunluk%2 == 0:
        medyan = (arr[(len/2)-1] + arr[len/2])/2.0
    else:
        medyan = arr(((len+1)/2)-1)
    return medyan
