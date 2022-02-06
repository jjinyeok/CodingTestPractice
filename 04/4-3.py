#18분
place = input()

x_r = ['a','b','c','d','e','f','g','h']
x = [1,2,3,4,5,6,7,8]
x_place = 1
for i in range(len(x)):
    if place[0] == x_r[i]:
        x_place = int(x[i])

y_place = int(place[1])
print(x_place, y_place)

count = 0
if x_place - 2 >= 1:
    if y_place - 1 >= 1:
        count += 1
    if y_place + 1 <= 8:
        count += 1
if x_place + 2 <= 8:
    if y_place - 1 >= 1:
        count += 1
    if y_place + 1 <= 8:
        count += 1
if y_place - 2 >= 1:
    if x_place - 1 >= 1:
        count += 1
    if x_place + 1 <= 8:
        count += 1
if y_place + 2 <= 8:
    if x_place - 1 >= 1:
        count += 1
    if x_place + 1 <= 8:
        count += 1

#x_palce = int(ord(place_data[0]) - int(ord('a')) + 1)
#steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
#for step in steps:
#    next_x = x_place + step[0]
#    next_y = y_place + step[1]
#    if next_x >= 1 and next_y >= 1 and next_x <= 8 and next_y <= 8:
#        count += 1

print(count)