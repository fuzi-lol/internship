class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_list = []
        for i in range(numRows):
            pascals_list.append([])
            for j in range(i+1):
                if j ==0 or i==j:
                    pascals_list[i].append(1)
                else:
                    pascals_list[i].append(pascals_list[i-1][j-1]+pascals_list[i-1][j])
        return pascals_list