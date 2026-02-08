import re
from urllib.parse import urlparse

class LinkHandler:
    def __init__(self):
        # Regex to capture spotify track ID
        # Supports: 
        # https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC
        # spotify:track:4uLU6hMCjMI75M1A2tKUQC
        self.track_pattern = re.compile(r'(?:open\.spotify\.com\/track\/|spotify:track:)([a-zA-Z0-9]+)')

    def extract_track_id(self, input_string):
        """
        Validates the input string and extracts the Spotify Track ID.
        Returns the Track ID (str) or None if invalid.
        """
        if not input_string:
            return None

        match = self.track_pattern.search(input_string)
        if match:
            return match.group(1)
        
        return None

    def validate_link(self, input_string):
        """
        Simple boolean validation
        """
        return self.extract_track_id(input_string) is not None
