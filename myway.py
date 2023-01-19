import random


#ランダムな3桁の数値を求める関数
def make_random_num():
    ary = []
    while len(ary) < 3:
        random_num = random.randint(0, 9)
        append_flg = True
 
        for ary_element in ary:
            if ary_element == random_num:
                append_flg = False
                break
        if append_flg == True:
            ary.append(random_num)
        append_flg = True
    return ary
 
#数値の入力とその値が3桁の異なる数値かどうかのチェックを行う関数
def input_and_check():
    input_num = input("3桁の数値を入力してください：")
    while True:
        input_num_ary = []
        if input_num.isdigit() == True and len(input_num) == 3:
            devision_num = int(input_num)
            for i in range(3):
                input_num_ary.append(devision_num // (10 ** (2-i)))
                devision_num = devision_num % (10 ** (2-i))
            if len(list(set(input_num_ary))) == 3:
                break
        input_num = input("【エラー】重複のない3桁の数値を入力してください：")
    return (input_num, input_num_ary)


# print(make_random_num())