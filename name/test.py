from name import manager

hong = manager.nameManager("홍길동")
if hong.isString():
    if hong.checkLen():
        if hong.isKorean():
            print(hong.getName())
        else:
            print("Error Language")
    else:
        print("Error Length")
else:
    print("Error Type")
