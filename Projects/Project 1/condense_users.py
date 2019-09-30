import pickle
import os

user_dict = {}

with open('Megan Lovejoy.pickle', 'rb') as f:
    megan_dict = pickle.load(f)

user_dict[megan_dict['Megan Lovejoy']['user_id']] = {}
user_dict[megan_dict['Megan Lovejoy']['user_id']]['screen_name'] = 'megan_lovejoy'
user_dict[megan_dict['Megan Lovejoy']['user_id']]['id'] = megan_dict['Megan Lovejoy']['user_id']
user_dict[megan_dict['Megan Lovejoy']['user_id']]['friends'] = megan_dict['Megan Lovejoy']['friends']

for friend in megan_dict['Megan Lovejoy']['friends']:
    user_dict[friend.id] = {}
    user_dict[friend.id]['id'] = friend.id
    user_dict[friend.id]['screen_name'] = friend.screen_name

for file in os.listdir('old_list_of_users'):
    id = int(file.rstrip('.pickle'))
    with open(os.path.join('old_list_of_users', file), 'rb') as f:
        friend_list = pickle.load(f)
    user_dict[id]['friends'] = []
    for friend in friend_list:
        user_dict[id]['friends'].append(friend.id)
        if friend.id not in user_dict:
            user_dict[friend.id] = {}
            user_dict[friend.id]['id'] = friend.id
            user_dict[friend.id]['screen_name'] = friend.screen_name

with open('all_users.pickle', 'wb') as f:
    pickle.dump(user_dict, f)
