import fire

def hello(name="World"):
  return "Hello %s! What a cool app" % name

if __name__ == '__main__':
  fire.Fire(hello)
