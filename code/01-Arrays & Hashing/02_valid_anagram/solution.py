from collections import Counter


class SortedSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class CounterSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class HashMapSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True


class OnlyOneHashMapSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count[t[i]] = count.get(t[i], 0) - 1

        for c in count:
            if count[c] != 0:
                return False

        return True
