from name import manager

nManager = manager.names(name1="asa", name2="김기덕")
mixNames =  nManager.mixNames()
if mixNames :
    print(mixNames)
else:
    print("재시도해 주세요.")