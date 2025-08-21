import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle

# If modifying these scopes, delete the token.pickle file
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly',
          'https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate_youtube():
    """
    Authenticate with YouTube API using OAuth 2.0
    Returns authenticated YouTube service object
    """
    creds = None
    
    # Token file stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no valid credentials, prompt user to authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # TODO: Replace 'credentials.json' with your actual credentials file path
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # Use a specific port and redirect URI
            creds = flow.run_local_server(port=8080)
        
        # Save credentials for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    # Build the YouTube service object
    youtube = build('youtube', 'v3', credentials=creds)
    return youtube

def get_channel_info(youtube):
    """
    Get basic information about the authenticated user's YouTube channel
    """
    try:
        # Get channel information
        request = youtube.channels().list(
            part='snippet,statistics,contentDetails',
            mine=True
        )
        response = request.execute()
        
        if response['items']:
            channel = response['items'][0]
            
            print("=== CHANNEL INFORMATION ===")
            print(f"Channel Title: {channel['snippet']['title']}")
            print(f"Channel ID: {channel['id']}")
            print(f"Description: {channel['snippet']['description'][:200]}...")
            print(f"Published At: {channel['snippet']['publishedAt']}")
            print(f"Country: {channel['snippet'].get('country', 'Not specified')}")
            
            # Statistics
            stats = channel['statistics']
            print(f"\n=== STATISTICS ===")
            print(f"View Count: {stats.get('viewCount', 'N/A')}")
            print(f"Subscriber Count: {stats.get('subscriberCount', 'Hidden')}")
            print(f"Video Count: {stats.get('videoCount', 'N/A')}")
            
            return channel['id']
        else:
            print("No channel found for this account")
            return None
            
    except Exception as e:
        print(f"Error getting channel info: {e}")
        return None

def like_video(youtube, video_id):
    """
    Like a specific video by its ID
    
    Args:
        youtube: Authenticated YouTube service object
        video_id (str): The YouTube video ID to like
    """
    try:
        # Like the video
        request = youtube.videos().rate(
            id=video_id,
            rating='like'
        )
        response = request.execute()
        
        print(f"Successfully liked video with ID: {video_id}")
        
        # Get video details to confirm
        video_request = youtube.videos().list(
            part='snippet',
            id=video_id
        )
        video_response = video_request.execute()
        
        if video_response['items']:
            video_title = video_response['items'][0]['snippet']['title']
            print(f"Video title: {video_title}")
        
    except Exception as e:
        print(f"Error liking video: {e}")

def get_liked_videos(youtube, max_results=10):
    """
    Get a list of recently liked videos (optional feature)
    
    Args:
        youtube: Authenticated YouTube service object
        max_results (int): Maximum number of results to return
    """
    try:
        request = youtube.videos().list(
            part='snippet',
            myRating='like',
            maxResults=max_results
        )
        response = request.execute()
        
        print(f"\n=== YOUR RECENTLY LIKED VIDEOS (Last {max_results}) ===")
        for item in response['items']:
            print(f"- {item['snippet']['title']}")
            print(f"  Video ID: {item['id']}")
            print(f"  Published: {item['snippet']['publishedAt']}")
            print()
            
    except Exception as e:
        print(f"Error getting liked videos: {e}")

def main():
    """
    Main function to execute the YouTube API operations
    """
    print("YouTube Data API Script")
    print("========================")
    
    # Authenticate with YouTube
    print("Authenticating with YouTube...")
    youtube = authenticate_youtube()
    
    if youtube:
        print("Authentication successful!\n")
        
        # Get channel information
        channel_id = get_channel_info(youtube)
        
        if channel_id:
            video_id_to_like = "VDbDH_ltCK0"  # Replace with actual video ID
            print(f"\nLiking video: {video_id_to_like}")
            like_video(youtube, video_id_to_like)

            # Optional: Show recently liked videos
            get_liked_videos(youtube, 5)
            
    else:
        print("Authentication failed!")

if __name__ == "__main__":
    # TODO: Install required packages first:
    # pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
    
    main()