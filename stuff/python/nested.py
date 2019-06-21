Ruicheng_info = {'name': 'Ruicheng',
                'favourite_food': 'rice',
                'email':'luoric1@gmail.com'}
oka_info = {'name': 'oka K',
            'favourite_food': 'ayam penyet',
            'email':'oka@oka.net'}
Tom_info = {'name': 'Tom',
            'favourite_food': 'fish',
            'email':'tom@tom.net'}

my_contact = [Ruicheng_info, oka_info, Tom_info]
print(my_contact[0]["email"])
print(my_contact[2]["favourite_food"])

find_user = 'oka K'
for contact in my_contact:
    if contact['name'] == find_user:
        contact['email'] = 'hihi'
        
for contact in my_contact :
    print ('============')
    for key, value in contact.items():
        print(key + ": " + value)
