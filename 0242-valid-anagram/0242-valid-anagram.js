/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let collection = {}

    for (var i in s) {
        let char = s[i]
        if (char in collection) {
            collection[char] += 1
        } else {
            collection[char] = 1
        }
    }
    
    for (var j in t) {
        let char = t[j]
        if (!char in collection) {
            return false
        } else {
                collection[char] -= 1
        }
    }

    for (var k in collection) {
        if (collection[k] != 0) {
            return false;
        }
    }

    return true;
    
};