from math import cos, pi


class Animation(object):
    def __init__(self):
        self.start = None
        self.dif = None
        self.steps = None
        self.cur_step = 0

        self.state = False

    def animate(self, start: int, end: int, steps: int):
        self.start = start
        self.dif = end-start
        self.steps = steps
        self.cur_step = 0

        self.state = True

    def step(self) -> float:
        assert self.dif is not None and self.steps is not None, "You have no animation running"
        ret = self.start + cos((self.cur_step/self.steps)*pi+pi)*(self.dif/2)+(self.dif/2)
        self.cur_step += 1

        if self.cur_step > self.steps:
            self.state = False
            self.reset()

        return ret

    def reset(self):
        self.start = None
        self.dif = None
        self.steps = None
        self.cur_step = 0
