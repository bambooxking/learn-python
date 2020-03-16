'''
@Description: 汉诺塔
@Author: wzx1
@Date: 2019-10-20 13:58:19
@LastEditTime: 2019-10-20 13:59:57
@LastEditors: wzx1
'''

def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        hanoi(height - 1, left, middle, right)
        print(left, '=>', right)
        hanoi(height - 1, middle, right, left)
        
hanoi(3)