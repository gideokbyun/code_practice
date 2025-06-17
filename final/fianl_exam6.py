#TML 태그 이름과 이름을 매개변수로 받는다
def wrap_in_tag(a, b):
    return f"<{a}>{b}</{a}>"
#해당 태그로 감싸진 HTML 요소를 반환하는 함수 wrap_in_tag 작성
print(wrap_in_tag('p', 'hello'))
#print(wrap_in_tag('p', 'hello')) -> <p>hello</p>

