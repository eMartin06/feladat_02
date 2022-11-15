reggeli = {'vaj','tea','piritós'}

ebed =set()
ebed = set(['halászlé','kenyér',True,True])
print(type[ebed])
print(ebed)

reggeli.add('víz')
# reggeli.remove('körte')
reggeli.discard('körte')
print(reggeli)

reggeli = {'víz', 'vaj','tea','piritós'}
ebed = set(['halászlé','kenyér','víz'])

print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

gyumolcskosar = ['eper', 'alam', 'szilva','eper']
fajta=set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)