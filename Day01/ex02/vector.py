

class Vector:
    def __init__(self, lst):
        self.values = lst

    @classmethod
    def by_size(self, size):
        i = 0
        self.values = []
        while i < size:
            self.values.append(float(i))
            i += 1
        return self(self.values)

    @classmethod
    def by_range(self, v_min, v_max):
        i = 0
        self.values = []
        while (v_min < v_max):
            self.values.append(float(v_min))
            v_min += 1
            i += 1
        return self(self.values)

    def __add__(self, v2):
        if isinstance(v2, Vector) and len(self.values) == len(v2.values):
            for i in range(len(self.values)):
                self.values[i] += v2.values[i]
        elif isinstance(v2, int) or isinstance(v2, float):
            for i in range(len(self.values)):
                self.values[i] += float(v2)

    def __radd__(self, nb):
        self.__add__(self, nb)

    def __sub__(self, v2):
        if isinstance(v2, Vector) and len(self.values) == len(v2.values):
            for i in range(len(self.values)):
                self.values[i] -= v2.values[i]
        elif isinstance(v2, int) or isinstance(v2, float):
            for i in range(len(self.values)):
                self.values[i] -= float(v2)

    def __rsub__(self, nb):
        self.__sub__(self, nb)

    def __mul__(self, v2):
        if isinstance(v2, Vector) and len(self.values) == len(v2.values):
            for i in range(len(self.values)):
                self.values[i] *= v2.values[i]
        elif isinstance(v2, int) or isinstance(v2, float):
            for i in range(len(self.values)):
                self.values[i] *= float(v2)

    def __rmul__(self, nb):
        self.__mul__(self, nb)

    def __str__(self):
        text = ""
        text += str(self.values)
        return text

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __truediv__(self, v2):
        if isinstance(v2, Vector) and len(v2.values) == len(self.values):
            for i in range(len(self.values)):
                if not v2.values[i] == 0:
                    self.values[i] /= v2.values[i]
        elif isinstance(v2, int) or isinstance(v2, float) and v2 != 0:
            for i in range(len(self.values)):
                self.values[i] /= v2

    def __rtruediv__(self, nb):
        self.__div__(nb)
