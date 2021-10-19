end = input().strip()
inp = input().strip()
mat = []
while inp != end:
    mat.append(inp[1:-1])
    inp = input().strip()
height = len(mat)
width = len(mat[0])
c = 0
for i in range(len(mat)):
    if mat[i][0] == '~':
        c = height - i
        break
water_volume = c * width
height, width = width, height
new_mat = []
if water_volume // width != water_volume / width:
    c = water_volume // width + 1
else:
    c = water_volume // width
for i in range(height):
    if i < c:
        new_mat.append('~' * width)
    else:
        new_mat.append('.' * width)
new_mat.reverse()
print('#' * (width + 2))
for i in range(height):
    print('#' + new_mat[i] + '#')
print('#' * (width + 2))
water_volume = c * width
gas_volume = height * width - water_volume
if water_volume > gas_volume:
    waterstr1 = 20 * '~'
    gasstr1 = round(gas_volume / water_volume * 20) * '.'
else:
    gasstr1 = 20 * '~'
    waterstr1 = round(water_volume / gas_volume * 20) * '.'
waterstr2 = str(water_volume) + '/' + str(width*height)
gasstr2 = str(gas_volume) + '/' + str(width*height)
l = len(max(waterstr2, gasstr2))
print(gasstr1.ljust(20) + ' ' + gasstr2.rjust(l))
print(waterstr1.ljust(20) + ' ' + waterstr2.rjust(l))
