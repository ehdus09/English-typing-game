import random as r
import time as t
import csv


# 프로그램 소개
def intro():
    print("영컴타자연습에 오신걸 환영합니다.")
    t.sleep(1)
    print("영어단어를 타자연습을 하면서 외우실 수 있는 프로그램입니다.")
    print("="*30)
    t.sleep(1)
    print()

# 메인 선택
def mainChoice():
    print("다음 중 무엇을 하시겠습니까?")
    print("1. 단어 학습 / 2. 단어 추가")
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

#main
while True:
    intro()
    main = main()
