######################  要求1  ######################

def caculate(min,max):
    # 請用你的程式補完這個函式的區塊
    sum=0
    while min<=max:
        sum=sum+min
        min+=1
    print(sum)
caculate(4,8) # 你的程式要能夠計算 1+2+3，最後印出 6calculate(4, 8)
caculate(1,3) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


######################  要求2  ######################
def avg(data):
    # 請用你的程式補完這個函式的區塊
    count=len(data["employees"])
    employees=data["employees"]
    total_salary=0
    for i in range(count):
        the_salary=employees[i]["salary"]
        total_salary+=the_salary
    avg_salary=total_salary/count
    print(avg_salary)


avg({
    "count":3,
    "employees":[
            {"name":"John","salary":30000},
            {"name":"Bob","salary":60000},
            {"name":"Jenny","salary":50000},
            ]
}) # 呼叫 avg 函式


######################  要求3  ######################

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    if len(nums)==[]:
        print(0)

    max=0
    for i in range(len(nums)):
        for o in range(len(nums)):
            if nums[i]*nums[o]>max and i!=o:
                max=nums[i]*nums[o]
    print(max)

maxProduct([5, 20, 2, 6])
# 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3])
# 得到 30 因為 10 和 3 相乘得到最大值


######################  要求4  ######################

def twoSum(nums, target):
    # your code here
    for i in range(len(nums)):
        for o in range(len(nums)):
            if nums[i]+nums[o]==target and i!=o:
                result=[i,o]
                return(result)
    print(result)
result=twoSum([2, 11, 7, 15], 9)
print(result) 
# show [0, 2] because nums[0]+nums[2] is 9


#################  要求5(Optional)  #################
def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    the_input=[]
    count=0
    for i in range(len(nums)):
        if nums[i]==0:
            count+=1
        elif nums[i]>0:
            the_input.append(count)
            count=0
    if count>0:
        the_input.append(count)
        result=max(the_input)
        print(result)
    elif count==0:
        print(0)
    
maxZeros([0, 1, 0, 0])
# 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
# 得到 4
maxZeros([1, 1, 1, 1, 1])
# 得到 0