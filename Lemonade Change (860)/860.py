# Runtime: 48 ms
# Beats 93.71% of Python submissions

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        curr_change = {5 : 0, 10 : 0, 20 : 0}
        cost = 5
        change_owed = 0
        for bill in bills:
            if bill == 5:
                curr_change[bill] += 1
            # We owe change
            if bill - cost > 0:
                if bill == 20:
                    if curr_change[10] and curr_change[5]:
                        curr_change[10] -= 1
                        curr_change[5] -= 1
                    elif curr_change[5] >= 3:
                        curr_change[5] -= 3
                    else:
                        return False
                elif bill == 10:
                    curr_change[bill] += 1
                    if curr_change[5]:
                        curr_change[5] -= 1
                    else:
                        return False
        return True