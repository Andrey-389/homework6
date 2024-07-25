my_dict={'Maxim':1992,'Anton':1980,'Demid':2003,'Andrey':2002}
print('dict:',my_dict)
print('Existing value:',my_dict.get('Maxim'))
print('Not existing value:',my_dict.get('Vasiliy'))
my_dict.update({'Vasiliy':2000,'Dmitriy':1983})
delete=my_dict.pop('Demid')
print('Modified dictionary:',my_dict)
my_set=set_={1,5,4,3,4,2,1,2,1,3,5,'Maxim','Anton',}
print('set',my_set)
set_.add(50)
set_.remove('Anton')
set_.remove(1)
print('Modified set:',my_set)