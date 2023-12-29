def can_segment(s, word_set):
    segment = ''
    for char in s:
        segment += char
        if segment in word_set:
            segment = ''
        elif len(segment) > max(len(word) for word in word_set):
            return False
    return True

# Example usage:

word_set = {'i', 'am', 'a', 'student', 'at', 'skymaker'}
s = 'iamastudentatskymaker'
can_segment_s = can_segment(s, word_set)
print(can_segment_s)
