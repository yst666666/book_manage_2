#
#
# for i in range(2, 1000):
#     l = []
#     for k in range(1, i+1):
#         if i % k == 0:
#             l.append(k)
#     if sum(l) == i:
#         print(i,l,end=',')
#         print( )


# s = 'abecd'
# print(s.find('f'))
# print(s.index('f'))

# 117
# names1 = ['a','b','c','d']
# names2 = names1  # 1变了2也会变,2变了1也会变
# names3 = names1[:]
# names2[0] ='Alice'
# names3[1]='Bob'
# sum = 0

# print(names1,names2,names3)
# for ls in (names1,names2,names3):
#     if ls[0] == 'Alice':
#         sum +=1
#     if ls[1] == 'Bob':
#         sum  += 10
#
# print(sum)


# snum_list = []
# i_list = []
# j_list = [1, ]
# snum = 0
#
# def wanshu(num):
#     global i_list, j_list
#     # print(j_list, num)
#
#     for j in range(2, num):
#         if num % j != 0:
#             continue
#         j_list.append(j)
#
# for i in range(2, 1000):
#     wanshu(i)
#     if i == sum(j_list):
#         snum_list.append(i)
#
#     j_list = [1, ]
# print(snum_list)


# snum_list = []
# i_list = []
# j_list = [1, ]
# snum = 0
#
#
# def min_yinshu(num):
#     global i_list, j_list
#     # print(j_list, num)
#
#     for j in range(2, num):  # 循环2 到 num+1
#         if num % j != 0:  # 如果i不可以整除j, 及j不是i的因子
#             continue  # back
#         # print(num, j)
#         j_list.append(j)
#         # print(num, j, int(num / j))
#         if num == 1:
#             return
#         num = int(num / j)
#         min_yinshu(num)
#         return
#     j_list.append(num)
#
# min_yinshu(12321321312321)
# print('所有因数为',j_list)
# print('因数为',list(set(j_list)))


# 向上取整
import math

# print(math.ceil(2.3))   #3
# print(math.ceil(2.6) )  #3


# 向下取整

"\nmath.floor---"
print(math.floor(2.3))  # 2

"math.floor(2.6) => ", math.floor(2.6)

# 四舍五入

"\nround---"
# print(round(2.3))  # 2
# print(round(2.6))  # 3


# "round(2.6) => ", round(2.6)

# 这三个的返回结果都是浮点型
"\n\nNOTE:every result is type of float"
# print(math.ceil(2))
# "math.ceil(2) => ", math.ceil(2)
# print(math.floor(2))
# "math.floor(2) => ", math.floor(2)

# print(math.floor(5.5))

# print(type(1/2))

# print(type(1+2L*3.14))
# print(list((1,2,3,4)))
# print(tuple([1,2,3,4]))


# x = 'foo'
# y  = 2
# print(x+y)


# a = ['a,1', 'b,2,7', 'c,3']
# b = ['a,4', 'b,5', 'c,6', 'd,4']
# print(a+b)
# ['a,1', 'b,2,7', 'c,3', 'a,4', 'b,5', 'c,6', 'd,4']


# alist = [2,4,5,6,7]
# for i in alist:
#     if i% 2 == 0:
#         alist.remove(i)
# print(alist)

# d={"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25}
# # print(d.items())  #dict_items([('a', 26), ('g', 20), ('e', 20), ('c', 24), ('d', 23), ('f', 21), ('b', 25)])
#
# print(sorted(d.items(),key=lambda x:x[1]))

# import copy
# a = [1,2,3,[4,5],6]
# b=a
# c =copy.copy(a)
# d = copy.deepcopy(a)
#
# b.append(10)
# c[3].append(11)
# d[3].append(12)
# print(a)
# print(b)
# print(c)
# print(d)

"""
[1, 2, 3, [4, 5, 11], 6, 10]
[1, 2, 3, [4, 5, 11], 6, 10]
[1, 2, 3, [4, 5, 11], 6]
[1, 2, 3, [4, 5, 12], 6]
"""

# a = 'abab'
# print([ i for i in range(2,101,2)])

print(list(filter(lambda x: x % 2 == 0, range(1, 101))))
print('大沙发地方=大师傅啊' == 3223)
