
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv

with open('data.csv', 'r',encoding = 'utf-8-sig') as f:
    reader = csv.reader(f)
    for source in reader:
        """
        print(source)
        """
### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}は存在します。".format(word))

    else:
        print("{}は存在しません。".format(word))
        source.append(word)
    
        with open('data.csv', 'w',encoding = 'utf-8-sig',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(source)
    
    print("{}が見つかりました".format(word))
    print(source)

if __name__ == "__main__":
    search()