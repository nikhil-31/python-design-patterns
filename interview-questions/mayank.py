list = [0, 1, 1, 1, 0, 0, 1, 0, 1]

left = 0
right = 1

while True:
    try:
        if list[left] != 0 and list[right] != 1:
            list[left], list[right] = list[right], list[left]
            left += 1
            right += 1
        elif list[left] != 0 and list[right] == 1:
            right += 1
        else:
            left += 1
    except:
        break


print(list)