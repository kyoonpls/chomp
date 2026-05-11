import pygame


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 900)) #Sets the size f the display in terms of number of pixels. Width, then height.
        self.clock = pygame.time.Clock() #Starts the gameclock, which sets the speed of the game.
        self.running = True #A variable we can use a switch to shut the game off if we need to.
        self.numRows = 18
        self.numCols = 9
        self.map = []
        for row in range(self.numRows):
            someRow = []
            for col in range(self.numCols):
                someRow.append(False)
            self.map.append(someRow)


    def main(self):
        while self.running: #Infinite loop. We will do these things over and over on repeat until our self.running variable gets set to False.
            self.events() #Check for any new events we need to act on
            self.update() #Update all of the things that move/change
            self.draw() #Redraw the screen, since things may have moved/changed.
            self.clock.tick(60) #60FPS. This just tells python to wait. The game is only allowed to execute this line 60 times per second.
            
    def events(self): #When called, Game checks if any input (clicking the x button, hitting a specific key, etc) needs acting on, and acts on it.
        for event in pygame.event.get(): #For each event pygame has as occuring...
            if event.type == pygame.QUIT: #If that event is the type of event that comes when the user hits the x button....
                self.running=False #Flips our switch to stop running the game. This closes the game, and the window.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    row = event.pos[0] / 900    
                    col = event.pos[1] / 900
                    print(row, col)
                    self.map[row][col] = True 

    def update(self):
        pass

    def draw(self): #A method Games can do. It draws everything that should be on the screen to the screen, then updates the screen.
        self.screen.fill((0, 0, 0)) #black out the screen. This removes the last drawing we made, so we start with a fresh black canvas.
        for row in range(self.numRows):
            for col in range(self.numCols):
                if map[row][col] == False:
                    pygame.draw.rect(self.screen, (62, 200, 105), pygame.Rect(row * 900/self.numRows, col * 900/self.numCols, (900/self.numRows) -1, (900/self.numCols) -1 ))
                else:
                    pygame.draw.rect(self.screen, (120, 220, 34), pygame.Rect(row * 900/self.numRows, col * 900/self.numCols, (900/self.numRows) -1, (900/self.numCols) -1 ))



        pygame.display.update()

#This is the code that gets executed when we tell python to run this file.
pygame.init() #Helps pygame start up, and sets up things like fonts
game = Game() #First, we make a Game object, calling its constructor. We save it to a variable so can access it later.
#game.create() #We point to our game object and tell it to execute its create method. This builds the initial world and sets things up.
game.main() #We point to our game objecvt and tell it to execute its main method. This method contains an infinite loop and will continue to run while they are playing.
pygame.quit() #We can only make it to here if the infinite loop from main ended, which means we want to stop playing the game, so we quit.
