class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts=collections.defaultdict(int)  #value의 형태를 int
        for word in words:
            counts[word]+=1
        return max(counts,key=counts.get)
