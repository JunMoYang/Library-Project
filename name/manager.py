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
        if len(self.__name) == 3 :
            return True
        else:
            return False