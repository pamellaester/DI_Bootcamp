

matrix_str = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''

matrix_list = list(matrix_str)
print(matrix_list)

column1 = matrix_list [0::4]
column2 = matrix_list [1::4]
column2 = matrix_list [2::4]

message = ""
def process_column(column: list[str]): 
    for char in column:
       if char.isalpha():
          message += char
    return message 

message1 = process_column (column1)
print(message)  

