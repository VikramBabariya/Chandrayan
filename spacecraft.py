class SpaceCraft:
    def __init__(self, x, y, z, face_dir):
        self.x = x
        self.y = y
        self.z = z
        self.face_dir = face_dir

    def move(self, f_or_b):
        if self.face_dir == "N":
            self.y += 1 if f_or_b == "f" else -1
        elif self.face_dir == "S":
            self.y += -1 if f_or_b == "f" else 1
        elif self.face_dir == "E":
            self.x += 1 if f_or_b == "f" else -1
        elif self.face_dir == "W":
            self.x += -1 if f_or_b == "f" else 1
        elif self.face_dir == "U":
            self.z += 1 if f_or_b == "f" else -1
        elif self.face_dir == "D":
            self.z += -1 if f_or_b == "f" else 1

    def __str__(self):
        return "Final Position: ({}, {}, {})\nFinal Direction: {}".format(self.x, self.y, self.z, self.face_dir)
