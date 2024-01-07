class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [
            s.index(c)
            for c in s
        ] == [
            t.index(c)
            for c in t
        ]


            

def test_example_1():
    s = Solution()
    assert s.isIsomorphic('egg', 'add') == True
