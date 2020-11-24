#represents characters that may be confused with one another
#that is, near each other or having a similar sound
characters = {"a": {"q", "w", "s", "z", "e", "u"}, 
            "b": {"v", "g", "h", "n"},
            "c": {"x", "d", "f", "v", "k", "s", "ck"},
            "d": {"s", "e", "r", "f", "c", "x"},
            "e": {"w", "r", "d", "s", "a", "y"},
            "f": {"d", "r", "g", "v", "c"},
            "g": {"f", "t", "h", "b", "v", "j"},
            "h": {"g", "y", "j", "n", "b"},
            "i": {"u", "o", "k", "e"},
            "j": {"u", "i", "k", "m", "n", "h", "g"},
            "k": {"i", "o", "l", "m", "j", "u", "c", "ck"},
            "l": {"o", "p", "k"},
            "m": {"n", "j", "k"},
            "n": {"b", "h", "j", "m"},
            "o": {"p", "l", "k", "i"},
            "p": {"l", "o"},
            "q": {"w","a"},
            "r": {"e","d","f","t"},
            "s": {"a","w","d", "x", "z", "c"},
            "t": {"r","f","g","y"},
            "u":{"y", "j", "i"},
            "v": {"c", "f", "g","b"},
            "w": {"q", "a", "s", "d", "e"},
            "x": {"z","s","d","c"},
            "y":{"e", "t", "h", "u"},
            "z":{"a", "s", "x"}}

wordsChecked = {}

