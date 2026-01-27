Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
namelist=['Hunter', 'Gabe', 'Sam']
morename=['Aubrie', 'Talson', 'Eli']
namelist.append(morename)
print(namelist)
['Hunter', 'Gabe', 'Sam', ['Aubrie', 'Talson', 'Eli']]
numberlist = ['12','0','3']
numberlist.insert(1,'/')
print(numberlist)
['12', '/', '0', '3']

numberlist=['12','8','03']
numberlist.remove('8')
print(numberlist)
['12', '03']

numlist=['1','2']
numlist2=['0','3']
result=numlist+numlist2
print(result)
['1', '2', '0', '3']

nums=[1,2]
result=nums*3
print(result)
[1, 2, 1, 2, 1, 2]


namelist=['Harry','Ron','Hermione']
more=['severus']
namelist.extend(more)
print(namelist)
['Harry', 'Ron', 'Hermione', 'severus']


namelist=['Harry','Ron','Hermione']
girl=namelist.pop()
print(girl)
Hermione
print(namelist)
['Harry', 'Ron']


number=[1,2,3,4,5,6,7,8]
print(number[1:6])
[2, 3, 4, 5, 6]

namelist=['Harry','Ron','Hermione']
del namelist[0]
print(namelist)
['Ron', 'Hermione']


namelist=['Harry','Ron','Hermione']
print('Harry' in namelist)
True
print('Hunter' in namelist)
False

namelist=['Harry','Ron','Hermione']
print(namelist.index('Ron'))
1
print(namelist.index('Harry'))
0


numbers=[3,5,6,1,8,9,10,2,4,7]
numbers.sort()
print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
print(numbers)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


namelist=['Harry','Ron','Hermione']
select=random.choice(namelist)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    select=random.choice(namelist)
NameError: name 'random' is not defined. Did you forget to import 'random'?
namelist=['Harry','Ron','Hermione']
randomchoice = random.chocie(namelist)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    randomchoice = random.chocie(namelist)
NameError: name 'random' is not defined. Did you forget to import 'random'?
>>> import random
>>> namelist=['Harry','Ron','Hermione']randomchoice = random.chocie(namelist)
SyntaxError: invalid syntax
>>> import random
>>> namelist=['Harry','Ron','Hermione']
>>> randomchoice = random.chocie(namelist)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    randomchoice = random.chocie(namelist)
AttributeError: module 'random' has no attribute 'chocie'. Did you mean: 'choice'?
>>> import random
>>> namelist=['Harry','Ron','Hermione']
>>> randomchoice = random.choice(namelist)
>>> print(randomchoice)
Harry
>>> 
>>> 
>>> 
>>> numlist=[[1,2,3],[4,5,6],[7,8,9]]
>>> print(numlist[0][1])
2
print(numlist[0][0])
1
print(numlist[0][1])
2
print(numlist[0][2])
3
