habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True)
]


def habit_report(habits):
    completed = 0

    for habit_name, status in habits:
        if status:
            completed += 1

    return {
        "completed": completed,
        "total": len(habits)
    }

for habit_name, status in habits:
    if status:
        print(f"{habit_name}: Done")
    else:
        print(f"{habit_name}: Not done")


print(habit_report(habits))