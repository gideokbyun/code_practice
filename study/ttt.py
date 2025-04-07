def getName(arg_name):
    return arg_name + "님"

def getGreeting(arg_name):
    greeting = arg_name + "안녕하세요"
    return greeting

def prtShow(arg_name):
    name = getName(arg_name)
    msg = getGreeting(name)
    print(f"name: {name} -> msg: {msg}")
prtShow("홍길동")