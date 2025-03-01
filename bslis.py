

class Solution:
    def bs(self,res,num):
        l,h=0,len(res)-1
        while l<=h:
            mid=(l+h)//2
            if res[mid]<num:
                l=mid+1
            else:
                h=mid-1
        return l
    def lis(self, arr):
        res=[]
        for num in arr:
            i=self.bs(res,num)
            if i==len(res):
                res.append(num)
            else:
                res[i]=num
        return len(res)
            