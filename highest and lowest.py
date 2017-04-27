def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))


def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return "{} {}".format(max(n), min(n))


def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])


def high_and_low(numbers):
    nums = map(int, numbers.split(" "))
    return " " .join(map(str, (max(nums), min(nums))))


def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))


