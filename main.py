import pandas as pd
import matplotlib.pyplot as plt
try:
    df=pd.read_csv("game_stats.csv")
except FileNotFoundError:
    df=pd.DataFrame(columns=["Name","Kills","Deaths","Wins","Matches Played"])
def show_line(dashes):
    print("-"*dashes,"\n")
print(f"\n--------GAME STATS ANALYZER--------\n")
while True:
    print(f"1.Enter Player Stats")
    print(f"2.Analyze Player Performance")
    print(f"3.Leaderboard")
    print(f"4.Show Charts")
    print(f"5.Update Player Stats")
    print(f"6.Delete Player Stats")
    print(f"7.Reset Program")
    print(f"8.Exit")
    try:
        option=int(input("Choose option: "))
    except ValueError:
        print("Option must be an integer. Please enter it correctly")
        show_line(len("Option must be an integer. Please enter it correctly"))
        continue
    if option==1:
        while True:
            name=input("Name: ")
            while True:
                try:
                    kills=int(input("Kills: "))
                    if kills>=0:
                        break
                    else:
                        print("Kills must be a positive integer. Please enter it correctly.")
                        show_line(len("Kills must be a positive integer. Please enter it correctly."))
                        continue
                except ValueError:
                    print("Kills must be a positive integer. Please enter it correctly.")
                    show_line(len("Kills must be a positive integer. Please enter it correctly."))
                    continue
            while True:
                try:
                    deaths=int(input("Deaths: "))
                    if deaths>=0:
                        break
                    else:
                        print("Deaths must be a positive integer. Please enter it correctly.")
                        show_line(len("Deaths must be a positive integer. Please enter it correctly."))
                        continue
                except ValueError:
                    print("Deaths must be a positive integer. Please enter it correctly.")
                    show_line(len("Deaths must be a positive integer. Please enter it correctly."))
                    continue    
            while True:
                try:
                    wins=int(input("Wins: "))
                    if wins>=0:
                        break
                    else:
                        print("Wins must be a positive integer. Please enter it correctly.")
                        show_line(len("Wins must be a positive integer. Please enter it correctly."))
                        continue
                except ValueError:
                    print("Wins must be a positive integer. Please enter it correctly.")
                    show_line(len("Wins must be a positive integer. Please enter it correctly."))
                    continue
            while True:
                try:
                    matches_played=int(input("Total Matches Played: "))
                    if matches_played>=0:
                        break
                    else:
                        print("Matches must be a positive integer. Please enter it correctly.")
                        show_line(len("Matches must be a positive integer. Please enter it correctly."))
                        continue
                except ValueError:
                    print("Matches must be a positive integer. Please enter it correctly.")
                    show_line(len("Matches must be a positive integer. Please enter it correctly."))
                    continue
            if matches_played==0 and kills!=0 and deaths!=0:
                print("kills and deaths can not be possible when any match is not played. Please enter player stats correctly!")
                show_line(len("kills and deaths can not be possible when any match is not played. Please enter player stats correctly!"))
                continue
            elif matches_played==0 and kills!=0:
                print("kills can not be possible when any match is not played. Please enter player stats correctly!")
                show_line(len("kills can not be possible when any match is not played. Please enter player stats correctly!"))
                continue
            elif matches_played==0 and deaths!=0:
                print("Deaths can not be possible when any match is not played. Please enter player stats correctly!")
                show_line(len("Deaths can not be possible when any match is not played. Please enter player stats correctly!"))
                continue
            elif matches_played<wins:
                print("The number of wins can not ne higher than the number of total matches played. Please enter player stats correctly!")
                show_line(len("The number of wins can not be higher than the number of total matches played. Please enter player stats correctly!"))
                continue
            else:
                game_stats={"Name":name,"Kills":kills,"Deaths":deaths,"Wins":wins,"Matches Played":matches_played}
                df=pd.concat([df,pd.DataFrame([game_stats])],ignore_index=True)
                df.to_csv("game_stats.csv",index=False)
                print("Player stats added successfully!")
                show_line(len("Player stats added successfully!"))
                break
    elif option==2:
        print(df)
        
    elif 0>=option or option>8:
        print("Please enter option correctly!")
        show_line(len("Please enter option correctly!"))
        continue
            
