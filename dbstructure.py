import uuid
import os
import datetime as dt

{ 
    "id" : uuid.uuid4(),
    "date-created" : dt.datetime.now(),

    # school, fun, reference
    # selected by dropdown most likely.
    "category" : "school",

    # only available if category == school.
    "dept" : "csce".upper(),
    "course" : "314".strip(),

    # typed in by user at upload
    "tags" : ["haskell", "programming", "functional-programming"],
    
    # fetched from google books api after title is typed in
    "gbooks" : {
        'title' : '',
        'subtitle' : '',
        'publisher' : '',
        'publishedDate' : '',
        'descr' : '',
        'abstract' : '',
        'thumbnail' : '',
        'authors' : '',
        'categories' : '',
        'rating' : ''
    }
}