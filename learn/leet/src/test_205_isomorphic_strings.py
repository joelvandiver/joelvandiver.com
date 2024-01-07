class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_idx: dict[str, set[int]] = {}
        t_idx: dict[str, set[int]] = {}
        for i, c in enumerate(s):
            if c in s_idx:
                s_idx[c].add(i)
            else:
                s_idx[c] = {i}
        for i, c in enumerate(t):
            if c in t_idx:
                t_idx[c].add(i)
            else:
                t_idx[c] = {i}
        s_values = list(s_idx.values())
        t_values = list(t_idx.values())
        for idx in s_values:
            if idx not in t_values:
                return False
        return True
        

def test_example_1():
    s = Solution()
    assert s.isIsomorphic('egg', 'add') == True
