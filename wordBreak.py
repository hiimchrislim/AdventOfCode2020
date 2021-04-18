def wordBreak(s, wordDict) -> bool:
    return is_segment(s, wordDict, 0)


def is_segment(s, wordDict, i):
    if i == len(s):
        return s in wordDict
    if s[0:i] in wordDict:
        return is_segment(s[i:], wordDict, 0) or is_segment(s, wordDict, i + 1)
    return is_segment(s, wordDict, i + 1)
