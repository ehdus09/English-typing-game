import random as r
import time as t
import csv
import openpyxl


# 프로그램 소개
def intro():
    print("영컴타자연습에 오신걸 환영합니다.")
    t.sleep(1)
    print("영어단어를 타자연습을 하면서 외우실 수 있는 프로그램입니다.")
    print("="*30)
    t.sleep(1)
    print()

# 단어장 불러오기
def loadVoca(filename):
    wordDict = {}
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pass



            


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
def WordTest():
    cnt = 0 # 맞은 개수
    textCount = 0 # 입력한 글자 수
    print("\n몇 개의 단어로 진행하시겠습니까?")
    number = int(input("숫자로 입력하여 주십시오 : ")) # 시험 칠 단어 개수
    input("\n[영컴타자연습] 준비되면 엔터")
    start = t.time()


#main
'''
while True:
    intro()
    main = main()
    if main == 1: # 단어 시험
        mode = modeChoice()
        if mode == 1: # 영어보고 뜻쓰기
        
        elif mode == 1: # 뜻보고 영어쓰기

        else: # 잘못된 입력

    elif main == 2: # 단어추가

    else: # 잘못된 입력
'''
