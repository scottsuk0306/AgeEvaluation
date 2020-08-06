from os import rename, listdir
import os
import shutil

def rename_file(path, alpha_code, check):
    idx = 500    # 시작 번호 설정 (ex. NAME1.png)
    if(check): idx=idx+500
    for file in listdir(path):
        idx += 1
        rename(path + file, path + alpha_code + str(idx) + '.png')
    print(str(idx) + " files have been renamed.")

# if __name__ == "__main__":
#     img_paths = "C:\\Users\\82108\\Documents\\GitHub\\AgeEvaluation\\Data\\All-Age-Faces Dataset\\"
#     for image_path in len(listdir(img_paths)):
#         alpha_code = image_path.split("_")[0]
#         if (image_path.split("_")[-1] == "2"):
#             rename_file(img_paths + image_path + "\\", alpha_code, 1)
#         else:
#             rename_file(img_paths + image_path + "\\", alpha_code, 0)

img_paths = "C:\\Users\\82108\\Documents\\GitHub\\AgeEvaluation\\Data\\All-Age-Faces Dataset\\aglined faces\\"

def gender_split():
    for img_path in listdir(img_paths):
        if(int(img_path.split('A')[0])<7381):
            new_path = img_paths+"female\\"+img_path
            shutil.move(img_paths+img_path,new_path)
        else:
            new_path = img_paths + "male\\" + img_path
            shutil.move(img_paths + img_path, new_path)

male_paths = img_paths+"male\\"
female_paths = img_paths+"female\\"

def age_split(img_paths):
    for img_path in listdir(img_paths):
        age = img_path.split('A')[1]
        age = int(age.split('.')[0])
        if(age <= 5):
            os.makedirs(img_paths+"2~5", exist_ok=True)
            shutil.move(img_paths+img_path, img_paths+"2~5\\"+img_path)
        elif (age <= 10):
            os.makedirs(img_paths + "6~10", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "6~10\\" + img_path)
        elif (age <= 15):
            os.makedirs(img_paths + "11~15", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "11~15\\" + img_path)
        elif (age <= 20):
            os.makedirs(img_paths + "16~20", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "16~20\\" + img_path)
        elif (age <=25):
            os.makedirs(img_paths + "21~25", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "21~25\\" + img_path)
        elif (age <= 30):
            os.makedirs(img_paths + "26~30", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "26~30\\" + img_path)
        elif (age <= 35):
            os.makedirs(img_paths + "31~35", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "31~35\\" + img_path)
        elif (age <= 40):
            os.makedirs(img_paths + "36~40", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "36~40\\" + img_path)
        elif (age <= 45):
            os.makedirs(img_paths + "41~45", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "41~45\\" + img_path)
        elif (age <= 50):
            os.makedirs(img_paths + "46~50", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "46~50\\" + img_path)
        elif (age <= 55):
            os.makedirs(img_paths + "51~55", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "51~55\\" + img_path)
        elif (age <= 60):
            os.makedirs(img_paths + "56~60", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "56~60\\" + img_path)
        elif (age <= 65):
            os.makedirs(img_paths + "61~65", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "61~65\\" + img_path)
        elif (age <= 70):
            os.makedirs(img_paths + "66~70", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "66~70\\" + img_path)
        elif (age <= 75):
            os.makedirs(img_paths + "71~75", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "71~75\\" + img_path)
        elif (age <= 80):
            os.makedirs(img_paths + "76~80", exist_ok=True)
            shutil.move(img_paths + img_path, img_paths + "76~80\\" + img_path)
