import unicodedata


# "nameManager"는 'name'의 '유효성 검사'및 '필요한 기능'들이 포함됩니다.
class nameManager:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isString(self):
        if type(self.__name) == str:
            return True
        else:
            return False

    def isKorean(self):
        for v in self.__name:
            if unicodedata.name(v).find("HANGUL") != -1:
                continue
            else:
                return False

        return True

    def checkLen(self):
        if len(self.__name) == 3:
            return True
        else:
            return False


# "namesManager"은 '2개의 이름'에 관련된 기능이 포함됩니다.
class namesManager:
    def __init__(self, name1, name2):
        self.__name = {}
        self.__name1 = name1
        self.__name2 = name2

    # 'name1'과 'name2'의 이름을 번갈아 가면서 'name'에 기입합니다.
    # 'name1[0]', 'name2[0]', 'name1[1]', 'name2[1]' ...
    def mixNames(self):
        for i in range(3):
            if i != 0:
                self.__name[i + i] = self.__name1[i]
            else:
                self.__name[i] = self.__name1[i]
        for i in range(3):
            if i == 0:
                self.__name[i + 1] = self.__name2[i]
            else:
                self.__name[i + i + 1] = self.__name2[i]

        return self.__name