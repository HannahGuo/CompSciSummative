# Hannah Guo and Manav Shardha
# June 18th 2018
# ICS3UR
# This is a button class that allows us to easily create buttons for our menus. It includes a button initializer, and
# several control functions, such as changing colour when the button is hovered. The buttons are all created relative
# to the center of the screen.


class button(object):
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

    def displayText(self):
        displayText = self.font.render(self.text, True, self.textColour)
        self.display.blit(displayText, [self.centerWidth - (displayText.get_rect().width / 2),
                                        self.centerHeight + (self.height / 2) - (displayText.get_rect().height / 2)
                                        + self.offset])

    def showButton(self):
        self.display.fill(self.colour, (self.left, self.top, self.width, self.height))
        self.displayText()

    def isHovered(self, cursor):
        if self.left < cursor[0] < self.left + self.width and self.top < cursor[1] < self.top + self.height:
            self.display.fill(self.hoverColour, (self.left, self.top, self.width, self.height))
            self.displayText()
            return True
