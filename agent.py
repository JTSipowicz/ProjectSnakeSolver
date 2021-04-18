import torch
import random
import numpy as np 
from collections import deque
from scoreboard import Scoreboard
from data_structures import Point
from model import Linear_QNet, QTrainer
from helper import plot
from game import Game

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent():
    def __init__(self):
        self.num_games = 0
        self.epsilon = 0    # Control randomness
        self.gamma = 0.9  # Discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # Pop at max
        self.model = Linear_QNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
        

    def get_state(self, game):
        head = game.get_snake_head()
        snake_len = game.get__snake_length()
        snake_dir = game.get_snake_direction()
        food_coor = game.get_food_coor()
        # Point coordinates are bottom left of rect
        point_r = Point(head.x + (snake_len * 2), head.y)
        point_u = Point(head.x, head.y - (snake_len * 2))
        point_l = Point(head.x - snake_len, head.y)
        point_d = Point(head.x, head.y + snake_len)

        dir_r = snake_dir == 'RIGHT'
        dir_u = snake_dir == 'UP'
        dir_l = snake_dir == 'LEFT'
        dir_d = snake_dir == 'DOWN'

        state = [
            # Danger in straight direction
            (dir_r and game.is_Collision(point_r)) or
            (dir_u and game.is_Collision(point_u)) or
            (dir_l and game.is_Collision(point_l)) or
            (dir_d and game.is_Collision(point_d)),

            # Danger right
            (dir_r and game.is_Collision(point_u)) or
            (dir_u and game.is_Collision(point_r)) or
            (dir_l and game.is_Collision(point_u)) or
            (dir_d and game.is_Collision(point_l)),

            # Danger left
            (dir_r and game.is_Collision(point_u)) or
            (dir_u and game.is_Collision(point_l)) or
            (dir_l and game.is_Collision(point_d)) or
            (dir_d and game.is_Collision(point_r)),

            # Direction
            dir_r,
            dir_u,
            dir_l,
            dir_d,

            # self.food Location
            food_coor.x < head.x,     # self.food to the left
            food_coor.x > head.x,     # self.food to the right
            food_coor.y < head.y,     # self.food above
            food_coor.y > head.y      # self.food below
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, game_over):
        self.memory.append((state, action, reward, next_state, game_over)) # Deque, one tuple

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)    # List of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, game_overs = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, game_overs)

    def train_short_memory(self, state, action, reward, next_state, game_over):
        self.trainer.train_step(state, action, reward, next_state, game_over) 

    def get_action(self, state):
        # Random moves: exploration
        self.epsilon = 80 - self.num_games
        final_move = [0, 0, 0]
        if(random.randint(0, 200)) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move
    
    def train(self, scoreboard):
        plot_scores = []
        plot_mean_scores = []
        total_score = 0
        record = 0
        game = Game(fps=30, scoreboard=scoreboard, mode='AI') 
        while True:
            old_state = self.get_state(game)
            final_move = self.get_action(old_state)
            reward, game_over, score = game.game_loop(action=final_move) 
            new_state = self.get_state(game)

            self.train_short_memory(old_state, final_move, reward, new_state, game_over)
            self.remember(old_state, final_move, reward, new_state, game_over)

            if game_over:
                # Long memory
                game.reset()
                self.num_games += 1
                self.train_long_memory()

                if score > record:
                    record = score
                    self.model.save()
                
                print('Game: ', self.num_games, 'Score: ', score, 'Record: ', record)

    def plot():
        plot_scores.append(score)
        total_score += score
        mean_scores = total_score / self.num_games
        plot_mean_scores.append(mean_scores)
        plot(plot_scores, plot_mean_scores)
                


