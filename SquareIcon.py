# Hannah Guo and Manav Shardha
# June 18th 2018
# ICS3UR
# This class makes it easier to create and display square icons. This was used to create the red X button for the help
# menu and the pause button during the game loop. It's similar to the Button class, however the SquareIcon is simpler
# to use for icons anywhere on the screen.


class SquareIcon(object):
    def __init__(self, colour, hoverColour, display, text, left, top, size, textColour, font):
        self.colour = colour
        self.hoverColour = hoverColour
        self.display = display
        self.text = text
        self.top = top
        self.left = left
        self.size = size
        self.textColour = textColour
        self.font = font

    def showIcon(self):
        self.display.fill(self.colour, (self.left, self.top, self.size, self.size))
        self.displayText()

    def displayText(self):
        displayText = self.font.render(self.text, True, self.textColour)
        self.display.blit(displayText, [self.left + (self.size / 2) - (displayText.get_rect().width / 2),
                                        self.top + (self.size / 2) - (displayText.get_rect().height / 2)])

    def isHovered(self, cursor):
        if self.left < cursor[0] < self.left + self.size and self.top < cursor[1] < self.top + self.size:
            self.display.fill(self.hoverColour, (self.left, self.top, self.size, self.size))
            self.displayText()
            return True
