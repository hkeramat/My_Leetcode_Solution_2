

num_rows =6 



def pascalTriangle(num_rows):
    if num_rows ==1:
            row =[1]
            triangle =[[1]]
            return triangle
    
    triangle =[[1]]
    for row_n in range (1, num_rows):
        row =[1]
        for column in range(1, row_n):
            row.append(triangle[row_n-1][column-1] + triangle[row_n-1][column]) 
        row.append(1)
        triangle.append(row)
    
    return triangle


answer = pascalTriangle(num_rows)
print(answer)
