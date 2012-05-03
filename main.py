DIGITS = {
    0 : (
      ' _ ',
      '| |',
      '|_|'),
    1 : (
      '   ',
      '  |',
      '  |'),
    2 : (
      ' _ ',
      ' _|',
      '|_ '),
    3 : (
      ' _ ',
      ' _|',
      ' _|'),
    4 : (
      '   ',
      '|_|',
      '  |'),
    5 : (
      ' _ ',
      '|_ ',
      ' _|'),
    6 : (
      ' _ ',
      '|_ ',
      '|_|'),
    7 : (
      ' _ ',
      '  |',
      '  |'),
    8 : (
      ' _ ',
      '|_|',
      '|_|'),
    9 : (
      ' _ ',
      '|_|',
      '  |'),
    }
LOOKUP = dict((v,k) for (k,v) in DIGITS.items())
def output(filename):
  with open(filename, 'w') as  out:
    for line in [
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2],
        [3,3,3,3,3,3,3,3,3,3],
        [4,4,4,4,4,4,4,4,4,4],
        [5,5,5,5,5,5,5,5,5,5],
        [6,6,6,6,6,6,6,6,6,6],
        [7,7,7,7,7,7,7,7,7,7],
        [8,8,8,8,8,8,8,8,8,8],
        [9,9,9,9,9,9,9,9,9,9],
        [0,1,2,3,4,5,6,7,8,9],
        ]:
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
