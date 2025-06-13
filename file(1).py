from datetime import datetime
import matplotlib.pyplot as plt


records = []

print("@@지출 관리 프로그램@@")
print("날짜에 x를 입력하여 종료하세요")

while True:
    # 입력받는 부분
    date = input("날짜를 입력하세요(YYMMDD): ")
    if date.strip() == 'x':
        break
    item = input("지출한 물품을 입력하세요: ")
    price = input("금액을 입력하세요: ")
    category = input("종류를 입력하세요:\n" \
                    "1 = 고정지출\n" \
                    "2 = 식비\n" \
                    "3 = 그외")
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

def average_weekly(records):
    weeks = {get_week(r["date"]) for r in records}
    return sum(r["price"] for r in records) // len(weeks) if weeks else 0

def average_monthly(records):
    months = {get_month(r["date"]) for r in records}
    return sum(r["price"] for r in records) // len(months) if months else 0

def draw_category_pie(records):
    category_names = {'1':'고정지출',
                      '2':'식비',
                      '3':'그외'}
    category_totals = {'1':0,'2':0,'3':0}

    for r in records:
        if r['category'] in category_totals:
            category_totals[r['category']]+=r['price']
    labels = [category_names[k] for k in category_totals]
    sizes = [category_totals[k] for k in category_totals ]

    plt.figure()
    plt.pie(sizes, labels=labels, autopct = '%1.1f%%')
    plt.title('종류별 지출')
    plt.show()

def draw_item_pie(records, target):
    category_names = {'1':'고정지출',
                      '2':'식비',
                      '3':'그외'}
    items_total = {}
    for r in records:
        if r['category'] == target:
            item = r['item']
            if item not in items_total:
                items_total[item]=0
            items_total[item] +=r['price']
    if not items_total:
        print(f'\'{category_names[target]}\'항목은 이번달 지출이 없습니다:)')

    labels = list(items_total.keys())
    sizes = list(items_total.values())

    plt.figure()
    plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
    plt.title('물품별 지출')
    plt.show()

def draw_date_pie(records):
    date_total = {}
    for r in records:
        date = r['date']
        price = r['price']
        if date not in date_total:
            date_total[date] = 0
        date_total[date] += price

    if not date_total:
        print('해당 날짜엔 지출이 없습니다:)')
        return
    
    labels = list(date_total.keys())
    sizes = list(date_total.values())

    plt.figure()
    plt.pie(sizes, labels = labels ,autopct = '%1.1f%%')
    plt.title('날짜별 지출')
    plt.show()

print("아래 기능을 사용할 수 있습니다.")

while True:
    # 기능 리스트들과 출력하는 부분
    m = input("동작을 입력하세요:\n"
    "1 = 이번 주 지출\n"
    "2 = 이번 달 지출\n"
    "3 = 주별 평균 사용량\n"
    "4 = 월별 평균 사용량\n"
    '5 = 월 분류 항목별 지출 비율\n'
    '6 = 월 고정지출 항목별 지출 비율\n'
    '7 = 월 식비 항목별 지출 비율\n'
    '8 = 월 그외 항목별 지출 비율\n'
    '9 = 해당 월 날짜별 지출'
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
        draw_category_pie(records)
    elif m == "6":
        draw_item_pie(records, '1')
    elif m == "7":
        draw_item_pie(records, '2')
    elif m == "8":
        draw_item_pie(records, '3')
    elif m == '9':
        draw_date_pie(records)
    elif m == ("0"):
        break
    else:
        print("다시 입력하세요")
        continue