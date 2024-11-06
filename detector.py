# detector.py

from soundcloud import SoundCloud
from constants import auth, whitelist
import time

class SoundCloudBotDetector:
    def __init__(self, auth_token):
        # Initialize SoundCloud client with authentication
        self.client = SoundCloud(auth_token=auth_token)
        self.user = self.client.get_me()
        self.user_id = self.user.id

        # Print user info upon initialization
        print("## USER INFO ##")
        print(self.user_id, self.user.permalink)

    def get_followers(self):
        # Retrieves a list of tuples with follower permalink and ID
        return [(follower.permalink, follower.id) for follower in self.client.get_user_followers(self.user_id)]

    def get_public_tracks(self, user_id):
        # Retrieves and prints public tracks of a given user
        for track in self.client.get_user_tracks(user_id):
            print(track.id, track.title)

    def get_track_likes(self, track_id):
        # Lists users who liked a specific track
        for liker in self.client.get_track_likers(track_id):
            print(liker.id, liker.permalink)

    def detect_bots(self):
        # Identifies potential bot accounts in followers list
        flagged = []
        timeout_checkpoints = []
        
        for follower in self.client.get_user_followers(self.user_id):
            timeout = time.time() + 5  # 5-second timeout for processing
            active_duration = (follower.last_modified - follower.created_at).days

            # Criteria for flagging potential bots
            if (active_duration < 4 or active_duration > 180) and (follower.followers_count < 20) and (follower.permalink not in whitelist):
                flagged.append((follower.permalink, active_duration))
            
            if time.time() > timeout:
                # Add follower to timeout checkpoints if the process takes too long
                timeout_checkpoints.append(follower.permalink)
                break
        
        return flagged, timeout_checkpoints

