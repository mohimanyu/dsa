def wrapLines(words, k):
    result = []
    sub_sentence = ""

    for i in words:
        # Avoid leading '-'
        temp = (sub_sentence + "-" + i) if sub_sentence else i
        if len(temp) <= k:
            sub_sentence = temp
        else:
            # Save previous line
            result.append(sub_sentence)
            # Start new line
            sub_sentence = i

    # Append last line
    if sub_sentence:
        result.append(sub_sentence)

    return result


# Test cases
words1 = [
    "The",
    "day",
    "began",
    "as",
    "still",
    "as",
    "the",
    "night",
    "abruptly",
    "lighted",
    "with",
    "brilliant",
    "flame",
]
words2 = ["Hello"]
words3 = ["Hello", "Hello"]
words4 = ["Well", "Hello", "world"]
words5 = ["Hello", "HelloWorld", "Hello", "Hello"]
words6 = ["a", "b", "c", "d"]

print(wrapLines(words1, 13))
