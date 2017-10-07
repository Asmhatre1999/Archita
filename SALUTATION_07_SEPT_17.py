print('salutations')
a=float(input('enter the time in am and pm:'))
if(a>=4 and a<=12):
    print('GOOD MORNING')
elif(a>12 and a<=16):
    print('GOOD AFTERNOON')
elif(a>16 and a<=20):
    print('GOOD EVENING')
else:
    print('GOOD NIGHT')
