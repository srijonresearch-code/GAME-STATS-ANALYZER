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
        print("\nOption must be an integer. Please enter it correctly")
    show_line()
    if option==1:
        pass
