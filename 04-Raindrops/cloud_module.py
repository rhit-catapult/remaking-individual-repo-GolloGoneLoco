class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []


    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        drop_x = random.randint(self.x, self.x + self.image.get_width())
        drop_y = self.y + self.image.get_height() - 5
        new_raindrop = Raindrop(self.screen, drop_x, drop_y)
        self.raindrops.append(new_raindrop)