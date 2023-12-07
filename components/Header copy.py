from reactpy import component, html

def Header(app_name): 
    return html.div(
        html.img(
            {
                "src" : "sosurces/film-image.jpg" ,
                "style": {"width": "50%"},
                "alt": "Logo"
            }
        ),
        html.h2(app_name),
        # html.input("Seach Box")
        # {"style" :{"flex":"row"} }
    )
