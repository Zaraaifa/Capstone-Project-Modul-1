print('----------Sumber--------------')
list_contoh = ['zaraa', 30, 11, 'Indonesia']
print(list_contoh)

print('--------APPEND---------')

##APPEND hanya di akhir list
##hanya bisa ditambahkan 1 nilai, jadi kalau banyak nilai hanya dianggap 1 dan masukkan dalam []
list_contoh = ['zaraa', 30, 11, 'Indonesia']
list_contoh.append('Kediri')
print(list_contoh)

print('---------INSERT--------')

##INSERT bisa ditambahkan di mana saja tergantung index
list_contoh.insert(0, 'zaraa')
print(list_contoh)

print('---------REMOVE--------')

##REMOVE menghapus sesuai value
list_contoh = ['zaraa', 'zaraa', 30, 11, 'Indonesia']
list_contoh.remove('zaraa')
print(list_contoh)

print('--------INSERT---------')

##INSERT bisa ditambahkan di mana saja tergantung index
list_contoh.insert(0, 'zaraa')
print(list_contoh)

print('-------CONCAT----------')

##CONCAT menggabugkan 2 list
list_contoh = ['zaraa', 30, 5, 'Indonesia']
list_contoh2 = ['abdillah', 2, 8, 'Yogyakarta']
list_contoh3 = list_contoh + list_contoh2
print(list_contoh3)

print('--------POP---------')

##POP menghapus sesuai index
list_contoh3 = ['zaraa', 30, 5, 'Indonesia', 'abdillah', 2, 8, 'Yogyakarta']
list_contoh3.pop(3)
print(list_contoh3)

print('---------EXTEND--------')

##EXTEND menggabungkan 2 list
list_contoh3 = ['zaraa', 30, 5, 'Indonesia']
list_contoh4 = ['abdillah', 2, 8, 'Yogyakarta']
list_contoh4.extend(list_contoh3) 
print(list_contoh4)

print('-----------------')

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
list3 = list1
print(list3)

print(r'append bisa ditambahkan di akhir list tapi hanya 1 nilai')
print(r'kalau extend bisa ditambahkan di mana saja dan hanya bisa antar data collection (gabisa variabel)')

print("-----------------")

print('---------INSERT--------')

##INSERT bisa ditambahkan di mana saja tergantung index
list_contoh.insert(0, 'zaraa')
print(list_contoh)

print('---------REMOVE--------')

##REMOVE menghapus sesuai value
list_contoh = ['zaraa', 'zaraa', 30, 11, 'Indonesia']
list_contoh.remove('zaraa')
print(list_contoh)

##SORT mengurutkan berdasarkan alfabet
list_contoh = ['zaraa', 'zaraa','Indonesia', 'Jogja']
list_contoh.sort()
print(list_contoh)

