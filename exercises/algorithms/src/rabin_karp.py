

def detect_plagiarism(source, submission):

    q = 101  # prime number
    d = 256  # number of possible input characters
    n = len(source)  # length of source
    m = len(submission)  # length of submission
    p = 0  # hash value for submisson
    t = 0  # hash value for source
    h = 1  # hash of the index

    # TODO - explain me
    for i in range(m - 1):
        h = (h * d) % q

    # calculating the hash for the first window of text
    for i in range(m):
        p = (d * p + ord(submission[i])) % q
        t = (d * t + ord(source[i])) % q

    # slide the text over the pattern one by one
    for i in range(n - m + 1):
        # check to see if hashes are the same
        if p == t:
            return True

        # calculate next hash value for t
        if i < m - n:
            t = (d * (t - ord(source[i]) * h) + ord(source[i + m])) % q

            # We might get negative values of t, converting it to positive
            if t < 0:
                t += q

    return False
