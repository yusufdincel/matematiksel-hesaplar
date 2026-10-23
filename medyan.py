def medyanHesaplama(arr: list):
    uzunluk = len(arr)
    if uzunluk%2 == 0:
        medyan = (arr[(uzunluk//2)-1] + arr[uzunluk//2])/2
    else:
        medyan = arr[(((uzunluk+1)//2)-1)]
    return medyan
