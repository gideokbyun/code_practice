#가변인자는 **kwargs
def student_score(name, **kwargs):
    total = kwargs['math'] + kwargs['english'] + kwargs['science']
    print(f"""{name}의 성적:
- math: {kwargs['math']}점
- english: {kwargs['english']}점
- science: {kwargs['science']}점
총점: {total}점""")


#학생의 이름과 여러 과목의 점수를 입력받아, 총 점수를 계산

student_score("민수", math=90, english=85, science=88)
