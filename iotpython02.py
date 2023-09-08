#Function 2 : Haze Parameter/No Return
#parameter คือตัวแปรประเภทหนึ่ง ขอบเขตการใช่งานพารามิเตอร์
# จะใช้ได้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น

def funcA( x, y ) :
    print('Hi...')
    z = x + y
    print(f'{x} + {y} = {z}')
    #ไม่มีคําสั่ง return

def funcB( x ) : 
    print(f"X is {x} 555...")

funcA(10, 20) #Argument       
funcA(5, 5)       
funcB( 'SAU IoT')