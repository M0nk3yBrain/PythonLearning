import art
from random import randint
from game_data import data


for item in data:
  print(item['name'])

def randPicker():
  dataLength = len(data)
  return randint(0, dataLength - 1)
  

print(art.logo)
def dictValues():
  A = data[randPicker()]
  name = A.get('name')
  followerCount = A.get('follower_count')
  description = A.get('description')
  country = A.get('country')
  return name, followerCount, description, country

 