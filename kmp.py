# python3
import sys


def compute_prefix_function(S):
    """
    Computes the prefix function of string S to be utilized in finding exact pattern matching (see find_pattern function)
    """
    s = [0 for _ in range(len(S))]
    s[0] = 0
    border = 0
    for i in range(1, len(S)):
        while border > 0 and S[i] != S[border]:
            border = s[border - 1]
        if S[i] == S[border]:
            border += 1
        else:
            border = 0

        s[i] = border

    return s


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text by implementing the Knuth-Morris-Pratt algorithm.
    example:
    input: pattern = 'ATAT' and text = 'G A T A T A T G C A T  A  T  A  C  T  T'
                                        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <-- index of letters
                                          A T A T <---------------------------------- full pattern found
                                              A T A T <------------------------------ full pattern found
                                                          A T  A  T <---------------- full pattern found
    output: result = [1, 3, 9]
    """

    # create a new string S by concatenating the Pattern, a $ sign, and the Text
    Str = pattern + '$' + text

    # compute the prefix function s of string S
    s = compute_prefix_function(Str)

    # traverse through prefix function s and find positions in Text where the full pattern appears
    result = []
    len_pattern = len(pattern)
    len_S = len(Str)
    for i in range(len_pattern + 1, len_S):
        if s[i] == len_pattern:
            result.append(i - 2 * len_pattern)

    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
