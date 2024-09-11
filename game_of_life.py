import pygame
import random
display_width = 1280
display_height = 720

game_size_row = 100
game_size_col = 100

cell_size = 5
def randomize_initial_generation():
    initial_generation = [[random.randint(0, 1) for x in range(game_size_row)] for y in range(game_size_col)] 
    print(initial_generation)
    return initial_generation

def simulate_next_generation(generation):
    new_generation = [[random.randint(0, 1) for x in range(game_size_row)] for y in range(game_size_col)] 
    for i in range(len(generation)):
        for j in range(len(generation[0])):
            new_generation[i][j] = get_new_state(generation, i , j)
    return new_generation

def draw_cell(generation, screen,  row, col):
    w,h = screen.get_size()
    x = (cell_size+2)*col
    y = row * (cell_size + 2)
    cell = pygame.Rect(x, y, cell_size, cell_size)
    if(generation[row][col] == 0):
        pygame.draw.rect(screen, pygame.Color("red"), cell)
    if(generation[row][col] == 1):
        pygame.draw.rect(screen, pygame.Color("green"), cell)

def display_generation(generation, screen):
    screen.fill(pygame.Color("black"))
    for i in range(len(generation)):
        for j in range(len(generation[0])):
            draw_cell(generation, screen, i , j)

def get_new_state(generation, row, col):
    alive_count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if generation[(row + i)%game_size_row][(col + j)%game_size_col] == 1:
                alive_count +=1
    if generation[row][col] == 1 and (alive_count < 2 or alive_count > 3):
        return 0
    elif generation[row][col] == 0 and alive_count == 3:
        return 1
    else:
        return generation[row][col]

def main():
    pygame.init()
    screen = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Conway\' Game of Life')
    generation = randomize_initial_generation()
    animating = True
    while animating:
        generation = simulate_next_generation(generation)
        display_generation(generation, screen)
        pygame.display.flip()
        pygame.time.wait(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                animating = False

if __name__=="__main__":
    main()