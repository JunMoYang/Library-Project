from korean import manager

kManager = manager.korean(mixNames="a김길두동뷁")

resultSumType0 = kManager.countType0()
if resultSumType0:
    print(resultSumType0)
else:
    print("재시도해 주세요.")