import random

# 顧客のデータ
customers = [
    {
        'name': '顧客1',
        'address': '住所1',
        'fixed_schedule': False  # 固定日時の予約がない場合
    },
    {
        'name': '顧客2',
        'address': '住所2',
        'fixed_schedule': True  # 固定日時の予約がある場合
    },
    # 他の顧客データも同様に追加
    # ...
]

# スケジュールをランダムにシャッフル
random.shuffle(customers)

# 固定日時の予約がある顧客を別リストに分ける
fixed_schedule_customers = [
    customer for customer in customers if customer['fixed_schedule']]

print(fixed_schedule_customers)
other_customers = [
    customer for customer in customers if not customer['fixed_schedule']]

# 固定日時の予約がある顧客のスケジュールを設定
schedule = fixed_schedule_customers.copy()

# 固定日時の予約がない顧客のスケジュールを設定
for customer in other_customers:
    # エリアが近く効率よく回れるように、スケジュールに追加するロジックを実装する
    schedule.append(customer)

# スケジュールの出力
for i, customer in enumerate(schedule):
    print(f"訪問{i+1}: {customer['name']}（住所: {customer['address']}）")
