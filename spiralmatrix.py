# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Try programiz.pro")

def generate_matrix(n):
    matrix = [[0]*n for i in range(n)]
    
    top,bottom = 0, n-1
    left,right = 0,n-1
    
    num = 1
    
    while top<=bottom and left<=right:
    # top row filling
        for i in range(left,right+1):
            matrix[top][i]=num
            num+=1
        top+=1
        
        # right column
        for i in range(top,bottom+1):
            matrix[i][right]=num
            num+=1
        right=right-1
        
        
        #Bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num=num+1
            bottom=bottom-1
            
        # Left column
        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=num
                num=num+1
            left=left+1
            
            
    return matrix
    
    
n=6
result=generate_matrix(n)

for row in result:
    print('  '.join(map(str,row)))