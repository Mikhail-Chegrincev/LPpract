s = input()
if s[0] != 'е' and s[0] != 'Е':
    print(s.count(' е')+s.count(' Е'))
else:
    print(s.count(' е')+s.count(' Е')+1)