class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        
        pass

    def add_post(self, post):
        post.user = self
        self.posts.append(post)
        
        pass

    def get_timeline(self):
        self.timeline = []
        for user in self.following:
            for post in user.posts:
             self.timeline.append(post)
        return self.timeline

    def follow(self, other):
        self.following.append(other)