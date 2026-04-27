# 🎮 Game Stats Analyzer

A command-line application to track, analyze, and visualize player game statistics. Built with Python, Pandas, NumPy, and Matplotlib.

---

## Features

- **Add Player Stats** — Enter player name, kills, deaths, wins, and matches played
- **Analyze Player Performance** — View K/D ratio, win rate, and average kills per player
- **Leaderboard** — Rank players by K/D ratio or win rate
- **Charts** — Visualize stats with bar charts (K/D, Win Rate, Kills vs Deaths, Wins vs Losses)
- **Update Player Stats** — Edit existing player data
- **Delete Player Stats** — Remove a player from the records
- **Reset Program** — Clear all data
- **Data Persistence** — All data is saved to a CSV file and loaded on startup

---

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

Install dependencies:
```
pip install pandas numpy matplotlib
```

---

## How to Run

```
python main.py
```

---

## Menu Options

| Option | Description |
|--------|-------------|
| 1 | Enter Player Stats |
| 2 | Analyze Player Performance |
| 3 | Leaderboard |
| 4 | Show Charts |
| 5 | Update Player Stats |
| 6 | Delete Player Stats |
| 7 | Reset Program |
| 8 | Exit |

---

## Stats Calculated

- **K/D Ratio** = Kills / Deaths
- **Win Rate** = Wins / Matches Played × 100%
- **Average Kills** = Kills / Matches Played

---

## Data Storage

Player data is automatically saved to `game_stats.csv` in the same directory as the program. The file is created automatically on first run.

---

## Project Structure

```
GAME-STATS-ANALYZER/
│
├── main.py           # Main program
└── game_stats.csv    # Auto-generated data file
```

---

## Author

Srijon Das
