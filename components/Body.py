import reactpy

movie_images_path = r'https://image.tmdb.org/t/p/w500'

def Body(searchResults):
    return reactpy.html.div(
        {},
        RecordList(searchResults)
    )

def RecordList(records):
    return reactpy.html.div(
        {
            'style': {
                "margin_left": "2%",
                "margin_right": "2%",
                "margin_top": "2%",
                "display": "flex",
                "flex_wrap": "wrap",
                "justify_content": "space-around",
            }
        },
        *[Record(rec) for rec in records]
    )

def Record(record):
    return reactpy.html.div(
        {
            'style': {
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
                'on_hover': {
                "transform": "scale(1.1)",
                }
            }
            
        },
        reactpy.html.img(
            {
                "src": movie_images_path + record['poster_path'],
                "style": {
                    "width": "100%",  # Adjusted width to 100%
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
        )
    )
