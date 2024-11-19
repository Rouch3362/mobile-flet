import flet

def oneLengthToOther(cm,inc,ft,mi,kl):
    
    if cm: 
        inc = str(round(float(cm) / 2.54, 2))
        ft  = str(float(cm) / 30.48)
        mi  = str(float(cm) / 160900)
        kl  = str(float(cm) / 100000)
    
    elif inc:
        cm  = str(round(float(inc) * 2.54, 2))
        ft  = str(round(float(inc) / 12, 2))
        mi  = str(float(inc) / 63360)
        kl  = str(float(inc) / 39370)

    elif ft:
        cm  = str(round(float(ft) * 30.48, 2))
        inc = str(round(float(ft) * 12, 2))
        mi  = str(float(ft) / 5280)
        kl  = str(float(ft) / 3281)

    elif mi:
        cm  = str(round(float(mi) * 160900, 2))
        inc = str(round(float(mi) * 63360, 2))
        ft  = str(round(float(mi) * 5280, 2))
        kl  = str(round(float(mi) * 1.609, 2))

    elif kl:
        cm  = str(round(float(kl) * 100000, 2))
        inc = str(round(float(kl) * 39370, 2))
        ft  = str(round(float(kl) * 3281, 2))
        mi  = str(round(float(kl) / 1.609, 2))


    return cm, inc, ft, mi, kl
    
    

def oneWeightToOther(gram,kilo,pound,ounce):
    if gram:
        kilo  = str(round(float(gram) / 1000 ,4))
        pound = str(round(float(gram) / 4536 ,4))
        ounce = str(round(float(gram) / 2835 ,4))

    elif kilo:
        gram  = str(round(float(kilo) * 1000 ,4))
        pound = str(round(float(kilo) * 2205 ,4))
        ounce = str(round(float(kilo) * 35274 ,4))

    elif pound:
        gram  = str(round(float(pound) * 4536 ,4))
        kilo  = str(round(float(pound) / 2205 ,4))
        ounce = str(round(float(pound) * 16 ,4))

    elif ounce:
        print('uf')
        gram  = str(round(float(ounce) * 28.34952 ,4))
        kilo  = str(round(float(ounce) * 0.02835 ,4))
        pound = str(round(float(ounce) / 16 ,4))

    return gram, kilo, pound, ounce



def oneDataToOthers(byte, megabyte, gigabyte, terabyte):
    if byte:
        megabyte = str(float(byte) / 1e+6)
        gigabyte = str(float(byte) / 1e+9)
        terabyte = str(float(byte) / 1e+12)
    elif megabyte:
        byte = str(round(float(megabyte) * 1e+6, 2))
        gigabyte = str(round(float(megabyte) / 1024, 2))
        terabyte = str(round(float(megabyte) / 1e+6, 2))
    elif gigabyte:
        byte = str(round(float(gigabyte) * 1e+9, 2))
        megabyte = str(round(float(gigabyte) * 1024, 2))
        terabyte = str(round(float(gigabyte) / 1024, 2))

    elif terabyte:
        byte = str(round(float(terabyte) * 1e+12, 2))
        megabyte = str(round(float(terabyte) * 1e+6, 2))
        gigabyte = str(round(float(terabyte) * 1024, 2))

    return byte, megabyte, gigabyte, terabyte