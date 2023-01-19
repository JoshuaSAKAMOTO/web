import myway
import cgi
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from ht01 import answer_num_ary 

html_head="""
<!DOCTYPE html>
<html la="ja">
<meta charset="UTF-8">
<head>
<title></title>
</head>
<body>
""" 

html_tail="""
</body>
</html>
"""
form = cgi.FieldStorage()
username = form["username"].value
cnt = int(form["count"].value) + 1
num = int(form["number"].value)
ans = int(form["answer"].value)
answer_count = 0

print("hit&blowゲームを開始します。")




form_post=f"""
<form action="ht02.py" method="post">
  答えは？<input type="text" name="answer">(3桁の自然数を入力してください)
  <input type="hidden" name="count" value={cnt}>
  <input type="hidden" name="number" value={num}>
  <input type="submit" value="回答">
</form>
"""


 

hit_count = 0
blow_count = 0
#入力した3桁の値を取得する
(my_answer_num, my_answer_num_ary) = myway.input_and_check()
answer_count += 1
for i in range(3):
    for j in range(3):
        if i == j and answer_num_ary[i] == my_answer_num_ary[j]:
            hit_count += 1
        elif i != j and answer_num_ary[i] == my_answer_num_ary[j]:
            blow_count += 1

print("【" + str(answer_count) + "回目の解答】")
print(str(my_answer_num) + "は【" + str(hit_count) + "H、" + str(blow_count) + "B】です。")
if hit_count == 3:
    print("正解です！正解するまで" + str(answer_count) + "回かかりました！")
    

print(html_head)
print(html_tail)
