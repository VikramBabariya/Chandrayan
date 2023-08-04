class SpaceCraft:
    def __init__(self, x, y, z, face_dir):
        self.x = x
        self.y = y
        self.z = z
        self.face_dir = face_dir

    def move(self, cmd):
        if self.face_dir == "N":
            self.y += 1 if cmd == "f" else -1
        elif self.face_dir == "S":
            self.y += -1 if cmd == "f" else 1
        elif self.face_dir == "E":
            self.x += 1 if cmd == "f" else -1
        elif self.face_dir == "W":
            self.x += -1 if cmd == "f" else 1
        elif self.face_dir == "U":
            self.z += 1 if cmd == "f" else -1
        elif self.face_dir == "D":
            self.z += -1 if cmd == "f" else 1

    def turn(self, cmd):
        if self.face_dir == "N":
            self.face_dir = "W" if cmd == "l" else ("E" if cmd == "r" else ("U" if cmd == "u" else "D"))
        elif self.face_dir == "S":
            self.face_dir = "E" if cmd == "l" else ("W" if cmd == "r" else ("U" if cmd == "u" else "D"))
        elif self.face_dir == "E":
            self.face_dir = "N" if cmd == "l" else ("S" if cmd == "r" else ("U" if cmd == "u" else "D"))
        elif self.face_dir == "W":
            self.face_dir = "S" if cmd == "l" else ("N" if cmd == "r" else ("U" if cmd == "u" else "D"))
        elif self.face_dir == "U":
            self.face_dir = "W" if cmd == "l" else ("E" if cmd == "r" else ("S" if cmd == "u" else "N"))
        elif self.face_dir == "D":
            self.face_dir = "E" if cmd == "l" else ("W" if cmd == "r" else ("N" if cmd == "u" else "S"))

    def run_spacecraft(self, cmds):
        for cmd in cmds:
            if cmd == "f" or cmd == "b":
                self.move(cmd)
            else:
                self.turn(cmd)

    def __str__(self):
        return "Final Position: ({}, {}, {})\nFinal Direction: {}".format(self.x, self.y, self.z, self.face_dir)
