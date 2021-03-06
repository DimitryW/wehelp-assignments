
#要求一：函式與流程控制
#完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
#提醒：請勿更動題目中任何已經寫好的程式。

def calculate(min, max):
    n = 0
    for i in range(min, max+1):
        n + = i
    print(n)

calculate(1, 3)
calculate(4, 8)

#要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
# 提醒：請勿更動題目中任何已經寫好的程式。

def avg(data):
    s = 0
    n = data['count']
    for i in range(data['count']):
        s+=data['employees'][i]['salary']
    print(s/n)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
})

# 要求三：演算法
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
    l = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                l.append(nums[i]*nums[j])
    print(max(l))

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

# 要求四 ( 請閱讀英文 )：演算法
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                a = nums[i] + nums[j]
                if a == target:
                    return([i, j])

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 要求五 ( Optional )：演算法
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
# 長度。
# 提醒：請勿更動題目中任何已經寫好的程式。

def maxZeros(nums):
    str_num = [str(i) for i in nums]
    a = "".join(str_num)
    b = a.split('1')
    print(len(max(b)))

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
