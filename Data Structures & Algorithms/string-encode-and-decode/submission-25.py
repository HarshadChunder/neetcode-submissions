class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for text in strs:
            encoded.append(str(len(text)) + '#' + text)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        hash_idx = s.find("#", i)
        strs = []

        while hash_idx != -1:
            length = int(s[i: hash_idx])
            i = hash_idx + length + 1

            strs.append(s[hash_idx + 1: i])
            hash_idx = s.find("#", i)

        return strs