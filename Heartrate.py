age= int(input("Enter your age: "))
heart_rate = 220-age
print("Heart rate is " ,heart_rate,  "bpm")
lowest = 0.5
highest = 0.85
lowest_heart_rate = heart_rate * lowest
highest_heart_rate = heart_rate * highest
print("The range of the user's target heart rate is " ,lowest_heart_rate,   "bpm" ,highest_heart_rate,  "bpm")

