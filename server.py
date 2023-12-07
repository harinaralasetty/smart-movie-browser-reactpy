import reactpy
from components.Header import Header
from components.Body import Body 
from apis.movie_api import search_movies, fetch_movies 

reactpy.config.REACTPY_DEBUG_MODE.current = True

async def fetch_and_set_movies(search_term, setSearchResults):
    try:
        if search_term.strip() == '':
            print("hit here")
            movies = await fetch_movies()
            setSearchResults(movies)
        else:
            search_movies_result = await search_movies(search_term)
            setSearchResults(search_movies_result)
    except Exception as error:
        print("Something failed:", error)

@reactpy.component
def App():
    searchResults, setSearchResults = reactpy.use_state([])
    searchTerm, setSearchTerm = reactpy.use_state('')

    # useEffect equivalent to fetch and set movies on component mount
    async def effect():
        await fetch_and_set_movies(searchTerm, setSearchResults)

    reactpy.use_effect(effect, [searchTerm])

    return reactpy.html.div(
        {"className": "App"},
        Header(searchTerm=searchTerm, setSearchTerm=setSearchTerm),
        Body(searchResults=searchResults)
    )

if __name__ == '__main__':
    reactpy.run(App)
