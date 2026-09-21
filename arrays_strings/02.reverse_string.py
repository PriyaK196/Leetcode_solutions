def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    '''
    return self.helper(s,0,len(s)-1)
    def helper(self,s,start,end):
        if start>end:
            return s
        s[start],s[end]=s[end],s[start]
        return self.helper(s,start+1,end-1)
    '''

    start = 0
    end = len(s)-1

    while start < end:
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1

    return s


# Test Case 1
text = list("hello")

print("Test Case 1:", "".join(reverseString(text)))



# Test Case 2 - single character
text2 = list("a")

print("Test Case 2:","".join(reverseString(text2)))
