import datetime

records = []

print("@@지출 관리 프로그램@@")
print("x를 입력하여 종료하세요")

while True:
    # 입력받는 부분
    date = input("날짜를 입력하세요(YYMMDD): ")
    item = input("항목을 입력하세요: ")
    price = input("금액을 입력하세요: ")
    category = input("분류를 입력하세요: ")
    if date.strip() == 'x':
        break
    record = {"date": date,
              "item": item,
              "price": int(price),
              "category": category
}
    records.append(record)


def get_week(date_str):
    date = datetime.strptime(date_str, "%y%m%d")
    return date.isocalendar()[1]

def get_month(date_str):
    return date_str[:4]


print("아래 기능을 사용할 수 있습니다.")
print("이번 주 지출/이번 달 지출/주별 평균 사용량/월별 평균 사용량/고정지출 합계/잔고고려 AI 식사추천")

while True:
    m = input("동작을 입력하세요")

    if m == "이번 주 지출":
        print("이번 주 지출은 {}원입니다.")
    elif m == "이번 달 지출":
        print("이번 달 지출은 {}원입니다.")
    elif m == "주별 평균 사용량":
        print("주별 평균 사용량은 {}원입니다.")
    elif m == "월별 평균 사용량":
        print("월별 평균 사용량은 {}원입니다.")
    elif m == "월별 고정지출 합계":
        print("월별 고정지출 합계는 {}원입니다.")
    elif m == "잔고고려 AI 식사추천":
        print("오늘 식사는 {}입니다.")
    elif m == ("x"):
        break
    else:
        print("다시 입력하세요")
        continue