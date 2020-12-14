class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """回文排列
        1. 字符串排列组合之后生成回文字符串
        统计出现次数为奇数次的字符串个数，如果>1则无法形成回文字符串
        推导：
        字符串为偶数长度：
            奇数次的字符串必然是成对出现，不可能小于1
        字符串为奇数长度：
            如果大于1则无法对称
        """