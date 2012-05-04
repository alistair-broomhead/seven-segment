DIGITS_TEXT = [
' _     _  _     _  _  _  _  _ ',
'| |  | _| _||_||_ |_   ||_||_|',
'|_|  ||_  _|  | _||_|  ||_|  |'
]
DIGITS = dict((n, tuple( l[3*n:3*(n+1)] for l in DIGITS_TEXT )) for n in range(10))
LOOKUP = dict((v,k) for (k,v) in DIGITS.items())
def output(filename):
  with open(filename, 'w') as  out:
    for line in [[n]*10 for n in range(10)] + [range(10)]:
      chars = ['']*3
      for char in line:
        d = DIGITS[char]
        for i in xrange(3):
          chars[i] += d[i]
      for l in chars:
        out.write(l + '\n')
      out.write('\n')

def parse(lines):
  output = []
  i = 0
  max_len = max( len(l) for l in lines)
  lines = [l + ' '*(max_len - len(l)) for l in lines]
  while True:
    if i+2 > max_len:
      return output
    k = tuple(l[i:i+3] for l in lines)
    if k in LOOKUP:
      output.append(LOOKUP[k])
      i += 3
    elif [l[i] for l in lines] == [' ']*3:
      i += 1
    else:
      i = max_len


def read_file(input_name):
  with open(input_name) as input_file:
    lines = []
    for line in input_file:
      lines.append(line)
      if len(lines) == 3:
        out = parse(lines)
        if not out:
          del lines[0]
        else:
          print out
          lines = []

if __name__ == '__main__':
  read_file('input.txt')
