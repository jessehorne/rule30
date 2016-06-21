import pygame
import math

class Rule30:
    def __init__(self):
        # Pro-Tip: Keep self.width always double self.height
        self.width = 1401
        self.height = 700

        self.current_row = [x**0 if x == math.floor(self.width/2+1) else 0 for x in xrange(self.width)]
        self.current_row_num = 0

        self.new_row_skeleton = [x**0 if x == math.floor(self.width/2+1) else 0 for x in xrange(self.width)]

        self.pixel_color = (106,205,202)
        self.backg_color = (17,37,50)

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.screen.fill(self.backg_color)

        pygame.display.flip()

        pygame.display.set_caption("Rule 30")

    def init(self):
        # init pygame things
        self.running = True

        while self.running:
            for event in pygame.event.get():
                self.event(event)

            self.update()
            self.render()

        self.cleanup()

    def update(self):
        pass

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def render(self):
        self.current_row_num += 1

        if self.current_row_num < self.height-5:
            new_row = self.new_row_skeleton[::]

            # rule logic here
            for key, val in enumerate(self.current_row):
                if key < len(self.current_row)-2:
                    curr = [val, self.current_row[key+1], self.current_row[key+2]]

                    if curr == [1, 1, 1]:
                        new_row[key+1] = 0

                    if curr == [1, 1, 0]:
                        new_row[key+1] = 0

                    if curr == [1, 0, 1]:
                        new_row[key+1] = 0

                    if curr == [1, 0, 0]:
                        new_row[key+1] = 1

                    if curr == [0, 1, 1]:
                        new_row[key+1] = 1

                    if curr == [0, 1, 0]:
                        new_row[key+1] = 1

                    if curr == [0, 0, 1]:
                        new_row[key+1] = 1

                    if curr == [0, 0, 0]:
                        new_row[key+1] = 0
            # end rule logic

            self.current_row = new_row

            # draw current_row
            # self.screen.set_at((rand_x, rand_y), self.pixel_color)
            for key, val in enumerate(self.current_row):
                if val == 1:
                    self.screen.set_at((key, self.current_row_num+2), self.pixel_color)

            pygame.display.flip()

    def cleanup(self):
        pygame.quit()


if __name__ == "__main__":
    rule30 = Rule30()
    rule30.init()
