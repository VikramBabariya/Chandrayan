class SpaceCraft:
    def __init__(self, x, y, z, face_dir):
        self.x = x
        self.y = y
        self.z = z
        self.face_dir = face_dir

    def __str__(self):
        return "Final Position: ({}, {}, {})\nFinal Direction: {}".format(self.x, self.y, self.z, self.face_dir)
