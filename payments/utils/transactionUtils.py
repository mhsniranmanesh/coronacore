import random
import string

from payments.models.transaction import CashIn


def random_string_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_factor_generator(new_factor_num=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_factor_num is not None:
        factor_num = new_factor_num
    else:
        factor_num = random_string_generator(size=8)

    factor_exists = CashIn.objects.filter(factor_number=factor_num).exists()
    if factor_exists:
        factor_num = random_string_generator(size=8)
        return unique_factor_generator(new_factor_num=factor_num)

    return factor_num
