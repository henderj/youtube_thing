import googleapiclient.discovery

def main():
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBMLJv9Ngonq0rYUoXepCACTeGJ1co5pXc"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=50,
        pageToken="CMgBEAA",
        playlistId="PLYOHQ3GXK5JIIYcSfxDzB8vJagRKAw8XN"
    )
    response = request.execute()

    print(response)


main()
