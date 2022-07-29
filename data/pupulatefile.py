from turtle import heading
import xlsxwriter

workbook = xlsxwriter.Workbook("allaboutexcel.xlsx")
worksheet = workbook.add_worksheet("filesheet")

data = [{"gender":"male", "learning style": "watching videos"}, 
        {"gender":"female", "learning style": "reading books"},]

worksheet.write(0,0, "#")

headings = ["key","name", "surname", "brand", "likes"]

for index, value in enumerate(headings):
    # print(index)
    worksheet.write(0,index,value)


list = ["books", "videos"] 

index = 0
named = ""
for index in range(len(list)):
    # index +=1
    print(index,list[index])
    # for name in list[index]:
    #     named = name
    #     print(named)
        
        # worksheet.write(index, "name", str(index))
#     worksheet.write(index+1, int(index+1), value["gender"])
#     worksheet.write(index+1, int(index+2), value["learning style"])
    
workbook.close()