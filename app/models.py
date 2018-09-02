class New:
    '''
    class that defines the movie object
    '''
    
    def __init__(self,id,name,description,url,country):
        self.id = id
        self.name = name
        self.country = country
        self.description = description
        self.url = url

class Article:
    '''
    class that defines the article object
    '''

    def __init__(self,id,name,desctiption,url,urlToImage,title,publishedAt):
        self.id = id
        self.name = name
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.title = title
        self.publishedAt = publishedAt

    