

list = ["水","金","地","火","木","土","天","海","冥"]

#①配列listの要素を1つずつ順番に出力する
for element in list:
  print(element)

#②　①を2回繰り返す
for _ in range(1):
  for element in list:
    print(element)

list = ["水","金","地","火","木","土","天","海","冥"]

# カウンターの初期化
counter = 0

# whileループで配列の要素を2回繰り返す
while counter < 2:
    for element in list:
        print(element)
    counter += 1