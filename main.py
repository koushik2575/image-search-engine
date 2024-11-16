import os
from engine.image import Image
from engine.search_engine import SearchEngine

def add_images_from_directory(directory, search_engine):
    
    for filename in os.listdir(directory):
       
        if filename.endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(directory, filename)
            
            tags = filename.split('.')[0].split('_') 

            image = Image(filename, tags, file_path)
            search_engine.add_image(image)

def main():

    search_engine = SearchEngine()

    image_directory = './data'

    add_images_from_directory(image_directory, search_engine)

    keyword = input("Enter a keyword to search for images: ")
    search_engine.search_by_keyword(keyword)

if __name__ == "__main__":
    main()
