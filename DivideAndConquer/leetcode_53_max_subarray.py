class Solution:
    def mid(arr, l, m, r):
        ltemp = 0
        left_sum=-10000
        for i in range(m, l-1, -1):
            ltemp += arr[i]
            if ltemp > left_sum:
                left_sum = ltemp
        rtemp=0
        right_sum=-10000
        for i in range(m+1,r+1,):
            rtemp += arr[i]
            if rtemp > right_sum:
                right_sum = rtemp
        return right_sum + left_sum


    def divide(self, arr, l, r):
        if l == r:
            return arr[l]

        mid = (l+r)/2

        return max( self.divide(arr,l,mid), self.divide(arr,mid+1,r), self.mid(arr,l,mid,r))


    def maxSubArray(self, a: List[int]) -> int:
        return self.divide(a,0,len(a)-1)