import datetime

ALLOWED_EXTENSIONS = ['pdf', 'png', 'jpg', 'jpeg']



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


filename = "Captura de tela_2022-08-14_20-38-40.png"


print(not allowed_file(filename))



print(filename)