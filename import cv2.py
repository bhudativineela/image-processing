import cv2
import os

def count_rice_grains(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    total_rice_grains = len(contours)
    total_broken_grains = 0
    total_full_grains = 0
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 100:
            total_broken_grains += 1
        else:
            total_full_grains += 1
    
    return total_rice_grains, total_broken_grains, total_full_grains


test_folder = "test"
submission_file = "submission.csv"


with open(submission_file, "w") as file:
    file.write("Image,Total Rice Grains,Total Broken Grains,Total Full Grains\n")


    for image_file in os.listdir(test_folder):
        image_path = os.path.join(test_folder, image_file)
        total_rice_grains, total_broken_grains, total_full_grains = count_rice_grains(image_path)
        file.write(f"{image_file},{total_rice_grains},{total_broken_grains},{total_full_grains}\n")

print("Counting completed and submission file created!")