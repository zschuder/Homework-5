import numpy as np

"""
>>>arr = np.array([[1,1,1],[2,2,3],[2,2,2]])
>>>findEqual(arr)
array([[1,1,1],[2,2,2]])
"""

arr = np.array([[1,1,1],[2,2,3],[2,2,2]])
def findEqual(arr):
    row_mean = np.mean(arr, axis=1)
    del_indexes = []
    for row_num in range(len(arr)):
        for element in arr[row_num]:
            if element != row_mean[row_num]:
                del_indexes.append(row_num)
    delete_row = np.unique(del_indexes)
    for i in delete_row:
        arr = np.delete(arr, i, 0)
    return arr
    
    #row_mean = np.mean(arr, axis=1)
    #for row in range(arr.shape[0]):
    #    #arr[row,:][arr[row,:] != row_mean[row]] = np.delete(arr,row_mean[row],axis=1)
    #    arr = np.all(arr[row,:][row_mean], axis=1)
    #return arr
    
print(findEqual(arr))