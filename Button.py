class Button(object):
    def __init__(self, colour, hoverColour, display, text, left, top, width, height, textColour, offset, centerWidth,
                 centerHeight, font):
        self.colour = colour
        self.hoverColour = hoverColour
        self.display = display
        self.text = text
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.textColour = textColour
        self.offset = offset
        self.centerWidth = centerWidth
        self.centerHeight = centerHeight
        self.font = font
        self.isShown = False

    def displayText(self):
        displayText = self.font.render(self.text, True, self.textColour)
        self.display.blit(displayText, [self.centerWidth - (displayText.get_rect().width / 2),
                                        self.centerHeight + (self.height / 2) - (displayText.get_rect().height / 2)
                                        + self.offset])

    def hover(self):
        self.display.fill(self.hoverColour, (self.left, self.top, self.width, self.height))
        self.displayText()

    def showButton(self):
        self.display.fill(self.colour, (self.left, self.top, self.width, self.height))
        self.displayText()
        self.isShown = True

    def isHovered(self, cursor):
        if self.left < cursor[0] < self.left + self.width and self.top < cursor[1] < self.top + self.height:
            self.hover()
            return True
