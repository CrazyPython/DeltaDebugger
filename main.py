import os.path,random
def fuzzer(maxlength=1024,t = str):
  if t == str:
    string_length = int(random.random() * maxlength)   
    out = ""
    for i in range(0, string_length):
      out += chr(int(random.random() * 96 + 32)) 
  elif t == int:
    out = random.randomint(0,maxlength)
  elif t == float:
    out = random.random()
  elif t == list:
    #nesting not supported
    #random list
    #recursive
    length = random.random * maxlength 
    gentypes = [random.choice(str,int,float) for i in range(length)]
    out = [fuzzer(maxlength,ty) for I,ty in zip(length,gentypes)]
  return out
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
def pythontest(cod,mode,fuzzertype):
  url = writetemp(code)
  if mode == "program"
    try:
        execfile(url)
    except:
        return "FAIL"
    else:
        return "PASS"
  else:
    try:
        execfile(url,locals = [fuzzer(fuzzertype)])
    except:
        return "FAIL"
    else:
        return "PASS"
def ddmin(s,tester=pythontest,mode = "program",fuzzertype=str): #mode is "program" or "function"(fuzzer)
    test = lambda code:tester(code,mode,fuzzertype)
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
