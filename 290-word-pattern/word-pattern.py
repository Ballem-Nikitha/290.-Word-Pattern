class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        chartoword = {}
        wordtochar = {}

        for p, w in zip(pattern, words):
            if p in chartoword and chartoword[p] != w:
                return False
            if w in wordtochar and wordtochar[w] != p:
                return False
            chartoword[p] = w
            wordtochar[w] = p

        return True
