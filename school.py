student_name=input("ENTER STUDENT NAME: ")
coursework_mark=int(input("ENTER COURSEWORK MARK: "))
exam_score=int(input("EXAM SCORE: "))
exam_score_outof_70=(exam_score/100*70)

print(exam_score/100*70)
final_score=(exam_score_outof_70+coursework_mark)
print(final_score)
print(f"NAME\t{student_name}\nCOURSEWORK MARKS\t{coursework_mark}\nEXAM SCORE OUT OF 70\t{exam_score_outof_70}\nFINAL\t{final_score}")
