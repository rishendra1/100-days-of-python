Scores = [123,234,145,456,231,345,789,567,459,111]
print("Given List is \n")
for score in Scores:
    print(score)
max_score = 0
for score in Scores:
    if score > max_score:
        max_score = score
print(f"The highest score is {max_score}")