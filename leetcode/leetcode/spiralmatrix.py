class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sm = []
        top =0
        left =0
        right = len(matrix[0])-1
        print(right)
        bottom = len(matrix)-1
        print(bottom)
        dir =0

        while(top <= bottom and left <= right):
            if dir == 0:
                for i in range(left, right+1):
                    sm.append(matrix[left][i])
                top+=1
            if dir == 1:
                for i in range(top,bottom+1):
                    sm.append(matrix[i][right])
                right -=1
            if dir == 2:
                for i in range(right,left-1,-1):
                    sm.append(matrix[bottom][i])
                bottom -= 1
            if dir == 3:
                for i in range(bottom,top-1,-1):
                    sm.append(matrix[i][left])
                left += 1
            dir =(dir+1)%4
        return sm
                