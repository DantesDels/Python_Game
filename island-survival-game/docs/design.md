# Design Document for Island Survival Game

## Overview
The Island Survival Game is a text-based survival game where players manage vital resources while stranded on an island. The game challenges players to make strategic decisions each day to maintain their hunger, thirst, and energy levels, ultimately aiming to survive for as long as possible.

## Architecture
The game is structured into several modules, each responsible for different aspects of the game:

- **Main Module (`src/__main__.py`)**: This is the entry point of the game. It initializes the game loop and handles user input to progress through the days.

- **Game Logic (`src/game.py`)**: Contains the core game logic, including the management of player actions, resource updates, and transitions between different game states.

- **Player Management (`src/player.py`)**: Defines the `Player` class, which tracks the player's vital resources (hunger, thirst, energy) and their current state in the game.

- **Actions (`src/actions.py`)**: Implements the various actions that players can take each day, such as fishing, searching for water, sleeping, and exploring.

- **Events (`src/events.py`)**: Manages random events that can occur during gameplay, such as rain, animal encounters, and resource discoveries.

- **User Interface (`src/ui.py`)**: Handles the console output, displaying the player's resource gauges and game messages.

- **Save and Load (`src/save.py`)**: Manages the saving and loading of game states, utilizing JSON files to store player progress.

- **Constants (`src/constants.py`)**: Defines critical values for hunger, thirst, and energy, as well as probabilities for various events.

- **Utilities (`src/utils.py`)**: Contains helper functions for tasks like random number generation and input validation.

## Game Flow
1. **Initialization**: The game starts by initializing the player and setting their initial resource levels.
2. **Daily Actions**: Each day, the player can choose one action to perform, which will affect their resource levels.
3. **Event Handling**: After the player's action, random events may occur, impacting the game state.
4. **Resource Management**: The game continuously updates the player's resource levels based on actions taken and events encountered.
5. **Game Over Conditions**: The game ends when the player’s resources reach critical levels or after a predetermined number of days.
6. **Saving and Loading**: Players can save their progress at any time and load it later to continue their adventure.

## Design Decisions
- **Text-Based Interface**: The game is designed as a console application to focus on gameplay mechanics and resource management without the complexity of graphical interfaces.
- **Random Events**: Incorporating random events adds unpredictability and enhances replayability, encouraging players to adapt their strategies.
- **Resource Management**: The core gameplay revolves around managing hunger, thirst, and energy, creating a tension that drives player decisions.
- **Modular Structure**: The code is organized into modules to promote maintainability and scalability, allowing for easy updates and feature additions in the future.

## Future Enhancements
- Implement additional difficulty levels that affect resource depletion rates.
- Expand the variety and complexity of random events.
- Introduce an inventory system for managing collected resources.

This design document outlines the foundational structure and thought process behind the Island Survival Game, providing a roadmap for development and future enhancements.