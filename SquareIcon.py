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

        self.display.fill(colour, (self.left, self.top, self.size, self.size))
        self.displayText()

    def hover(self):
        self.display.fill(self.hoverColour, (self.left, self.top, self.size, self.size))
        self.displayText()

    def displayText(self):
        displayText = self.font.render(self.text, True, self.textColour)
        self.display.blit(displayText, [self.left + (self.size / 2) - (displayText.get_rect().width / 2),
                                        self.top + (self.size / 2) - (displayText.get_rect().height / 2)])