def calculate_love_score(string1, string2):
    a = "trueTRUE"
    b = "loveLOVE"
    T = 0
    L = 0
    string3 = string1 + string2
    for char in string3:
        if char in a:
            T += 1
        if char in b:
            L += 1
    Love_Score = (T * 10) + L
    print(Love_Score)
calculate_love_score("Rishi", "Rishendra")
