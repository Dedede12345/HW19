# Ex.3

class RealString:
    """
    Real string class
    """

    def __init__(self, word):
        self.word = word
        self.length = len(word)


    @classmethod
    def compare_both(cls, arg1, arg2, func: str):
        comparison = f"{arg_1.length} {func} {arg2.length}"
        result = eval(comparison)
        print(f"{arg1.word} {func} {arg2.word} is {result}")


    def compare_with_string(self, string: str, func: str):
        comparison = f"{arg_1.length} {func} {len(string)}"
        result = eval(comparison)
        print(f"{self.word} {func} {string} is {result}")


arg_1 = RealString("Apple")
arg_2 = RealString("Яблоко")
RealString.compare_both(arg_1, arg_2, ">")
arg_1.compare_with_string("Яблоко", "<=")