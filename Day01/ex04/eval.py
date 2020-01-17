class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return -1
        print(sum(x * len(keys) for (x, keys) in zip(coefs, words)))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return -1
        print(sum(len(word) * coefs[i] for i, word in enumerate(words)))
