#Function 3 : No Parameter/Have Return ***
def funcA( ) :
    print('AAA')
    print('BBB')
    return 'Wow Wow Wow'

def funcB( ) :
    return 999, True, 10 + 20

# funcA( ) เขียนได้ แต่เขาไม่ทํากัน
print( funcA( ) )
x = funcA( )

a, b, c = funcB( ) #***
print(f'{a} {b} {c}')