import reactpy
from http import cookies

movie_images_path = r'https://image.tmdb.org/t/p/w500'

styles = {
    "recordList": {
        "margin_left": "2%",
        "margin_right": "2%",
        "margin_top": "2%",
        "display": "flex",
        "flex_wrap": "wrap",
        "justify_content": "space-around",
    },
    "record": {
        "display": "flex",
        "flex_direction": "column",
        "align_items": "center",
        "width": "150px",
        "height": "auto",
        "margin": "10px",
        "border_radius": "10px",
        "overflow": "hidden",
        "background_color": "rgb(211, 210, 210)",
        "transition": "transform 0.3s ease-in-out",
        "position": "relative",
        "z_index": "1",
    },
    "recordHover": {
        "transform": "scale(1.1)",
    },
    "likeButton": {
        "background": "none",
        "border": "none",
        "cursor": "pointer",
        "font_size": "15px",
        "transition": "color 0.3s ease-in-out",
        "position": "absolute",
        "bottom": "10px",
        "right": "1px",
        "margin": "5px",
        "color": "#bebdbd",
    },
    "liked": {
        "background_color": "#e2eefc",
    },
    "likeButtonLiked": {
        "color": "#ff0000",
    },
}

like_cookies = cookies.SimpleCookie()
def set_like_status_cookies(record, status): 
    like_cookies[str(record['id'])] = status
    print(f"Movie {record['original_title']} is {'liked' if like_cookies[str(record['id'])] else 'unliked'}")

def get_like_status_cookies(record):
    return like_cookies[str(record['id'])].value if str(record['id']) in like_cookies else False

@reactpy.component
def Body(searchResults):
    return reactpy.html.div(
        {},
        reactpy.html.div(
            {
                'style': styles["recordList"]
            },
            *[Record(rec) for rec in searchResults]
        )
    )

@reactpy.component
def Record(record):
    like_status, set_like_status = reactpy.hooks.use_state(get_like_status_cookies(record))

    # reactpy.hooks.use_effect(
    #     lambda: set_like_status_cookies(record, like_status),
    #     []
    # )

    def handleLikeClick():
        set_like_status(not like_status)
        print(f"Movie {record['original_title']} is {'liked' if not like_status else 'unliked'}")

    return reactpy.html.div(
        {
            'style': {**styles["record"], **styles["liked"]} if like_status else styles["record"],
            ':hover': styles["recordHover"],
            'class_name': 'liked' if like_status else None,
        },
        reactpy.html.img(
            {
                "src": movie_images_path + record['poster_path'],
                "style": {
                    "width": "100%",
                    "height": "auto",
                    "border_bottom": "1px solid #ccc",
                    "object_fit": "cover",
                }
            }
        ),
        reactpy.html.p(
            {
                "style": {
                    "font_size": "14px",
                    "text_align": "center",
                    "transition": "transform 0.3s ease-in-out",
                }
            },
            record.get('title', '')
        ),
        reactpy.html.button(
            {
                "style": {**styles["likeButton"], **styles["likeButtonLiked"]} if like_status else styles["likeButton"],
                'on_click': lambda event: handleLikeClick(),
            },
            "❤️" if like_status else "🤍"
        )
    )

