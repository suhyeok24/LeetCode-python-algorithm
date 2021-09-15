class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        letters,digitals=[],[] # 튜플처럼 입력 ㄱㄴ
        for log in logs:
            if log.split()[1].isdigit():
                digitals.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        #기준 2개 이상이면 튜플로 묶어줘야 한다.
        return letters + digitals
    # sort에 2가지 기준을 걸어주면 첫번째가 우선이고 두번째는 후순위(첫번째 동일할때)