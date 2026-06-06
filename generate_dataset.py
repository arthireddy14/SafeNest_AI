import pandas as pd
import random

data = []

for _ in range(1000):

    person = random.choice([
        "Known",
        "Unknown"
    ])

    time = random.choice([
        "Day",
        "Night"
    ])

    motion = random.choice([0, 1])

    door = random.choice([0, 1])

    window = random.choice([0, 1])

    vacation = random.choice([0, 1])

    previous_incidents = random.randint(0, 5)

    score = 0

    if person == "Unknown":
        score += 40

    if time == "Night":
        score += 20

    if motion:
        score += 10

    if door:
        score += 10

    if window:
        score += 15

    if vacation:
        score += 20

    score += previous_incidents * 3

    if score < 40:
        threat = "Low"

    elif score < 70:
        threat = "Medium"

    else:
        threat = "High"

    data.append([
        person,
        time,
        motion,
        door,
        window,
        vacation,
        previous_incidents,
        threat
    ])

df = pd.DataFrame(
    data,
    columns=[
        "person",
        "time",
        "motion",
        "door",
        "window",
        "vacation",
        "previous_incidents",
        "threat"
    ]
)

df.to_csv(
    "threat_dataset.csv",
    index=False
)

print("Dataset Saved")
print(df.head())