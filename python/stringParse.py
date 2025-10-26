def multiply_complex(num1: str, num2: str) -> str:
  result = ''

  # return the result as "<real>+<imag>i"
  a, b = num1.split('+')
  c, d = num2.split('+')
  b = b[:-1]
  d = d[:-1]

  a, b, c, d, = int(a), int(b), int(c), int(d)

  real = (a*c - b*d)
  imag = (a*d + b*c)
  result = str(real) + '+' + str(imag) + 'i'
  return result

print(multiply_complex("1+1i", "1+1i"))   # "0+2i"
print(multiply_complex("1+-1i", "1+-1i")) # "0+-2i"
print(multiply_complex("3+2i", "1+7i"))   # "-11+23i"

assert multiply_complex("1+1i", "1+1i") == "0+2i"
assert multiply_complex("1+-1i", "1+-1i") == "0+-2i"
assert multiply_complex("3+2i", "1+7i") == "-11+23i"
assert multiply_complex("0+2i", "0+2i") == "-4+0i"
assert multiply_complex("2+0i", "3+0i") == "6+0i"
assert multiply_complex("1+0i", "0+1i") == "0+1i"

print("All tests passed! 🎉")