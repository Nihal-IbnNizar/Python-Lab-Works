#a=5
#b=10.23
#c=2j
#print('The type of a is:', type(a))
#print('The type of b is:', type(b))
#print('The type of c is:', type(c))

#first_name='Muhammed'
#last_name='Nihal'
#print('My name is ',first_name ,last_name)


#mylist1 = [1.5,2,3,('a','b','c')]
#mylist2 = ["nihal", "anshad", "minu" ,[11,12,(13,14)]]
#mylist3 = list((2,4,6))    
#print(type(mylist1))
#print(type(mylist2))
#print(type(mylist3))

#thislist = ["apple", "banana", "cherry"]
#mylist = thislist.copy()
#print(mylist)
#thislist.append("strawberry")
#print(thislist)
#print(mylist)

#mytuple = ("apple", "banana", "cherry")
#print(type(mytuple))



dictionary ={
    'student1':{
        'name':'nihal',
        'age': 21,
        'marks': {
        'maths':32,
        'english':50,
        'cs':42
        }
    },
    'student2':{
        'name':'anshad',
        'age': 24,
        'marks': {
        'maths':32,
        'english':50,
        'cs':42
        }
    }
    
}
print(dictionary)
print(dictionary['student1'])
print(dictionary.get('student2').get('marks'))
print(dictionary['student1']['name'])

set1={1,2,3,4,5}
set2={'a','b','c','d',22,23,24,'a',22,'23'}
print(set1)
print(set2)


