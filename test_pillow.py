from PIL import Image,ImageDraw
import ipdb

if __name__ == '__main__':
    base_img = Image.open('base.png')
    w = base_img.width
    h = base_img.height
    box = ((w-400),(h-400),(w-100),(h-100))
    box_w = ((w - 410), (h - 410), (w - 90), (h - 90))
    draw_img = ImageDraw.Draw(base_img)
    draw_img.rectangle(box_w, fill=(192,192,192))
    color = Image.open('color.png')
    new_color = color.resize((300,300),Image.ANTIALIAS)
    base_img.paste(new_color,box)
    base_img.save('new_ps.png')
