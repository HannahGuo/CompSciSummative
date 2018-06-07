import pygame

pygame.init()
buttonFont = pygame.font.SysFont("comicsansms", 20)


class Button(object):
    def __init__(self, colour, hoverColour, display, text, top, left, width, height, textColour, offset, centerWidth, centerHeight):
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

        self.display.fill(colour, (self.top, self.left, self.width, self.height))
        self.displayText()

    def displayText(self):
        displayText = buttonFont.render(self.text, True, self.textColour)
        self.display.blit(displayText, [self.centerWidth - (displayText.get_rect().width / 2),
                                        self.centerHeight + (self.height / 2) - (displayText.get_rect().height / 2)
                                        + self.offset])

    def hover(self):
        self.display.fill(self.hoverColour, (self.top, self.left, self.width, self.height))
        self.displayText()
