import os
def cls():  
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')