from Solution import day_of_week

print(day_of_week(1, 1, 1971))  # Expected Output: "Friday"
print(day_of_week(31, 12, 2100))  # Expected Output: "Friday"
print(day_of_week(29, 2, 2000))  # Expected Output: "Tuesday" (Leap Year)
print(day_of_week(29, 2, 2100))  # Expected Output: "Monday" (Not a Leap Year)
print(day_of_week(15, 8, 2023))  # Expected Output: "Tuesday"
print(day_of_week(26, 5, 2023))  # Expected Output: "Friday"
