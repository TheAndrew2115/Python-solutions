import collections

'''
You are given two arrays, mapping (int) and nums (string).

The mapping array shows you a new digit system to convert the numbers in the
nums array based on their position in mapping. 

You are to output a new array that is sorted based on the new value of mapping.
For ex:
mapping = [3,2,5] -> 3 now means 0, 2 means 1, and 5 means 2
nums = ['332','53','25']

'332' -> '001' or just '1'
'53' -> '20'
'25' -> '12'

output = ['332','25','53']
If two nums have the same 'true value', you should preserve the order in which
they appear.
'''

def strangeSort(mapping, nums):
    # Write your code here
    digitMap = collections.defaultdict() # value to position
    for i in range(0,len(mapping)):
        digitMap[mapping[i]] = str(i)
    
    trueValueMap = collections.defaultdict() # string to value
    retArr = []
    
    for string in nums:
        tempString = ""
        for char in string:
            tempString = tempString + digitMap[int(char)]
        trueValueMap[string] = int(tempString)
    
    for key in trueValueMap:
        if len(retArr) == 0:
            retArr.append(key)
            continue
        for i in range(0,len(retArr)):
            if trueValueMap[key] < trueValueMap[retArr[i]]:
                retArr.insert(i,key)
                break
            elif i == len(retArr)-1:
                retArr.append(key)
                break
    
    return retArr

print(strangeSort([3,5,4,6,2,7,9,8,0,1],['3', '3','33','991','333990','3990','33990','990','32','332']))
        
