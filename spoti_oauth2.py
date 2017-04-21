from requests_oauthlib import OAuth2Session
from urllib import quote_plus

client_id = "208dad78912a445e8efd1ed5ae97789a"
client_secret = "0146428a2ad94146836117920b941e26"
authorization_base_url = "https://accounts.spotify.com/authorize"
authorization_token_url = "https://accounts.spotify.com/api/token"
scope = ['playlist-read-private', 'playlist-modify-private', 'playlist-modify-public', 'playlist-modify-private', 'streaming', 'user-follow-modify', 'user-follow-read', 'user-library-read', 'user-library-modify', 'user-read-private']
redirect_uri = "https://localhost:8888/"

spotify = OAuth2Session(client_id=client_id, scope=scope, redirect_uri=redirect_uri)

authorization_url, state = spotify.authorization_url(authorization_base_url)

print 'Please go here and authorize\n', authorization_url

redirect_response = raw_input('Paste the full redirect URL here:\n')
spotify.fetch_token(token_url=authorization_token_url, client_secret=client_secret, authorization_response=redirect_response)

def get_track_id(track_name, oauth_target):
    target_response = oauth_target.get('https://api.spotify.com/v1/search?q={0}&type=track'.format(quote_plus(track_name)))
    return target_response.json().items()[0][1]['items'][0]['id'];

