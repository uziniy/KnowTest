import random
import os

# 문제와 답을 딕셔너리 형태로 저장
questions_and_answers = {
    "새로운 Git 저장소를 초기화하는 명령어는 무엇인가요?": "git init",
    "기존 저장소를 클론하는 명령어는 무엇인가요?": "git clone <url>",
    "파일을 스테이징 영역에 추가하는 명령어는 무엇인가요?": "git add <file>",
    "모든 변경 사항을 스테이징 영역에 추가하는 명령어는 무엇인가요?": "git add .",
    "변경 사항을 커밋하는 명령어는 무엇인가요?": "git commit",
    "현재 상태를 확인하는 명령어는 무엇인가요?": "git status",

    "스테이징된 파일을 언스테이징하는 명령어는 무엇인가요?": "git restore --staged <file>",
    "추적하지 않을 파일을 정의하는 파일 이름은 무엇인가요?": ".gitignore",
    "파일을 삭제하고 변경 사항을 기록하는 명령어는 무엇인가요?": "git rm <file>",
    "파일을 추적에서 제외하는 명령어는 무엇인가요?": "git rm --cached <file>",
    "새 브랜치를 생성하는 명령어는 무엇인가요?": "git branch <branch_name>",
    "브랜치를 전환하는 명령어는 무엇인가요?": "git checkout <branch_name>",

   "브랜치를 생성 후 바로 전환하는 명령어는 무엇인가요?": "git checkout -b <branch_name>",
   "브랜치를 병합하는 명령어는 무엇인가요?": "git merge <branch_name>",
    "원격 저장소로부터 업데이트를 가져오는 명령어는 무엇인가요?": "git fetch",
   "로컬 변경 사항을 원격 저장소로 푸시하는 명령어는 무엇인가요?": "git push",
   "원격 저장소의 변경 사항을 로컬로 병합하는 명령어는 무엇인가요?": "git pull",
    "원격 저장소를 추가하는 명령어는 무엇인가요?": "git remote add <name> <url>",
    "등록된 원격 저장소를 확인하는 명령어는 무엇인가요?": "git remote -v",
    
    "특정 커밋에 태그를 추가하는 명령어는 무엇인가요?": "git tag <tag_name>",
    "주석 태그를 생성하는 명령어는 무엇인가요?": "git tag -a <tag_name> -m <message>",
    "커밋 로그를 확인하는 명령어는 무엇인가요?": "git log",
    "변경 사항을 비교하는 명령어는 무엇인가요?": "git diff",
    "스테이징 영역과 마지막 커밋을 비교하는 명령어는 무엇인가요?": "git diff --cached",
    "변경 사항을 임시로 저장하는 명령어는 무엇인가요?": "git stash",

    "임시 저장된 변경 사항을 복구하는 명령어는 무엇인가요?": "git stash pop",
    "CSS 약자 ": "Cascading Staye Sheets",
    "HEAD를 이동하되 기록은 유지하는 명령어는 무엇인가요?": "git reset --soft HEAD~",
    "HEAD와 인덱스를 이동하는 명령어는 무엇인가요?": "git reset HEAD~",
    "HEAD, 인덱스 및 작업 디렉토리를 초기화하는 명령어는 무엇인가요?": "git reset --hard HEAD~",
    "브랜치의 변경 사항을 다른 브랜치로 재적용하는 명령어는 무엇인가요?": "git rebase",
    "특정 브랜치로 재배치하는 명령어는 무엇인가요?": "git rebase --onto <newparent> <oldparent> <branch>"
}

# 터미널 화면을 깨끗하게 지우는 함수
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# 문제 풀기 함수
def solve_quiz():
    score = 0
    attempts = 0
    questions = list(questions_and_answers.keys())
    random.shuffle(questions)  # 문제 랜덤 정렬
    incorrect_answers = []  # 틀린 문제 저장

    for question in questions:
        clear_screen()
        print("=" * 50)
        print("🧑‍💻  Git 문제 풀기 퀴즈!  🧑‍💻")
        print("=" * 50)
        print(f"💡 현재 점수: {score} | 시도 횟수: {attempts}")
        print(f"남은 문제: {len(questions) - attempts}")
        print()

        print(f"문제: {question}")
        print("-" * 50)
        answer = input("👉 답을 입력하세요 ('그만' 입력 시 종료): ")

        if answer.strip().lower() == "그만":
            break

        attempts += 1
        if answer.strip().lower() == questions_and_answers[question].strip().lower():
            print("\n✅ 정답입니다!\n")
            score += 1
        else:
            print(f"\n❌ 오답입니다! 정답은: {questions_and_answers[question]}\n")
            incorrect_answers.append((question, questions_and_answers[question]))

        input("계속하려면 엔터를 누르세요...")

    # 퀴즈 결과 출력
    clear_screen()
    print("=" * 50)
    print("🎉 퀴즈 종료! 🎉")
    print(f"총 시도 횟수: {attempts} | 맞힌 문제: {score} | 틀린 문제: {len(incorrect_answers)}")
    print("=" * 50)

    # 틀린 문제 출력
    if incorrect_answers:
        print("\n❌ 틀린 문제와 정답")
        for idx, (q, a) in enumerate(incorrect_answers, start=1):
            print(f"{idx}. 문제: {q}")
            print(f"   정답: {a}\n")
    else:
        print("\n모든 문제를 맞췄습니다! 👍")

# 퀴즈 실행
solve_quiz()
