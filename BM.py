input_data = open('input.txt', 'r') 

data = input_data.read() 
#--------------------------------------------------------------------
data = data.split()
A = int(data[0])
B = int(data[1])
aut = str
aut = 0
if A > B: 
    aut = ">"
else:
    if A < B :
        aut = "<"
    else:
        aut = "="        


#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(aut))


# Закрываем открытые ранее файлы!
input_data.close() 
output_data.close()