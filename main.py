from korean import manager as krMgr
from name import manager as nameMgr

if __name__ == '__main__':
    while True:
        name1, name2 = input("[ 이름을 입려해주세요 ]\n"
                             "( ex> input : 홍길동 이순신 )\n"
                             "input : ").split()

        nMgr = nameMgr.names(name1=name1, name2=name2)
        mixNames = nMgr.mixNames()
        if mixNames:
            kMgr = krMgr.korean(mixNames=mixNames)
            resultSumType0 = kMgr.countType0()
            if resultSumType0:
                print("'ㄱ' 1획 기준 결과 : ", resultSumType0)

            resultSumType1 = kMgr.countType1()
            if resultSumType1:
                print("'ㄱ' 2획 기준 결과 : ", resultSumType1)
        print("\n")