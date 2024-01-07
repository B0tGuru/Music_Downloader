from youtubesearchpython import VideosSearch

def search_youtube(query):
    try:
        # Search YouTube using the user's query
        videos_search = VideosSearch(query, limit=1)

        # Get the search results
        results = videos_search.result()['result']
        print(results)
        # Process and display the search results
        #for result in results:
            #video_title = result['title']
            #video_url = result['link']
            #print(f"Title: {video_title}")
            #print(f"URL: {video_url}")
            #print()
        return results[0]

    except Exception as e:
        print("An error occurred:")
        print(e)

#search_youtube("anti hero Audio")