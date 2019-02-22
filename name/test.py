from name import manager

hong = manager.nameManager("홍길동")
kim = manager.nameManager("김두령")

if hong.isString() and kim.isString():
    if hong.checkLen() and kim.checkLen():
        if hong.isKorean() and kim.isKorean():
            names = manager.namesManager(hong.getName(), kim.getName())
            print(names.mixNames())
        else:
            print("Error Language")
    else:
        print("Error Length")
else:
    print("Error Type")
