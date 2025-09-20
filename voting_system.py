# Basic Voting System in Python

# Dictionary to store votes
votes = {}

# Function to cast vote
def cast_vote():
    name = input("Enter candidate name to vote: ")
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
    print(f"✅ Vote casted for {name}\n")

# Function to view results
def view_results():
    if not votes:
        print("No votes casted yet.\n")
        return
    print("📊 Voting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    print()

# Function to find winner with proper tie handling
def view_winner():
    if not votes:
        print("No votes casted yet.\n")
        return
        
winners = []
for name, count in votes.items():
    if count == max_votes:
        winners.append(name)


    if len(winners) > 1:
        print(f"🤝 It's a tie between: {', '.join(winners)} with {max_votes} votes each\n")
    else:
        print(f"🏆 Winner: {winners[0]} with {max_votes} votes\n")

# Main menu
def main():
    while True:
        print("------ VOTING SYSTEM MENU ------")
        print("1. Cast Vote")
        print("2. View Results")
        print("3. View Winner")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            cast_vote()
        elif choice == "2":
            view_results()
        elif choice == "3":
            view_winner()
        elif choice == "4":
            print("👋 Exiting Voting System. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
