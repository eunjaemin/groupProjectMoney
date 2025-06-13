from datetime import datetime
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="",
)

records = []

print("@@지출 관리 프로그램@@")
print("날짜에 x를 입력하여 종료하세요")

while True:
    # 입력받는 부분
    date = input("날짜를 입력하세요(YYMMDD): ")
    if date.strip() == 'x':
        break
    item = input("항목을 입력하세요: ")
    price = input("금액을 입력하세요: ")
    category = input("분류를 입력하세요: ")
    fixed = input("고정지출이면 y, 아니면 n을 입력하세요: ")
    record = {"date": date,
              "item": item,
              "price": int(price),
              "category": category
    }
    records.append(record)


# 기능 구현을 위한 함수들
def get_week(date_str):
    date = datetime.strptime(date_str, "%y%m%d")
    return date.isocalendar()[1]

def get_month(date_str):
    return date_str[:4]

def total_this_week(records):
    this_week = datetime.now().isocalendar()[1]
    return sum(r['price'] for r in records if get_week(r["date"]) == this_week)

def total_this_month(records):
    this_month = datetime.now().strftime("%y%m")
    return sum(r["price"] for r in records if get_month(r["date"]) == this_month)

def fixed_expense(records):
    return sum(r["price"] for r in records if r.get("fixed", False))

def average_weekly(records):
    weeks = {get_week(r["date"]) for r in records}
    return sum(r["price"] for r in records) // len(weeks) if weeks else 0

def average_monthly(records):
    months = {get_month(r["date"]) for r in records}
    return sum(r["price"] for r in records) // len(months) if months else 0


print("아래 기능을 사용할 수 있습니다.")

while True:
    # 기능 리스트들과 출력하는 부분
    m = input("동작을 입력하세요:\n"
    "1 = 이번 주 지출"
    "2 = 이번 달 지출"
    "3 = 주별 평균 사용량"
    "4 = 월별 평균 사용량"
    "5 = 월별 고정지출 합계"
    "6 = 잔고고려 AI 식사추천"
    "0 = 종료")

    if m == "1":
        print(f"이번 주 지출은 {total_this_week(records)}원입니다.")
    elif m == "2":
        print(f"이번 달 지출은 {total_this_month(records)}원입니다.")
    elif m == "3":
        print(f"주별 평균 사용량은 {average_weekly(records)}원입니다.")
    elif m == "4":
        print(f"월별 평균 사용량은 {average_monthly(records)}원입니다.")
    elif m == "5":
        print(f"월별 고정지출 합계는 {fixed_expense(records)}원입니다.")
    elif m == "6":
        salary = int(input('이번 달 월급을 입력하세요: '))
        total_spent = sum(r['price'] for r in records)
        balance = salary - total_spent
        prompt = f'내 잔고는 {balance}원이야. 오늘 식사 하나 추천해줘. 간단한 이유도 덧붙여줘'
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            extra_body={},
            model="meta-llama/llama-3.3-8b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
                ]
            )
        print(completion.choices[0].message.content)
    elif m == ("0"):
        break
    else:
        print("다시 입력하세요")
        continue