#Design wants stair step *s
'''
*
***
******
**********
'''

stars = "*"
for i in range(0, 1, 1):
    for j in range(0, 5, 1):
        if j == 1:
            continue
        stars += ("*"*j)
        print(stars)
