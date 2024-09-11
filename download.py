from typing import List
import urllib.request
import os
from sequences import train_sequences, test_sequences, validation_sequences

bucket_path = "https://egobody3m-bucket-1.s3.us-west-1.amazonaws.com"

os.makedirs("dataset", exist_ok=True)

def tmp_file_name(file: str):
    return file + "_tmp"

def download_sequences(sequences : List[str], out_path : str, aws_folder_name : str):
    os.makedirs(out_path, exist_ok=True)
    for sequence in sequences:
        img_path = sequence + ".images.zip"
        meta_path = sequence + ".metadata.zip"

        full_img_path = aws_folder_name + "/" + img_path
        full_meta_path = aws_folder_name + "/" + meta_path

        out_img_path = os.path.join(out_path, img_path)
        out_meta_path = os.path.join(out_path, meta_path)

        print (f"Sequence {sequence}")
        if os.path.isfile(out_img_path) and os.path.isfile(out_meta_path):
            print(f"Skipping {sequence} because already downloaded.")
            continue
    
        print (f"   Loading images from '{full_img_path}'")
        urllib.request.urlretrieve(full_img_path, tmp_file_name(out_img_path))
        os.rename(tmp_file_name(out_img_path), out_img_path)
    
        print (f"   Loading metadata from '{full_meta_path}'")
        urllib.request.urlretrieve(full_meta_path, tmp_file_name(out_meta_path))
        os.rename(tmp_file_name(out_meta_path), out_meta_path)


download_sequences(train_sequences, "./dataset/train", bucket_path + "/train")
download_sequences(test_sequences, "./dataset/test", bucket_path)
download_sequences(validation_sequences, "./dataset/validation", bucket_path + "/validation")

