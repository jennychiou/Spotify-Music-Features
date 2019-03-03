import spotipy
import spotipy.util as util

username = 'o7dgqfjas82wkfhhwljkw7w7b'
password = 'jenny850121'
scope = 'user-library-read'
client_id = '56585547a2104e1bac19f149e1e3db0f'
redirect_uri = 'http://localhost/'
client_secret = 'a13333899bd14cbc895eed52e9cf6484'

token = util.prompt_for_user_token(username=username, \
                scope=scope,  \
                client_id=client_id, \
                redirect_uri=redirect_uri, \
                client_secret=client_secret)
if token:
    
    # 歌單中的歌名以及歌手名稱(最愛的歌曲)
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print("最愛的歌曲：")
        print ('| * ' + track['name'] + ' | ' + track['artists'][0]['name'])

    # 取得使用者的playlists資訊
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists('JennyChiou')
    items = playlists['items'][0]
    print("\n播放清單：")
    print('| * Playlists link:', items['external_urls']['spotify'])
    print('| * Playlist ID:' ,items['id'])
    print('| * User :', items['name'])
    print('| * Owner :', items['owner']['display_name'])
    print('| * Profile Url:',  items['owner']['external_urls']['spotify'])
    print('| * Song Number:', items['tracks']['total'])
    print('| * Track:', items['tracks']['href'])
    # 取得該播放清單的歌曲的詳細資訊
##    results = sp.user_playlist("plusoneee", items['id'])
##    track = results['tracks']['items']
##    print('| | * Playlists Detail:')
##    for song in track[:]:
##        print('| | ')
##        print('| | * Artists Name: ', song['track']['artists'][0]['name'])
##        print('| | * Artists ID: ', song['track']['artists'][0]['id'])
##        print('| | * Album Name: ', song['track']['album']['name'])
##        print('| | * Album Release Date: ', song['track']['album']['release_date'])
