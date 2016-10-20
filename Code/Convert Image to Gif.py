import os
from PIL import Image
import images2gif

def convert_to_gif(target_gif_Path, image_file_paths, type = 0):
    # Get the images needed to convert to gif.
    images = []

    # Get the max length among the images
    max_width_and_height = 1

    # Max width and height
    max_width = 1
    max_height = 1

    # Sort the images by width
    width_and_file_paths = []

    # Sort the images by height
    height_and_file_paths = []

    # Open the images and get related information
    for image_path in image_file_paths:
        fp = open(image_path, "rb")
        width, height = Image.open(fp).size
        width_and_file_paths.append((width, image_path))
        height_and_file_paths.append((height, image_path))
        max_width = max(max_width, width)
        max_height = max(max_height, height)
        fp.close()

    # Get the max width and height
    max_width_and_height = max(max_width_and_height, max_width, max_height)

    # Sort the width and height in descending order
    width_and_file_paths.sort(key=lambda item: item[0], reverse=True)
    height_and_file_paths.sort(key=lambda item: item[0], reverse=True)

    # Choose the style to sort the images
    if type == 4 or type == 5:
        # Convert the original figures directly ordered by width
        if type == 4:
            for width_and_file_path in width_and_file_paths:
                img = Image.open(width_and_file_path[1])
                images.append(img)
                # Convert the original figures directly ordered by height
        if type == 5:
            for height_and_file_Path in height_and_file_paths:
                img = Image.open(height_and_file_path[1])
                images.append(img)

    else:
        for image_file_path in image_file_paths:
            fp = open(image_file_path, "rb")
            img = Image.open(fp)
            width, height = img.size
            # Build a white background canvas
            if type == 0 or type == 2:
                # rectangular
                imgResizeAndCenter = Image.new("RGB", [max_width, max_height], (255, 255, 255))
            elif type == 1 or type == 3:
                # quadrate
                imgResizeAndCenter = Image.new("RGB", [max_width_and_height, max_width_and_height], (255, 255, 255))

            if type == 0:
                # max width >= max height, revise the size a little bit
                if max_width / width >= max_height / height:
                    resizeImg = img.resize((width * max_height / height, max_height), Image.ANTIALIAS)
                    imgResizeAndCenter.paste(resizeImg, ((max_width - width * max_height / height) / 2, 0))
                else:
                    resizeImg = img.resize((max_width, height * max_width / width), Image.ANTIALIAS)
                    imgResizeAndCenter.paste(resizeImg, (0, (max_height - height * max_width / width) / 2))

            if type == 1:
                # width >= height, zoom the width to max length
                if width >= height:
                    resizeImg = img.resize((max_width_and_height, height * max_width_and_height / width), Image.ANTIALIAS)
                    imgResizeAndCenter.paste(resizeImg,
                                             (0, (max_width_and_height - height * max_width_and_height / width) / 2))
                else:
                    resizeImg = img.resize((width * max_width_and_height / height, max_width_and_height), Image.ANTIALIAS)
                    imgResizeAndCenter.paste(resizeImg,
                                             ((max_width_and_height - width * max_width_and_height / height) / 2, 0))
            elif type == 2:
                imgResizeAndCenter.paste(img, ((max_width - width) / 2, (max_height - height) / 2))
            elif type == 3:
                imgResizeAndCenter.paste(img, ((max_width_and_height - width) / 2, (max_width_and_height - height) / 2))

            #Save the images
            imgResizeAndCenter.convert("RGB").save(os.path.dirname(image_file_path) + os.sep + "ResizeAndCenter" + os.path.basename(image_file_path), 'jpeg')
            images.append(imgResizeAndCenter)
            fp.close()

    images2gif.writeGif(target_gif_Path, images, duration=1, nq=0.1)

if __name__ == "__main__":
    # Open result folder if it's not exist
    newpath = r'./result'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    #Save the GIF file
    convert_to_gif(r"result\convert.gif",
                              [r"world_gdppercapita 2006-2015\world_GDP percapita_2006.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2007.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2008.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2009.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2010.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2011.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2012.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2013.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2014.jpg",
                               r"world_gdppercapita 2006-2015\world_GDP percapita_2015.jpg",],
                              2)
