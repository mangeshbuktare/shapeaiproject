import requests

r = requests.get('http://textfiles.com/stories/13chil.txt')

with open('slay_fox.txt', 'w') as f:
      f.write(r.text)