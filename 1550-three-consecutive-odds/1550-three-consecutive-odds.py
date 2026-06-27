class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ev = []
        found = False

        for i in arr:
            if i % 2 == 0:
                ev.append("Even")
            else:
                ev.append("Odd")


        for i in range(len(ev) - 2):
            if ev[i] == "Odd" and ev[i+1] == "Odd" and ev[i+2] == "Odd":
                found = True

        if found:
            return True
        else:
            return False