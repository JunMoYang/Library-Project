"""
https://github.com/neotune/python-korean-handler
위의 소스를 응용하여 '초성' '중성' '종성'을 분리하고 각 각 '획수'를 계산합니다.

'국립국어원'에서는 'ㄱ'과 'ㄴ'의 획수가 '1' or '2', 어느쪽인지에 대한 답변을 아래와 같이 했습니다.
"한글의 획수에 대하여 따로 규정되어 있지 않으므로 안내해 드리기 어렵습니다."

때문에 '초.중.종성'의 '획수'는 '2가지'의 패턴으로 나누어서 개발합니다.


    [ 초성 중성 종성 분리 하기 ] 출처 : 위의 github 경로.
	유니코드 한글은 0xAC00 으로부터
	초성 19개, 중성21개, 종성28개로 이루어지고
	이들을 조합한 11,172개의 문자를 갖는다.
	한글코드의 값 = ((초성 * 21) + 중성) * 28 + 종성 + 0xAC00
	(0xAC00은 'ㄱ'의 코드값)
	따라서 다음과 같은 계산 식이 구해진다.
	유니코드 한글 문자 코드 값이 X일 때,
	초성 = ((X - 0xAC00) / 28) / 21
	중성 = ((X - 0xAC00) / 28) % 21
	종성 = (X - 0xAC00) % 28
	이 때 초성, 중성, 종성의 값은 각 소리 글자의 코드값이 아니라
	이들이 각각 몇 번째 문자인가를 나타내기 때문에 다음과 같이 다시 처리한다.
	초성문자코드 = 초성 + 0x1100 //('ㄱ')
	중성문자코드 = 중성 + 0x1161 // ('ㅏ')
	종성문자코드 = 종성 + 0x11A8 - 1 // (종성이 없는 경우가 있으므로 1을 뺌)
"""


class korean:
    # 유니코드 한글 시작 : 44032, 끝 : 55199
    __baseCode, __choSung, __jungSung = 44032, 588, 28

    # 초성 리스트. 00 ~ 18
    __choSungList = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    # 중성 리스트. 00 ~ 20
    __jungSungList = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ',
                      'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

    # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    __jongSungList = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ',
                      'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                      'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    __choSungListType0 = {'ㄱ': 1, 'ㄲ': 2, 'ㄴ': 1, 'ㄷ': 2, 'ㄸ': 4, 'ㄹ': 3, 'ㅁ': 3, 'ㅂ': 4,
                          'ㅃ': 8, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 2, 'ㅉ': 4, 'ㅊ': 3, 'ㅋ': 2,
                          'ㅌ': 3, 'ㅍ': 4, 'ㅎ': 3}
    __choSungListType1 = {'ㄱ': 2, 'ㄲ': 4, 'ㄴ': 2, 'ㄷ': 3, 'ㄸ': 6, 'ㄹ': 5, 'ㅁ': 4, 'ㅂ': 4,
                          'ㅃ': 8, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 3, 'ㅉ': 6, 'ㅊ': 4, 'ㅋ': 3,
                          'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3}

    __jungSungListType = {'ㅏ': 2, 'ㅐ': 3, 'ㅑ': 3, 'ㅒ': 4, 'ㅓ': 2, 'ㅔ': 3, 'ㅕ': 3, 'ㅖ': 4,
                          'ㅗ': 2, 'ㅘ': 4, 'ㅙ': 5, 'ㅚ': 3, 'ㅛ': 3, 'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 5,
                          'ㅟ': 3, 'ㅠ': 3, 'ㅡ': 1, 'ㅢ': 2, 'ㅣ': 1}

    __jongSungListType0 = {' ': 0, 'ㄱ': 1, 'ㄲ': 2, 'ㄳ': 3, 'ㄴ': 1, 'ㄵ': 3, 'ㄶ': 4, 'ㄷ': 2,
                           'ㄹ': 3, 'ㄺ': 4, 'ㄻ': 6, 'ㄼ': 7, 'ㄽ': 5, 'ㄾ': 6, 'ㄿ': 7, 'ㅀ': 6,
                           'ㅁ': 3, 'ㅂ': 4, 'ㅄ': 6, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 2, 'ㅊ': 3,
                           'ㅋ': 2, 'ㅌ': 3, 'ㅍ': 4, 'ㅎ': 3}
    __jongSungListType1 = {' ': 0, 'ㄱ': 2, 'ㄲ': 4, 'ㄳ': 4, 'ㄴ': 2, 'ㄵ': 5, 'ㄶ': 5, 'ㄷ': 3,
                           'ㄹ': 5, 'ㄺ': 7, 'ㄻ': 9, 'ㄼ': 9, 'ㄽ': 7, 'ㄾ': 9, 'ㄿ': 9, 'ㅀ': 8,
                           'ㅁ': 4, 'ㅂ': 4, 'ㅄ': 6, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 3, 'ㅊ': 4,
                           'ㅋ': 3, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3}

    def __init__(self, mixNames):
        self.__mixNames = list(mixNames)

    def __convert(self):
        result = list()
        for keyword in self.__mixNames:
            conver = ""
            char_code = ord(keyword) - self.__baseCode
            char1 = int(char_code / self.__choSung)
            conver += self.__choSungList[char1]
            char2 = int((char_code - (self.__choSung * char1)) / self.__jungSung)
            conver += self.__jungSungList[char2]
            char3 = int((char_code - (self.__choSung * char1) - (self.__jungSung * char2)))
            if char3 == 0:
                conver += ' '
            else:
                conver += self.__jongSungList[char3]
            result.append(list(conver))
        return result

    # 'ㄱ' : 1획 기준, 획수 계산.
    def countType0(self):
        cjjSungList = self.__convert()
        resultType0 = list()
        for v in cjjSungList:
            type0 = list()
            for i in range(len(v)):
                if i == 0:
                    type0.append(self.__choSungListType0[v[i]])
                elif i == 1:
                    type0.append(self.__jungSungListType[v[i]])
                else:
                    type0.append(self.__jongSungListType0[v[i]])
            resultType0.append(type0)

        return self.__sum(resultType0)

    # 'ㄱ' : 2획 기준, 획수 계산.
    def countType1(self):
        cjjSungList = self.__convert()
        resultType1 = list()
        for v in cjjSungList:
            type1 = list()
            for i in range(len(v)):
                if i == 0:
                    type1.append(self.__choSungListType1[v[i]])
                elif i == 1:
                    type1.append(self.__jungSungListType[v[i]])
                else:
                    type1.append(self.__jongSungListType1[v[i]])
            resultType1.append(type1)
        return self.__sum(resultType1)

    # 궁합계산
    def __sum(self, cjjSungCountList):
        sumList = list()
        result = list()
        for v in cjjSungCountList:
            sumValue = v[0] + v[1] + v[2]
            result.append(self.__checkNum(sumValue))
        for _ in range(len(result) * 3):
            if len(result) != 1:
                sumValue = result.pop(0) + result[0]
                sumList.append(self.__checkNum(sumValue))
            else:
                result.clear()
                result = list(sumList)
                sumList.clear()

        return ''.join(str(e) for e in result)

    def __checkNum(self, num):
        if num > 9:
            return int(str(num)[1:])
        else:
            return num
