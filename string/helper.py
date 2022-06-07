# print(ord('a'))

str ='geeksforgeeks'
# print(str[0])
# print(ord(str[0]))
# print(ord('a'))
d=ord(str[0])-ord('a')
# print(d)

visited=[0]*(26)
# print(visited)
print(visited[ord(str[0])-ord('a')])
if visited[ord(str[0])-ord('a')]==True:
    print('yes')
print('no')
