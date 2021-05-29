from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from visage import ApplyMakeup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_image():
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': "'1r3F8xFg48lqNKRSxWCBcCq7kCjMO4sN1' in parents and trashed=false"}).GetList()
    files_downloaded = []
    for file in file_list:
        file.GetContentFile(file['title'], mimetype='image/jpg')
        files_downloaded.append(file['title'])
    return files_downloaded

def get_color(color):
    color_values = {'red': [170, 10, 30], 'pink': [255, 51, 255], 'blue': [102, 102, 255], 'magenta': [153, 0, 76], 'green': [41, 196, 49]}
    return color_values[color]

def apply_makeup(file):
    AM = ApplyMakeup()
    color = input("Enter the color of the lipstick amongst red, pink, blue, magenta, green: ")
    color_values = get_color(color)
    file_with_lipstick = AM.apply_lipstick(file, color_values[0], color_values[1], color_values[2])
    file_with_liner = AM.apply_liner(file_with_lipstick)
    file_with_blush = AM.apply_blush(file_with_liner)
    print("The name of the file with final result is: ", file_with_blush)


def main():
    # images = download_image()
    # print("The image files downloaded are :", images)
    # for image in images:
    #     apply_makeup(image)

    apply_makeup('nicolascage.jpg')

if __name__ == '__main__':
    main()