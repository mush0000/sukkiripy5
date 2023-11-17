#5-5

# #計算データの入力
# def int_input(msg_amount,msg_people):
#     amount = int(input(msg_amount))
#     people = int(input(msg_people))
#     return[amount,people]

# #割り勘の計算
# def calc_payment(amount,people=2):
#     dnum = amount / people      #総額を人数で割る
#     pay = dnum // 100 * 100     #100円未満を切り捨てる

#     if dnum > pay:              #元の値と比較して、
#         pay = int(pay + 100)    #小さければ100円未満があったので上乗せ
    
#     payorg = amount - pay * (people - 1)
#     return[int(pay), int(payorg)]

# #幹事の支払額の計算
# def show_payment(pay,payorg,people=2):
#     #結果の表示
#     print("*** 支払額 ***")
#     print("1人あたり{}円({}人)、幹事は{}円です".format(pay,people -1, payorg))

# amount,people = int_input("支払総額を入力してください>>","参加人数を入力してください>>")
# [pay,paylog] = calc_payment(amount,people)
# show_payment(pay,paylog,people)


#計算データの入力
def int_input(msg):
    return int(input("{}を入力してください>>".format(msg))) 

#割り勘の計算
def calc_payment(amount,people=2):
    dnum = amount / people      #総額を人数で割る
    pay = dnum // 100 * 100     #100円未満を切り捨てる

    if dnum > pay:              #元の値と比較して、
        pay = int(pay + 100)    #小さければ100円未満があったので上乗せ

    #幹事の支払額の計算
    payorg = amount - pay * (people -1)
    return (int(pay),int(payorg))

 #結果の表示
def show_payment(pay,payorg,people=2):
    print("*** 支払額 ***")
    print("1人あたり{}円({}人)、幹事は{}円です".format(pay,people -1,payorg))

#関数の呼び出し
amount = int_input("支払総額")
people = int_input("参加人数")

pay,payorg = calc_payment(amount,people)
show_payment(pay,payorg,people)


