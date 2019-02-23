from korean import manager

m = manager.koreanManager("홍김길두동령")
cjj = m.convert()
print(cjj)
cjjCount0 = m.countType0(cjj)
print(cjjCount0)
cjjCount1 = m.countType1(cjj)
print(cjjCount1)