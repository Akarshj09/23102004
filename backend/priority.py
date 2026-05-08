import requests
from datetime import datetime

API_URL = "http://4.224.186.213/evaluation-service/notifications"

response = requests.get(API_URL)

data = response.json()

notifications = data["notifications"]

priority_weight = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

def calculate_score(notification):

    type_score = priority_weight.get(
        notification["Type"], 0
    )

    timestamp = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    recency_score = timestamp.timestamp()

    final_score = (
        type_score * 1000000000
        + recency_score
    )

    return final_score

sorted_notifications = sorted(
    notifications,
    key=calculate_score,
    reverse=True
)

top_10 = sorted_notifications[:10]

print("\nTOP 10 PRIORITY NOTIFICATIONS\n")

for i, notif in enumerate(top_10, start=1):

    print(f"{i}.")
    print("Type:", notif["Type"])
    print("Message:", notif["Message"])
    print("Timestamp:", notif["Timestamp"])
    print("-" * 40)