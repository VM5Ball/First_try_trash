
keys=['Vladimir', 'Svetlana', 'Sergey', 'Alexey']
values=['Russian, Englishh, French', 'Russian', 'Russian, English', 'Russian, English, Deutch']
d={k:v for (k,v) in zip(keys,values)}
for keys,values in d.items():
    print(keys, ': ', values, sep='')
d['Nikita'] = 'Zero'
print('------------------------------')

d.setdefault('Nastya', 'Russian')
for k in d:
	print(k, ': ', d[k], sep='')
#d.pop(key)