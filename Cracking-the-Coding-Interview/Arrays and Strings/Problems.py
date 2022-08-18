#1 Is Unique
def isUnique(s):
    if len(s) > 128: 
        return False
    seen = set()
    for c in s: 
        if c in seen:
            return False
        seen.add(c)
    return True 

#2 Check Permutation
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_hash = {}
    s2_hash = {}
    for i in range(len(s1)):
        s1_hash[s1[i]] = 1 + s1_hash.get(s1[i], 0)
        s2_hash[s2[i]] = 1 + s2_hash.get(s2[i], 0)
    return s1_hash == s2_hash

#3 URLify
def urlify(s, length):
    s = s.strip()
    s = s.split(' ')
    new_s = ''
    for c in s:
        new_s += c + '%20'
    return new_s

# Test 
if __name__ == '__main__':
    # Test 1
    print('isUnique(\'abcabc\'): ', isUnique('abcabc'))
    print('isUnique(\'abcdef\'): ', isUnique('abcdef'))

    # Test 2
    print('checkPermutation(\'abcdef\', \'fedcba\'): ', checkPermutation('abc', 'cba'))
    print('checkPermutation(\'abcdef\', \'fedcba\'): ', checkPermutation('abc', 'fed'))

    # Test 3
    print('urlify(\'Mr John Smith    \', 13): ', urlify('Mr John Smith    ', 13))
