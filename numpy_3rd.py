import numpy as np

points = np.array([
    [10, 25, 30, 22, 12, 18, 26, 32, 24, 29],  
    [20, 15, 12, 28, 24, 26, 30, 18, 22, 25],  
    [35, 30, 32, 40, 28, 34, 29, 31, 26, 37],  
    [12, 18, 20, 15, 22, 14, 19, 21, 23, 17],  
    [28, 26, 27, 25, 30, 29, 35, 32, 31, 38]   
])

print("Average points per game:")
for i in range(5):
    avg = np.mean(points[i])
    print(round(avg, 1), end=" ")

total_points = []
for i in range(5):
    total = sum(points[i])
    total_points.append(total)

best_player = total_points.index(max(total_points)) + 1
worst_player = total_points.index(min(total_points)) + 1

print(f"\n\nBest-performing player: Player {best_player} (Total: {max(total_points)} points)")
print(f"Worst-performing player: Player {worst_player} (Total: {min(total_points)} points)")

print("\nGames with scores above 30:")
for i in range(5):
    games = []
    for j in range(10):
        if points[i][j] > 30:
            games.append(j + 1)  
    if len(games) > 0:
        print(f"Player {i + 1}: Games {games}")

player_data = list(enumerate(total_points, start=1))  
player_data.sort(key=lambda x: x[1], reverse=True)

print("\nSorted Players by Total Points:")
for rank, (player_id, score) in enumerate(player_data, start=1):
    print(f"{rank}. Player {player_id} - {score} points")