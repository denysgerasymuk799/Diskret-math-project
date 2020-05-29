import re


def inversion_by_module(base, module):
    """
    Return inverted by give module number
    :param base: int
    :param module: int
    :return: int
    """
    s_list = [1, 0]
    t_list = [0, 1]
    q_list = [0]

    def extended_Euclidean_alg(k):
        for i in range(1, len(q_list) - 1):
            s = s_list[i - 1] - q_list[i] * s_list[i]
            t = t_list[i - 1] - q_list[i] * t_list[i]
            s_list.append(s)
            t_list.append(t)
        return s_list[-1] % k

    def Euclidean_alg(n, k):
        if k == 0:
            return extended_Euclidean_alg(module)
        else:
            t1, t2 = divmod(n, k)
            q_list.append(t1)
            return Euclidean_alg(k, t2)

    return Euclidean_alg(base, module)


def deciphering_code(codes_lst):
    """
    Converts deciphered code of integers into words
    :param codes_lst: list(int)
    :return: str
    """
    message = ""
    for code in codes_lst:
        second_letter_code = code % 100
        first_letter_code = code // 100

        letter1 = chr(first_letter_code + 97)
        letter2 = chr(second_letter_code + 97)
        message += letter1 + letter2

    return message


def translate_into_ints(message):
    """
    Translate message into list of ints
    :param message: str
    :return: list(int)
    """
    message = re.sub(r'[^A-Za-z]', '', message)
    if len(message) % 2 == 1:
        message += "a"
    message_ = message.lower()
    result = []
    for bite in range(len(message_) // 2):
        result.append(
            int("".join([str(ord(letter) - ord("a")).zfill(2)
                         for letter in message_[bite * 2: bite * 2 + 2]])))
    return result


def modular_degree(base, degree, module):
    """
    Fast modular raising to a degree
    :param base: int
    :param degree: int
    :param module: int
    :return: int
    """
    result = 1
    power = base % module
    while degree:
        if degree & 1:
            result = (result * power) % module
        power = power ** 2 % module
        degree >>= 1
    return result


def decoder(message, p, q, e):
    """
    Decode message encoded with RSA and
    returns list of strings of integers that represents
    letters in message
    :param message: str
    :param p: prime int
    :param q: prime int
    :param e: int mutually prime to p and q
    :return: str
    """
    decoded_message = []
    message = [int(num) for num in message.replace(",", "").split()]
    d = inversion_by_module(e, (p - 1) * (q - 1))
    n = p * q
    for bite in message:
        decoded_message.append(modular_degree(bite, d, n))
    return deciphering_code(decoded_message)


if __name__ == '__main__':
    print(decoder("3185, 2038, 2460, 2550", 53, 61, 17))
    print(decoder("667, 1947, 671", 59, 43, 13))
