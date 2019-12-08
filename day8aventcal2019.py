# Advent of Code 2019
# challenge day 8
# https://adventofcode.com/2019/day/7

WIDE = 25
TALL = 6

# 2nd part of the challenge, decoding image


def decoding_image(image):
    """ Decode the image, turns black into " " 
    and white into "*" to see the image message"""
    decoded_image = []
    for j in range(TALL):
        decoded_line = []
        for i in range(WIDE):
            for h in range(total_layer):
                pix = image[h][0][j*WIDE+i]
                if pix == 0:
                    pix = " "
                    break
                elif pix == 1:
                    pix = "*"
                    break
            decoded_line.append(pix)
        decoded_image.append(decoded_line)
    return decoded_image


if __name__ == "__main__":
    f = open("./day 8/inputday8.txt", "r")
    data = f.readline()
    image = []
    imge_dimen = WIDE*TALL
    total_layer = len(data)//imge_dimen
    for h in range(total_layer):
        layer = []
        for j in range(TALL):
            for i in range(WIDE):
                layer.append(int(data[imge_dimen*h+WIDE*j+i]))
        image.append((layer, layer.count(0)))

    # 1st part of the challenge
    new_image = sorted(image, key=lambda x: x[1])
    print(new_image[0][0].count(1) * new_image[0][0].count(2))

    # 2nd part of the challenge, decoding image
    decoded_image = decoding_image(image)
    for item in decoded_image:
        for it in item:
            print(it, end="")
        print()
