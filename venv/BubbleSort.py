
mDataForSort = [10, 75, 43, 15, 26, 0, 87, 99, 38, 62]
print("Data for sort:", mDataForSort)

def bubbleSort(mList):
    mLastItem = len(mList) - 1
    for i in range(0, mLastItem):
        for j in range(0, mLastItem - i):
            if mList[j] > mList[j + 1]:
                mList[j], mList[j + 1] = mList[j + 1], mList[j]
            # print(mList)
    mTime.endlog()
    return mList

mNewList = bubbleSort(mDataForSort).copy()
print("Bubble sort result:", mNewList)
