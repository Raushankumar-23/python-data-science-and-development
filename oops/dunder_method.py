
class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
        
    def __len__(self):
        return self.pages
        
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    
    
    def __call__(self, *args, **kwds):
        print("Hi")
    
    
d=Author("Raushan","Python Basic to Advance ",300)
print(len(d))
print(d)
d()