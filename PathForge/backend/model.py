import numpy as np
import gym
from gym import spaces

class LevelEnv(gym.Env):
    def __init__(self, width=10, height=10):
        self.width = width; self.height = height
        self.observation_space = spaces.Box(0,1,shape=(width,height), dtype=np.int8)
        self.action_space = spaces.Discrete(width*height)
        self.state = np.zeros((width,height), dtype=np.int8)
    def reset(self):
        self.state[:] = 0
        return self.state
    def step(self, action):
        x, y = divmod(action, self.height)
        self.state[x,y] = 1
        reward = 1.0  # placeholder
        return self.state, reward, False, {}
