import random
import time

# Starting player stats
player_hp = 100
total_gold = 0
rooms_cleared = 0

print("=" * 40)
print(" DUNGEON ESCAPE - TEXT ADVENTURE ")
print("=" * 40)
print("Explore mystery rooms and survive.")
print("Goal: Collect as much gold as you can!\n")

while True:
    # 1. Ask the player for an action
    action = input("Press ENTER to enter a new room (or q to quit): ").lower()
    
    # 2. Quit and escape safely
    if action == "q":
        print("\nYou safely escaped from the dungeon!")
        break
        
    print("\nThe door is slowly opening...")
    time.sleep(1)  # Wait 1 second for suspense
    
    # 3. Pick a random event (1: Treasure, 2: Monster, 3: Healing potion)
    event = random.randint(1, 3)
    
    if event == 1:
        # Found treasure
        found_gold = random.randint(20, 60)
        total_gold += found_gold
        print(f" Great! You found a treasure chest: +{found_gold} Gold!")
        
    elif event == 2:
        # Monster attack
        damage = random.randint(15, 35)
        player_hp -= damage
        print(f" Watch out! A monster attacked you for {damage} damage!")
        
    else:
        # Healing fountain
        heal = random.randint(10, 25)
        player_hp += heal
        print(f" You found a magic fountain: +{heal} HP restored!")
        
    # Increment room count
    rooms_cleared += 1
    
    # Display current status
    print(f"Status -> HP: {player_hp} | Total Gold: {total_gold}")
    print("-" * 35)
    
    # 4. Check if player has run out of health
    if player_hp <= 0:
        print("\n You lost all your HP! Game Over...")
        break

# Summary statistics after the loop ends
print("\n" + "=" * 40)
print(" GAME SUMMARY ")
print("=" * 40)
print(f"Rooms Cleared: {rooms_cleared}")
print(f"Total Gold Earned: {total_gold}")
if rooms_cleared > 0:
    avg_gold = total_gold / rooms_cleared
    print(f"Average Gold/Room: {avg_gold:.2f}")
print("Thank you for playing!")
