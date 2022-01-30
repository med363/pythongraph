ch='python'
print(ch[1:])
print('*******')
print(ch[-2:])
print('********')
print(ch[-3:])
print('********')
print(ch[:-3])
print('/////////////')
ch1='med amine blibech'
print('ch2: ',ch1.title())
ch3='MED Amine Blibech'
print('ch4 ',ch3.swapcase())
print("l'indice de A est" ,ch3.find('A'))
print("l'indice de a est" ,ch3.find('a'))
print("l'indice de m est" ,ch3.find('m',2))
# print("l'indice de a est" ,ch3.index('a'))
print("commence par" ,ch3.startswith('a'))
print('liste de ch3:',ch3.split())
print('liste de ch3:',ch3.split('\n'))
print('liste de ch3:',ch3.split('\t'))
print('liste de ch3:',ch3.split(maxsplit=1))
ch4='''gfgdfd
         fdhgj 
              dfgjfkcc'''
print('liste de ch4:',ch4.split('\n'))
print('neveau de ch3:',ch3.replace('n','i'))
ch5=   "\tfdhgf"
print(ch5.strip())
print(max(ch5))
# [A..Z]==65..90 pour [a..z] +32
list=['a','b','c','d']
