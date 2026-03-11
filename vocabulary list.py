wordslist = {}

while True:
    a = input("1 단어 추가 / 2 문제 풀기 / 3 불러오기 / 4 저장 => ")

    if a == '1': # 단어 추가
        ask = input('문제=>')
        answer = input('답=>')
        wordslist[ask] = answer

    elif a == '2': # 문제 풀기
        import random

        problemcount = int(input('풀 문제 수 => '))
        quiz = list(wordslist.items())
        random.shuffle(quiz)

        for ask, answer in quiz[:problemcount]:
            print(ask)
            user = input('답=>')

            if user == answer:
                print("정답")
            else:
                print("오답/정답:" + answer)

            print("="*40)

    elif a == '3': # 불러오기
        f = open("voca.txt","r")
        for line in f:
            ask, answer = line.strip().split(":")
            wordslist[ask] = answer
        f.close()
        print("단어장 불러오기 완료")

    elif a == '4': # 저장
        f = open("voca.txt","w")
        for ask, answer in wordslist.items():
            f.write(ask + ":" + answer + "\n")
        f.close()
        print("단어장 저장 완료")
21

            
