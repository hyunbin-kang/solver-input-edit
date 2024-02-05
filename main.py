import os

filename = str(input('Enter file name : '))
f = open(filename)
A = f.readlines()
str1 = str(input('Enter variable name : ')) #variable
sweep_start = int(input('Enter start boundary :'))
sweep_end   = int(input('Enter end boundary :'))
sweep_step  = int(input('Enter boundary step size :'))


for var in range(sweep_start, sweep_end+1, sweep_step):
    if var < 0:
        dir = str1+'n'+str(abs(var))
    else:
        dir = str1+str(var)
        
    B = ''
    os.mkdir(dir)
    for i in A:
        if not str1 in i:
            B += i
        else:
            tmp = str1+'\t'+'= '+str(var)+'.0,\n'
            B += ' '+tmp
            
    with open(dir+'/'+filename, 'w') as f:
        f.write(B)