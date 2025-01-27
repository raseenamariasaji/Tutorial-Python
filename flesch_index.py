text=open("text.txt","r")
s=text.read()
w=s.split()
total_sentence=0
total_syllable=0
total_words=len(w)
for char in s:
    if char in ["?", "!", ";", ":", "."]:
        total_sentence=total_sentence+1
    if char.lower() in ["a", "e", "i", "o", "u","A","E","I","O","U"]:
        total_syllable=total_syllable+1
score=206.835-(1.015*(total_words/total_sentence))-(84.6*(total_syllable/total_words))
grade=(0.39*(total_words/total_sentence))+(11.8*(total_syllable/total_words))-15.59
print("Score: ",score)
print("Grade: ",grade)
if score>=0 and score<30:
    print("Graduate level (Very difficult)")
elif score>=30 and score<50:
    print("College level (Difficult)")        
elif score>=50 and score<60:
    print("10th-12th grade level (Fairly difficult)")
elif score>=60 and score<70:
    print("8th-9th grade level (Standard)")        
elif score>=70 and score<80:
    print("7th grade level (Fairly easy)")
elif score>=80 and score<90:
    print("6th grade level (Easy)")
elif score>=90 and score<=100:
    print("5th grade level (Very easy)")