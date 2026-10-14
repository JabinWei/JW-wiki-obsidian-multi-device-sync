import random 

def generate_number(start, end):
    return random.randint(start, end)

def get_user_guess():
    while True:
        try:
            return int(input("请输入您猜测的数字(0-100之间，-1退出)："))
        except ValueError:
            print("输入不合法，请输入0～100的数字（包含0，100）。")

def play_one_round():
    randomNumber = generate_number(0, 100)
    # print(randomNumber)
    thisGuessCnt = 0
    while True:
        guessNum = get_user_guess()
        thisGuessCnt += 1
        if guessNum == -1:
            return 0
        if guessNum < randomNumber:
            print("猜测的数字太小了！！！")
        elif guessNum > randomNumber:
            print("猜测的数字太大了！！！")
        else:
            print("恭喜您猜对了！！！")
            break
    return thisGuessCnt

if __name__ == "__main__":
    print("欢迎来到Jabin的猜数游戏")
    totalGuessCnt = 0
    guessCntList = []
    while True:
        thisRoundGuessCnt = play_one_round()
        guessCntList.append(thisRoundGuessCnt)
        totalGuessCnt += thisRoundGuessCnt
        continueGameFlg = input("是否需要再来一局(Y/N)：")
        if continueGameFlg.strip().lower().startswith('n'):
            print(f"一共猜测了{totalGuessCnt}次")
            counter = 0
            for roundGuessCnt in guessCntList:
                counter += 1
                print(f"第{counter}轮游戏一共猜测了{roundGuessCnt}次")
            break