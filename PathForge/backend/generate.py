import numpy as np
from model import LevelEnv

def generate_level(width=10, height=10, steps=20):
    env = LevelEnv(width, height)
    state = env.reset()
    for _ in range(steps):
        action = env.action_space.sample()
        state, _, _, _ = env.step(action)
    return state

if __name__ == "__main__":
    lvl = generate_level()
    print(lvl)
