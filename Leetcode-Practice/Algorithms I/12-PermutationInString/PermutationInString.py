class Solution:        
        
    def TLE_checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        h1 = {}
        h2 = {}
        for i in range(window_size):
            if (s1[i] not in h1):
                h1[s1[i]] = 1
                h2[s1[i]] = 0
            else:
                h1[s1[i]] += 1
        
        substring = [];
        i = 0
        while (i < len(s2)):
            substring.append(s2[i])
            if (s2[i] in h2):
                h2[s2[i]] += 1
            if (len(substring)==window_size):
                if (h2 == h1):
                    return True
                i -= window_size-1
                substring = []
                h2 = h2.fromkeys(h2, 0)
            i += 1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_frequencies = {}
        start = matches = 0
        
        # keep track of distinct chars and their frequencies/count
        for char in s1:
            if char not in s1_frequencies:
                s1_frequencies[char] = 0
            s1_frequencies[char] += 1
        
        for end in range(len(s2)):
            char = s2[end]
            # if we run into a char thats in our s1 hashmap - decrement
            if char in s1_frequencies:
                s1_frequencies[char] -= 1
                # if 0 we know we have a match for this character
                if s1_frequencies[char] == 0:
                    matches += 1
            # number of matches = number of distinct chars in s1 -> we have a permutation
            if matches == len(s1_frequencies):
                return True
            # only consider window sizes of s1 length
            window_size = end - start + 1
            if window_size >= len(s1):
                char_to_remove = s2[start]
                start += 1
                
                if char_to_remove in s1_frequencies:
                    # if we are removing a char that had a match, decrement match count
                    if s1_frequencies[char_to_remove] == 0:
                        matches -= 1
                    # add back count to frequency map
                    s1_frequencies[char_to_remove] += 1
        
        return False

            