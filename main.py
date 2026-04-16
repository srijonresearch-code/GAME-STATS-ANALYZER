import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("game_stats.csv")
def show_line():
    print("-"*36,"\n")
print(f"\n--------GAME STATS ANALYZER--------\n")
while True:
    print(f"1.Enter Player Stats")
    print(f"2.Analyze Player Performance")
    print(f"3.Leaderboard")
    print(f"4.Show Charts")
    print(f"5.Update Player Stats")
    print(f"6.Delete Player Stats")
    print(f"6.Reset Program")
    print(f"7.Exit")
    try:
        option=int(input("Choose option: "))
    except ValueError:
        print("\nOption must be an integer. Please enter it correctly\n")
        continue
    show_line()
    if option==1:
        while True:
            name=input("Name: ")
            try:
                kills=int(input("Kills: "))
            except ValueError:
                print("\nKills must be an integer. Please enter player stats correctly")
                continue
            try:
                deaths=int(input("Deaths: "))
            except ValueError:
                print("\nDeaths must be an integer. Please enter player stats correctly")
                continue    
            try:
                wins=int(input("Wins: "))
            except ValueError:
                print("\nWins must be an integer. Please enter player stats correctly")
                continue
            try:
                match_played=int(input("Total Match Played: "))
            except ValueError:
                print("\nMatches must be an integer. Please enter player stats correctly")
                continue
            game_stats={"Name":name,"Deaths":deaths,"Wins":wins,"Mathch Played":match_played}
            df=pd.concat([df,pd.DataFrame([game_stats])],ignore_index=True)
            df.to_csv("game_stats.csv",index=True)
            print(df)
            break
        if option==2:
            pass
        else:
            print("Please enter option correctly!")
            continue
            
