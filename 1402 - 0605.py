import random as r
import time
# 프로그램 소개
print("영컴타자연습에 오신걸 환영합니다.")
time.sleep(1)
print("영어단어를 타자연습을 하면서 외우실 수 있는 프로그램입니다.")
print("="*30)
time.sleep(1)
print()

# 메인 선택
print("다음 중 무엇을 하시겠습니까?")
print("1. 단어 학습 / 2. 단어 추가")
main = int(input())

if main == 1: # 단어 학습
    print("\n출제 방식을 선택해주십시오.")
    print("1. 영어보고 뜻쓰기 / 2. 뜻보고 영어쓰기")
    method = int(input())

    if method == 1:
        print("\n단어 종류를 선택해주십시오.")
        print("1. 기본 제공 단어 (기말시험범위) / 2. 개인 단어장 단어")
        kind = int(input())

        if kind == 1:
            cnt= 0 # 맞은 개수
            textCount = 0 # 입력한 글자 수
            print("\n몇 개의 단어로 진행하시겠습니까?")
            number = int(input("숫자로 입력하여 주십시오 : "))
            input("\n[영컴타자연습] 준비되면 엔터")
            start = time.time()
            
            i = 1
            for i in range(number):
                question = r.choice(list)
                print(f'{i}. {question}')
                answer = input("답 입력 : ")
                textCount += len(answer)
                i += 1

                if answer == question:
                    cnt += 1
                    list.remove(question)
                    print("Correct")
                else:
                    list.remove(question)
                    print("Wrong")
            
            end = time.time()

            result = end - start
            speed = (textCount/result) * 60

            # 결과 출력
            print("결과")
            print(f'맞은개수: {cnt}/{number}')
            print(f'걸린시간: {result}')
            print(f'타자속도: {speed:.1f} 타/분')
                    

        elif kind == 2:
            print("몇 개의 단어로 진행하시겠습니까?")
            number = int(input("숫자로 입력하여 주십시오 : "))
            for i in range(number):
                pass

        else:
            print("보기에 없는 숫자입니다. 다시 선택해주십시오.")
    
    elif method == 2:
        print("")
    
    else:
        print("보기에 없는 숫자입니다. 다시 선택해주십시오.")

elif main == 2: # 단어 추가
    print("영단어-뜻 형식으로 단어를 입력해주십시오.")
    print("입력하신 단어는 개인 단어장에 저장됩니다.")
    while True:
        word = input()

else:
    print("보기에 없는 숫자입니다. 다시 선택해주십시오.")