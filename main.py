import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
try:
    df=pd.read_csv("game_stats.csv")
except FileNotFoundError:
    df=pd.DataFrame(columns=["Name","Kills","Deaths","Wins","Matches Played"])

#K/D Ratio = kills / deaths
def calculate_kd_ratio(kills,deaths):
    if kills==0 and deaths==0:
        kd_ratio=0
    elif deaths==0:
        kd_ratio=kills
    else:
        kd_ratio=kills/deaths
    return kd_ratio    

#Win Rate = wins / matches
def calculate_win_rate(wins,matches):
    if matches==0:
        win_rate=0.00
    else:
        win_rate=wins/matches
    return win_rate
    
#Avg Kills = kills / matches
def calculate_average_kills(kills,matches):
    if matches==0:
        average_kills=0
    else:
        average_kills=kills/matches
    return average_kills
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
                    print("Wins must be an integer. Please enter it correctly.")
                    show_line(len("Wins must be an integer. Please enter it correctly."))
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
            if matches_played==0 and (kills!=0 or wins!=0 or deaths!=0):
                print("kills, deaths or wins can not be possible when any match is not played. Please enter player stats correctly!")
                show_line(len("kills, deaths or wins can not be possible when any match is not played. Please enter player stats correctly!"))
                continue
            elif matches_played<wins:
                print("The number of wins can not be higher than the number of total matches played. Please enter player stats correctly!")
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
        if df.empty:
            print("No player data available.")
            show_line(len("No player data available."))
            continue
        print(df)
        show_line(len("     Name  Kills  Deaths  Wins  Matches Played  "))
        while True:
            try:
                index=int(input("Enter index to analyze player stats or enter (-1) to return to the Main menu: "))
                show_line(len("Enter index to analyze player stats or enter (-1) to return to the Main menu:   "))
            except ValueError:
                print("Index must be an integer. Please enter it correctly!")
                show_line(len("Index must be an integer. Please enter it correctly!"))
                continue
            if index>=0 and index<len(df.index):
               print(f"Name: {df['Name'][index]}")
               print(f"K/D Ratio: {calculate_kd_ratio(df['Kills'][index],df['Deaths'][index]):.2f}")
               print(f"Win Rate: {calculate_win_rate(df['Wins'][index],df['Matches Played'][index])*100:.2f}%")
               print(f"Average Kills: {calculate_average_kills(df['Kills'][index],df['Matches Played'][index]):.2f}")
               show_line(len("Average Kills:      "))
            elif index!=-1:
                print(f"Check the list carefully and enter index between {0} and {len(df.index)-1}.")
                show_line(len(f"Check the list carefully and enter index between {0} and {len(df.index)-1}."))
                continue 
            elif index==-1:
                break
            continue
    elif option==3:
        while True:    
            print(f"1. Rank by K/D")
            print(f"2. Rank by Win Rate")
            try:
                option=int(input("Enter option or enter (-1) to return to the Main menu:"))
            except ValueError:
                print(f"Option must be an integer. Please enter it correctly")
                show_line(len("Option must be an integer. Please enter it correctly"))
                continue
            if df.empty:
                print("No player data available.")
                show_line(len("No player data available."))
                break
            if option==1:
                print("\n---------Leaderboard---------\n")
                index=0
                rank_kd={df["Name"][index]:calculate_kd_ratio(df["Kills"][index],df["Deaths"][index])}
                while len(df.index)-1>index>=0:
                    rank_kd.update({df["Name"][index+1]:calculate_kd_ratio(df["Kills"][index+1],df["Deaths"][index+1])})
                    index+=1
                index=1
                sorted_rank_kd=dict(sorted(rank_kd.items(), key=lambda item:item[1], reverse=True))
                print("-"*29)
                print(f"|{' ':3}{'Name':12}{'|':6}{'K/D':6}|")
                print("-"*29)
                for name,kd in sorted_rank_kd.items():
                    print(f"|{index:2}.{name:12}{'|':6}{kd:.2f}{' ':2}|")
                    print("-"*29)
                    index+=1
                print("\n")
            elif option==2:
                print("\n----------Leaderboard----------\n")
                index=0
                rank_win_rate={df["Name"][index]:calculate_win_rate(df["Wins"][index],df["Matches Played"][index])}
                while len(df.index)-1>index>=0:
                    rank_win_rate.update({df["Name"][index+1]:calculate_win_rate(df["Wins"][index+1],df["Matches Played"][index+1])})
                    index+=1
                index=1
                sorted_rank_win_rate=dict(sorted(rank_win_rate.items(),key=lambda item:item[1],reverse=True))
                print("-"*31)
                print(f"|{' ':3}{'Name':12}{'|':6}{'Win Rate':6}|")
                print("-"*31)
                for name,win_rate in sorted_rank_win_rate.items():
                    print(f"|{index:2}.{name:12}{'|':6}{win_rate:.2f}%{' ':3}|")
                    print("-"*31)
                    index+=1
                print("\n")
            elif option==-1:
                print('\n')
                break
            else:
                print("\nPlease enter option correctly!")
                show_line(len("Please enter option correctly!"))
                continue
    elif option==4:
        if df.empty:
                print("No player data available.")
                show_line(len("No player data available."))
                continue
        print(f"1. K/D Ratio Chart")
        print(f"2. Win Rate Chart")
        print(f"3. Kills vs Deaths Chart")
        print(f"4. Wins vs Losses Chart")
        while True:
            try:
                option=int(input("Enter option or enter (-1) to return to the Main menu:"))
            except ValueError:
                print(f"Option must be an integer. Please enter it correctly")
                show_line(len("Option must be an integer. Please enter it correctly"))
                continue
            if option==-1:
                print('\n')
                break
            elif option==1:
                pass
            #start from here
            elif option==3: 
                x = np.arange(len(df.index))
                plt.bar(x-0.1, df["Kills"], 0.2, label="Kills")
                plt.bar(x+0.1, df["Deaths"], 0.2, label="Deaths")
                plt.xticks(x, df["Name"])
                plt.title("Kills vs Deaths Chart")
                plt.xlabel("Names")
                plt.ylabel("Kills,Deaths")
                plt.legend()
                plt.xticks(rotation=45, ha="right")
                plt.show()
            elif option==4:
                x=np.arange(len(df.index))
                plt.bar(x-0.1, df["Wins"], 0.2, label="Wins")
                losses=df["Matches Played"]-df["Wins"]
                plt.bar(x+0.1,losses,0.2,label="losses")
                plt.xticks(x,df["Name"])
                plt.title("Wins vs Losses Chart")
                plt.xlabel("Name")
                plt.ylabel("Wins,Losses")
                plt.xticks(rotation=45,ha="right")
                plt.legend()
                plt.show()
            else:
                print("\nPlease enter option correctly!")
                show_line(len("Please enter option correctly!"))
                continue
    elif option==5:
        if df.empty:
                print("No player data available.")
                show_line(len("No player data available."))
                continue
        print(df)
        show_line(len("     Name  Kills  Deaths  Wins  Matches Played  "))
        while True:
            try:
                index=int(input("Enter index to update player stats or enter (-1) to return to the Main menu: "))
                show_line(len("Enter index to update player stats or enter (-1) to return to the Main menu:   "))
            except ValueError:
                print("Index must be an integer. Please enter it correctly!")
                show_line(len("Index must be an integer. Please enter it correctly!"))
                continue
            if index==-1:
                print("\n")
                break
            elif len(df.index)>index>=0:
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
                            print("Wins must be an integer. Please enter it correctly.")
                            show_line(len("Wins must be an integer. Please enter it correctly."))
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
                    if matches_played==0 and (kills!=0 or wins!=0 or deaths!=0):
                        print("kills, deaths or wins can not be possible when any match is not played. Please enter player stats correctly!")
                        show_line(len("kills, deaths or wins can not be possible when any match is not played. Please enter player stats correctly!"))
                        continue
                    elif matches_played<wins:
                        print("The number of wins can not be higher than the number of total matches played. Please enter player stats correctly!")
                        show_line(len("The number of wins can not be higher than the number of total matches played. Please enter player stats correctly!"))
                        continue
                    else:
                        df.loc[index,'Name']=name
                        df.loc[index,'Kills']=kills
                        df.loc[index,'Deaths']=deaths
                        df.loc[index,'Wins']=wins
                        df.loc[index,'Matches Played']=matches_played
                        df.to_csv("game_stats.csv",index=False)
                        print("Player stats updated successfully!")
                        show_line(len("Player stats updated successfully!"))
                        break
            else:
                print("\nPlease enter index correctly!")
                show_line(len("Please enter index correctly!"))
                continue
    elif option==6:
        if df.empty:
                print("No player data available.")
                show_line(len("No player data available."))
                continue
        print(df)
        show_line(len("     Name  Kills  Deaths  Wins  Matches Played  "))
        while True:
            try:
                index=int(input("Enter index to update player stats or enter (-1) to return to the Main menu: "))
                show_line(len("Enter index to update player stats or enter (-1) to return to the Main menu:   "))
            except ValueError:
                print("Index must be an integer. Please enter it correctly!")
                show_line(len("Index must be an integer. Please enter it correctly!"))
                continue
            if len(df.index)>index>=0:
                df=df.drop(index=index).reset_index(drop=True)
                df.to_csv("game_stats.csv",index=False)
                break
            elif index==-1:
                print("\n")
                break
            else:
                print("\nPlease enter index correctly!")
                show_line(len("Please enter index correctly!"))
                continue
    elif option==7:
        df=pd.DataFrame(columns=["Name","Kills","Deaths","Wins","Matches Played"])
        df.to_csv("game_stats.csv",index=False)
        print("Program reset successfully!")
        show_line(len("Program reset successfully!"))    
    elif option==8:
        print("\nProgram exited successfully!")
        show_line(len("Program exited successfully!"))
        break
    elif 0>=option or option>8:
        print("Please enter option correctly!")
        show_line(len("Please enter option correctly!"))
            
