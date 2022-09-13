import pygame 
import random 
import time

pygame.init()
FONT=pygame.font.SysFont("comicsans",30)


class Info:
    WHITE=(255,255,255)
    GREEN=(0,255,0)
    RED=(255,0,0)
    SHADES=[(220,220,220),(169,169,169),(128,128,128)]
    def __init__(self,width,height,max_val_range,min_val_range,num_vals):
        self.width=width
        self.height=height 
        self.max_val=max_val_range
        self.min_val=min_val_range
        self.num_vals=num_vals
        self.window=pygame.display.set_mode((self.width,self.height))
        self.caption=pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.box_width=(self.width-100)//self.num_vals
        self.lst=self.generate_list()
        self.scale=10
        self.title_text_one="b - bubble sort | i - insertion sort | s - selection sort"
        self.title_text_two=" r - RESET"
        self.colors={}

    def generate_list(self):
        list=[]
        cur_x=50
        for i in range(self.num_vals):
            num=random.randint(self.min_val,self.max_val)
            list.append(num)
        return list 
    
    def draw(self):
        self.window.fill(self.WHITE)
        text_one=FONT.render(self.title_text_one,1,(0,0,0))
        text_two=FONT.render(self.title_text_two,1,(0,0,0))
        self.window.blit(text_one,(self.width//2-text_one.get_width()//2,40))
        self.window.blit(text_two,(self.width//2-text_two.get_width()//2,70))
        cur_x=50
        for i in range(len(self.lst)):
            val=self.lst[i]
            pygame.draw.rect(self.window,self.SHADES[i%3] if i not in self.colors else self.colors[i],(cur_x,self.height-(val*10),self.box_width,val*10))
            cur_x+=self.box_width
    
    def bubble_sort(self):
        lim=255
        for i in range(len(self.lst)-1):
            for j in range(len(self.lst)-1-i):
                if self.lst[j]>self.lst[j+1]:
                    self.lst[j],self.lst[j+1]=self.lst[j+1],self.lst[j]
                    self.draw()
                    yield True 
            self.colors[j+1]=(0,lim,0)
            lim-=10
    
    def insertion_sort(self):
        lim=255
        for step in range(1,len(self.lst)):
            key=self.lst[step]
            j=step-1 
            while j>=0 and key<self.lst[j]:
                self.lst[j+1]=self.lst[j]
                self.draw()
                yield True 
                j-=1 
            self.lst[j+1]=key
            self.colors[step]=(0,lim,0)
            lim-=10
    
    def selection_sort(self):
        lim=255 
        for i in range(len(self.lst)):
            min_idx=i
            for j in range(i+1,len(self.lst)):
                if self.lst[j]<self.lst[min_idx]:
                    min_idx=j 
            self.lst[i],self.lst[min_idx]=self.lst[min_idx],self.lst[i]
            self.draw()
            self.colors[i]=(0,lim,0)
            lim-=10
            yield True 
    
    def heap_sort(self):
        max_heap=MaxHeap(self.lst,self)
        max_heap.sort()



def main():
    run=True 
    display_info=Info(700,700,50,0,20)
    clock=pygame.time.Clock()
    sorting=False
    algorithm=None 
    while run:
        clock.tick(20)
        if sorting:
            try:
                next(algorithm)
            except StopIteration:
                sorting=False 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False 
            keys=pygame.key.get_pressed()
            if keys[pygame.K_b]and not sorting:
                sorting=True
                algorithm=display_info.bubble_sort()
            
            if keys[pygame.K_i]:
                sorting=True 
                algorithm=display_info.insertion_sort()
            
            if keys[pygame.K_s]:
                sorting=True 
                algorithm=display_info.selection_sort()
            
            if keys[pygame.K_r]:
                sorting=False 
                display_info=Info(700,700,50,0,20)
                algorithm=None
            
            if keys[pygame.K_h]:
                display_info.heap_sort()
        display_info.draw()
        pygame.display.update()
    pygame.quit()



if __name__=="__main__":
    main()
