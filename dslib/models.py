"""
Place classes you make here.
"""

# Just an example of what you might put here.
class User(object):
    def __init__(self, username):
        self.username = username
    
    def greeting(self):
        return 'Hello, %s!' % self.username