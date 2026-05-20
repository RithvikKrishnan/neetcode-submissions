class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 1000
        for string in strs:
            minLength = min(len(string), minLength)
        if minLength == 0:
            return ""
        answer = []
        for i in range(minLength):
            c = strs[0][i]
            for string in strs:
                if string[i] != c:
                    return "".join(answer)
            answer.append(c)
        return "".join(answer)

        