class Pagination:

    def __init__(self, items, page_size = 10):
        self.items = items
        self.page_size = int(page_size)


    def getVisibleItems(self):
        visible_items = []
        while self.page_size in self.items:
         visible_items += self.page_size
        return visible_items
    
    # def prevPage(self)
        
    # def firstPage(self)
    
    # def lastPage(self)
    
    # def goToPage(pageNum)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.getVisibleItems() 