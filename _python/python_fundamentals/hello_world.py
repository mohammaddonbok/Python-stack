
#######################################################################################################
def func(list):
    if (len(list) < 2):
        return 'false'
    else:
        first = list[0]
        last = list[-1]
        return  first , last

first,last = func("1,2,3,4,5")
print("this is first element {} This is the last element {}".format(first , last)) #format print 
print(f"first element {first} \n last element {last}")
#######################################################################################################
def sumFunc(list):
    sum=0
    for i in list:
        sum = sum + i
    return sum
print("This is thne sum ",sumFunc([1,2,3,4,5]))
############################################################################################################
def swapFunc(list):
    list.reverse()
    print(list)
swapFunc([1,2,3,4,5])
########################################################################################################
def dict(list):
    m=max(list)
    mi=min(list)
    s=sum(list)
    a=s/len(list)
    return m,mi,s,a
max,min,sum,avg =dict([1,2,3,4,5,6])    
print(f"max: {max} min: {min} sum: {sum} avg {avg}")
###############################################################################################################

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
def bubbleSort(A):
    for k in range(len(A) - 1):
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
if __name__ == '__main__':
    A = [4, 10, 8, 3, 1, 9, -2]
    bubbleSort(A)
    print(A)
