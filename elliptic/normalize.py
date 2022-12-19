class elliptic:
    def __init__(self, a1, a3, a2, a4, a6):
        self.A = [0] * 7
        self.A[1] = a1
        self.A[3] = a3
        self.A[2] = a2
        self.A[4] = a4
        self.A[6] = a6