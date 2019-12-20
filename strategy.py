import types


class Strategy(object):

    def __init__(self, func=None):
        if func is not None:
            # take a function, bind it to this instance, and replace the default bound method 'execute' with this new bound method.
            self.execute = types.MethodType(func, self)
            self.name = '{}_{}'.format(self.__class__.__name__, func.__name__)
        else:
            self.name = "Strategy default"

    def execute(self):
        print('Default method')
        print('{}\n'.format(self.name))

def execute_replacement1(self):
    print('Replacement1 method')
    print('{}\n'.format(self.name))


def execute_replacement2(self):
    print('Replacement2 method')
    print('{}\n'.format(self.name))

def main():

    s0 = Strategy()
    s0.execute()

    s1 = Strategy(execute_replacement1)
    s1.execute()

    s2 = Strategy(execute_replacement2)
    s2.execute()


main()