#5-2

# year = int(input("うるう年を判定します（西暦を入力）>>"))

# def leap_year(year):
#     if( year % 400 == 0 ):
#         print("西暦"+ str(year) + "は、うるう年です")

#     elif(year % 100 == 0 ):
#         print("西暦"+str(year) + "は、うるう年ではありません")     
            
#     elif(year % 4 == 0):
#         print("西暦"+ str(year) + "は、うるう年です")

#     else:
#         print("西暦"+ str(year) + "は、うるう年ではありません")

# leap_year(year)

def is_leapyear(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

year = int(input("調べたい西暦を入力してください"))

if(is_leapyear(year)):
    input("{}はうるう年です".format(year))
else:
    input("{}はうるう年ではありません".format(year))