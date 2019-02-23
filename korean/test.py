from korean import manager

m = manager.koreanManager("홍김길두동뷁")
cjj = m.convert()
print(cjj)
cjjCount0 = m.countType0(cjj)
print(cjjCount0)
print(m.sum(cjjCount0))

# cjjCount1 = m.countType1(cjj)
# print(cjjCount1)
# print(m.sum(cjjCount1))