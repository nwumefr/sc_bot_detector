# driver.py

from detector import SoundCloudBotDetector
from constants import auth

def main():
    # Initialize SoundCloudBotDetector with authentication token
    bot_detector = SoundCloudBotDetector(auth_token=auth)
    
    # Step 1: Display all followers
    print("\n## USER FOLLOWERS ##")
    followers = bot_detector.get_followers()
    for follower in followers:
        print(f"Follower Permalink: {follower[0]}, ID: {follower[1]}")
    
    # Step 2: Display public tracks for the authenticated user
    print("\n## PUBLIC TRACKS ##")
    bot_detector.get_public_tracks(bot_detector.user_id)
    
    # Step 3: Display likes for each public track
    # Here we demonstrate with a sample track ID; replace `sample_track_id` with a real track ID for actual use.
    sample_track_id = 12345678  # Replace this with an actual track ID
    print(f"\n## LIKES FOR TRACK ID {sample_track_id} ##")
    bot_detector.get_track_likes(sample_track_id)
    
    # Step 4: Detect potential bots in followers
    print("\n## POSSIBLE BOTS IN FOLLOWING ##")
    possible_bots, timeouts = bot_detector.detect_bots()
    for bot in possible_bots:
        print(f"Bot Permalink: {bot[0]}, Active Duration (days): {bot[1]}")
    
    # Step 5: Print any timeouts
    if timeouts:
        print("\n## TIMEOUT CHECKPOINTS ##")
        for checkpoint in timeouts:
            print(f"Timeout at follower: {checkpoint}")

if __name__ == "__main__":
    main()
