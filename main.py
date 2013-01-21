import os.path
def writetemp(what):
  if not os.path.exists("temp"):
    f = open(test)
    f.write(what)
    f.close()
    return where
  elif not os.path.exists("test"):
    f = open(test)
    f.write(what)
    f.close()
    return where
  else:
    import sys,time
    sys.err.write("ERROR:Directory needs to not have temp or test so deltadebugger can write a temporary file")
    time.sleep(20)
    sys.exit()
def pythontest(input):
  url = writetemp(input)
  try:
    execfile(url)
  except:
    return "FAIL"
  else:
    return "PASS"
def ddmin(s,test):
    if test(s) == "FAIL":
      print "Works"
    n = 2     # Initial granularity
    while len(s) >= 2:
        start = 0
        subset_length = len(s) / n
        some_complement_is_failing = False

        while start < len(s):
            complement = s[:start] + s[start + subset_length:]

            if test(complement) == "FAIL":
                s = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break
                
            start += subset_length

        if not some_complement_is_failing:
            if n == len(s):
                break
            n = min(n *2, len(s))
        return s
