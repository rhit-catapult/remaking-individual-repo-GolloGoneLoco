import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # TODO 1: Create an image with the 2dogs.JPG image
    dogs_image = pygame.image.load("2dogs.jpg")
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dogs_image = pygame.transform.scale(dogs_image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    bottom_font = pygame.font.SysFont("Arial", 28)
    #                         |        |         ^sets a font size
    #                         |        ^name of font from library
    #                         ^searches comp for your font library

    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    bottom_caption = bottom_font.render("Two Dogs",True, BLACK)
    top_caption = bottom_font.render("MOVE", True, WHITE)

    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dogs_image, (0,0))

        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        cap_x = screen.get_width() / 2 - bottom_caption.get_width() / 2
        cap_y = screen.get_height() - 2 - bottom_caption.get_height()
        screen.blit(bottom_caption, (cap_x, cap_y))
        screen.blit(top_caption, (150,30))

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
