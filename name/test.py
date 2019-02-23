from name import manager

hong = manager.nameManager("홍길동")
kim = manager.nameManager("김두령")

if hong.verification() and kim.verification():
    names = manager.namesManager(hong.getName(), kim.getName())
    print(names.mixNames())