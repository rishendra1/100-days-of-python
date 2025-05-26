class Subject:
  def __init__(self, name, highest_score, cutoff):
    print("Entering the details................")
    self.name = name
    self.highest_score = highest_score
    self.cutoff = cutoff
    print("Given details by the user: ")
    print(f"Subject Name: {self.name}\nHighest Score: {self.highest_score}\nCutoff: {self.cutoff}")
  def grade(self,marks):
    S = self.highest_score
    C = self.cutoff
    if marks > 0:
        if S - C < marks <= S:
            print("O grade")
        elif S - 2*C < marks <= S - C:
            print("A+ grade")
        elif S - 3*C < marks <= S - 2*C:
            print("A grade")
        elif S - 4*C < marks <= S - 3*C:
            print("B+ grade")
        elif S - 5*C < marks <= S - 4*C:
            print("B grade")
        elif S - 6*C < marks <= S - 5*C:
            print("C grade")
        elif S - 7*C < marks <= S - 6*C:
            print("D grade")
        elif S-8*C < marks <= S - 7*C:
            print("E grade")
        elif S-9*C < marks <= S-8*C:
            print("F grade")
        elif S-10*C < marks <= S-9*C:
            print("G grade")
    else:
            print("Marks are invalid")
while True:
     Subject_Name = input("Enter Subject Name: ")
     Highest_Score = int(input("Enter Highest Score: "))
     Cutoff = int(input("Enter Cutoff for each grade: "))
     s1 = Subject(Subject_Name, Highest_Score, Cutoff)
     Marks = int(input("Enter Marks: "))
     s1.grade(Marks)
     choice = input("Do you want to continue? - (yes/no): ").lower()
     if choice == "yes":
         continue
     elif choice == "no":
         print("Thank you for using Grade Calculator")
         break

