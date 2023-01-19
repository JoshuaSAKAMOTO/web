import myway
import cgi
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_head="""
<!DOCTYPE html>
<html la="ja">
<meta charset="UTF-8">
<head>
<title></title>
</head>
<body>
""" 
print("hit&blowゲームを開始します。")
html_tail="""
</body>
</html>
"""
form = cgi.FieldStorage()
username = form["username"].value
cnt = int(form["count"].value) + 1
num = int(form["number"].value)
ans = list(form["answer"].value)

answer_count = 0



form_post=f"""
<form action="ht02.py" method="post">
  答えは？<input type="text" name="answer">(3桁の自然数を入力してください)
  <input type="hidden" name="count" value={cnt}>
  <input type="hidden" name="number" value={num}>
  <input type="submit" value="回答">
</form>
"""

#ランダムな3桁の値を生成する
answer_num_ary = myway.make_random_num()

print(html_head)
print(form_post)
print(html_tail)
