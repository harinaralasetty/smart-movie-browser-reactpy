import reactpy

def Header(searchTerm, setSearchTerm):
    return reactpy.html.div(
        {
            'style': {
                "background_color": "rgb(88, 109, 226)",
                "color": "white",
                "padding": "1.75rem",
                "display": "flex",
                "align_items": "center",
                "text_align": "left",
                "padding_left": "20px",
            }
        },
        reactpy.html.img(
            {
                "src": 'sources/film-image.jpg',
                "style": {
                    "width": "70px",
                    "padding_right": "5px",
                },
                "alt": "Logo",
            }
        ),
        reactpy.html.h2(
            {
                'style': {
                    'fontSize': '24px',
                    'margin': '0',
                }
            },
            "Smart Movie Browser",
            
        ),
        reactpy.html.div(
            {
                'className': 'search-box',
                'style': {
                    'display': 'flex',
                    'align_items': 'center',
                    'justify_content': 'space-between',
                    'width': '700px',
                    'height': '30px',
                    'position': 'relative',
                    'margin_left': 'auto',
                    'margin_right': 'auto',
                    'border_radius': '20px',
                    'border': 'None',
                }
            },
            reactpy.html.input(
                {
                    "type": "text",
                    "placeholder": "Search movies...",
                    "value": searchTerm,
                    "on_change": lambda event: setSearchTerm(event['target']['value']),
                    "style": {
                        "padding_left": "15px",
                        "user_select": "auto",
                        "outline": "None",
                        "flex_grow": "1",
                        "border": "2px solid transparent",
                        "border_radius": "8px"
                    }
                }
            ),
            reactpy.html.button(
                {
                    'style': {
                        'background_color': 'transparent',
                        'border': 'None',
                        'cursor': 'pointer',
                        'right': '3.5px',
                        'position': 'absolute',
                        'align_items': 'center',
                        'vertical_align': 'center',
                        'top': '50%',
                        'transform': 'translateY(-48%)',
                    }
                },
                reactpy.html.img(
                    {
                        "src": 'sources/search-image.jpg',
                        "alt": "Search",
                        "style": {
                            "width": "35px",
                        }
                    }
                )
            )
        )
    )
