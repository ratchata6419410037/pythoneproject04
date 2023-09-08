#หาพื้นที่



def inputWitdhLong( ) :
    wi = float( input('ป้อนกว้าง : ') )
    lo = float( input('ป้อนยาว : ') )
    return wi, lo

def inputBaseHight( ) :
    ba = float( input('ป้อนฐาน : ') )
    hi = float( input('ป้อนสูง : ') )
    return ba, hi

def calAndShowAreaSquare( wi, lo ) :
    area = wi * lo
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}')

def calAndShowAreaSquare( ba, hi ) :
    area = ba * hi / 2
    print(f'สามเหลี่ยมฐาน {wi} สูง {lo} มีพื้นที่ {area}')

wi, lo = inputWitdhLong()
calAndShowAreaSquare(wi, lo)
print('---------------------------')
ba, hi = inputBaseHight( )
calAndShowAreaSquare(ba, hi)
     
