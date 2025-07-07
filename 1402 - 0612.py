import random as r
import time as t
import csv
import openpyxl
import sys


# 프로그램 소개
def intro():
    print("영컴타자연습에 오신걸 환영합니다.")
    t.sleep(1)
    print("영어단어를 타자연습을 하면서 외우실 수 있는 프로그램입니다.")
    print("="*30)
    t.sleep(1)
    print()

# 영어가 키인 기본 단어장 불러오기
def loadEngVoca(filename):
    engWordDict = {}
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2: # 줄에 영어, 뜻 2개의 항목이 있을때만 저장
                eng, kor = row
                engWordDict[eng.strip()] = kor.strip()
    return engWordDict

# 뜻이 키인 기본 단어장 불러오기
def loadKorVoca(engDict):
    # 딕셔너리 컴프리헨션
    korWordDict = {k: e for e, k in engDict.items()}
    return korWordDict

# 메인 선택
def mainChoice():
    print("다음 중 무엇을 하시겠습니까?")
    print("1. 단어 시험 / 2. 단어 추가")
    return int(input())

# 출제 방식 선택
def modeChoice():
    print("\n출제 방식을 선택해주십시오.")
    print("1. 영어보고 뜻쓰기 / 2. 뜻보고 영어쓰기")
    return int(input())

# 단어 종류 선택
def kindChoice():
    print("\n단어 종류를 선택해주십시오.")
    print("1. 기본 제공 단어 (기말시험범위) / 2. 개인 단어장 단어")
    return int(input())

# 단어 시험
def wordTest(dic):
    right = 0 # 맞은 개수
    textCount = 0 # 입력한 글자 수
    print("\n몇 개의 단어로 진행하시겠습니까?")
    number = int(input("숫자로 입력하여 주십시오 : ")) # 시험 칠 단어 개수
    input("\n[영컴타자연습] 준비되면 엔터")
    start = t.time() # 시작 시간
    for i in range(number):
        keys = list(dic.keys())
        question = r.choice(keys) # 문제
        print(question)
        answer = input("답: ") # 답
        textCount += len(answer)
        if answer == dic[question]:
            right += 1
            print("⭕️")
            del dic[question]
        else:
            print("❌")
    end = t.time() # 종료 시간
    print("시험이 종료되었습니다.")
    totalTime = end-start # 걸린시간
    print(f'걸린 시간: {totalTime}')
    print(f'맞은 개수: {right}')
    print(f'자수: {textCount/totalTime*60:.1f}자')

# 단어 추가
def inputWord(eng, kor, filename="personalWord.xlsx"):
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    # 단어 추가
    ws.append([eng.strip(), kor.strip()])
    wb.save(filename)
    

# 결과 후 선택
def choiceExit():
    print("프로그램을 종료할까요?")
    print("1. 프로그램 종료 / 2. 처음으로 돌아가기")
    return int(input())

# 프로그램 종료
def exitProgram():
    sys.exit(0)

# 잘못된 숫자 선택
def wrongAnswer():
    print("보기에 없는 숫자입니다. 다시 선택해주십시오.")



#main
while True:
    intro()
    main = mainChoice()
    if main == 1: # 단어 시험
        mode = modeChoice() # 영어로 칠지 한글로 칠지 선택
        kind = kindChoice() # 기본제공 단어로 칠지, 개인 단어장으로 칠지 선택

        if kind == 1: # 기본제공 단어
            enWord = loadEngVoca("word.csv")
            koWord = loadKorVoca(loadKorVoca(enWord))

            if mode == 1: # 영어보고 뜻쓰기
                wordTest(enWord)
                exit = choiceExit # 종료할지 처음으로 돌아갈지 선택

                if exit == 1:
                    exitProgram()
                elif exit == 2:
                    mainChoice()
                else:
                    wrongAnswer()

            elif mode == 2: # 한글보고 뜻쓰기
                wordTest(koWord)
        
    elif main == 2: # 단어추가
        pass
    else: # 잘못된 입력
        wrongAnswer()