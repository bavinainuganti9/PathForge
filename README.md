# PathForge

## Overview / Description  
PathForge is an AI-powered game level generator that creates playable levels for platformer and puzzle games. It uses procedural generation combined with reinforcement learning techniques to design game maps dynamically. You can customize level size and difficulty and preview generated levels visually in game engines like Unity and Godot.

## Features  
- Procedural generation of game levels via a custom Gym environment  
- Reinforcement learning agent for AI-assisted level design  
- Visual previews of generated levels using Unity and Godot  
- Configurable parameters such as level width, height, and generation steps  
- Simple CLI interface for generating levels  

## Architecture  
- LevelEnv (Gym Environment): Simulates the game level grid as an RL environment with actions to place elements on the grid  
- RL Agent: Trains on LevelEnv to generate playable and interesting levels  
- Level Generator: Runs procedural or random generation using the environment API  
- Game Engine Integration: Exports levels to Unity and Godot for visualization and gameplay testing  

## Tech Stack  
- Python (Gym for environment, NumPy for data handling)  
- TensorFlow for reinforcement learning models  
- Unity and Godot for level visualization and game development  
- CLI tools for parameter configuration  
