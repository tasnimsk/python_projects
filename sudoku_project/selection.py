
class SelectNumber:
    def __init__(self, pygame, font):
        self.pygame = pygame
        self.btnW = 60 # button width
        self.btnH = 60 # button height
        self.myFont = font

        self.colorBtn = (200,200,200)
        self.colorSelected = (0, 255, 0)

        self.colorDisabled = (99,52,71)
        self.grid = None

        self.selectedNum = 0

        self.btnPositions = [(850,30), (940, 30), #horizontal diff: 90pxl
                             (850, 110), (940, 110), #vertical diff: 80pxl
                             (850, 190), (940, 190), 
                             (850,270), (940, 270), 
                             (940, 350)]
        
    def setGridReference(self, grid):
        self.grid = grid

    def draw(self, pygame, surface):
        for index, pos in enumerate(self.btnPositions):
            number = index + 1
            isDisabled = False
            
            #checks if within the grid and the there's the nine values initialized
            if self.grid and self.grid.correctCounts.get(number, 0) == 9:
                isDisabled = True
                btnColor = self.colorDisabled
                textColor = self.colorDisabled
                pygame.draw.rect(surface, self.colorDisabled, [pos[0], pos[1], self.btnW, self.btnH], width=3, border_radius=10)

            else:
                btnColor = self.colorBtn
                textColor = (200,200,200)
                pygame.draw.rect(surface, self.colorBtn, [pos[0], pos[1], self.btnW, self.btnH], width=3, border_radius=10)

            #checking if mouse is hovering
            if not isDisabled and self.btnHover(pos):
                pygame.draw.rect(surface, self.colorSelected, [pos[0], pos[1], self.btnW, self.btnH], width=3, border_radius= 10)
                textSurface = self.myFont.render(str(index+1), False, (0,255,0))

            if not isDisabled and self.selectedNum > 0:
                if self.selectedNum - 1 == index:
                    pygame.draw.rect(surface, self.colorSelected, [pos[0], pos[1], self.btnW, self.btnH], width=3, border_radius= 10)
                    textSurface = self.myFont.render(str(index+1), False, self.colorSelected)
            
            textSurface = self.myFont.render(str(index+1), False, self.colorBtn)
            surface.blit(textSurface, (pos[0]+26, pos[1]))
    
    def btnClicked(self, mouseX: int, mouseY:int) -> None:
        for index, pos in enumerate(self.btnPositions):
            number = index + 1
            #only allow selection if number isnt disabled
            if self.onBtn(mouseX, mouseY, pos) and self.grid and self.grid.numberCounts.get(number, 0) < 9:
                self.selectedNum = number

    def btnHover(self, pos:tuple) -> bool:
        mousePos = self.pygame.mouse.get_pos()
        if(self.onBtn(mousePos[0], mousePos[1], pos)):
            return True
        return False

    def onBtn(self, mouseX: int, mouseY: int, pos: tuple) -> bool:
        return pos[0] < mouseX < pos[0] + self.btnW and pos[1] < mouseY < pos[1] + self.btnH
