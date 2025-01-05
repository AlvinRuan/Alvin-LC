/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let collection = {}

    for (var i in s) {
        if (s[i] in collection) {
            collection[s[i]] += 1
        } else {
            collection[s[i]] = 1
        }
    }
    
    for (var j in t) {
        if (!t[j] in collection) {
            return false
        } else {
                collection[t[j]] -= 1
        }
    }

    for (var k in collection) {
        if (collection[k] != 0) {
            return false;
        }
    }

    return true;
    
};