from typing import List
import urllib.request
import os

bucket_path = "https://egobody3m-bucket-1.s3.us-west-1.amazonaws.com"

sequences = ["2431173007038810", "673966801194449", "764872174807763", "923115909013017", "937647847269034",
             "557805499664836", "752624746477160", "76780933376047", "924192258613890", "938487244256666"]

out_path = "./dataset"
os.makedirs("dataset", exist_ok=True)

for sequence in sequences:
    img_path = sequence + ".images.zip"
    meta_path = sequence + ".metadata.zip"

    full_img_path = bucket_path + "/" + img_path
    full_meta_path = bucket_path + "/" + meta_path

    print (f"Sequence {sequence}")

    print (f"   Loading images from '{full_img_path}'")
    urllib.request.urlretrieve(full_img_path, os.path.join(out_path, img_path))

    print (f"   Loading metadata from '{full_meta_path}'")
    urllib.request.urlretrieve(full_meta_path, os.path.join(out_path, img_path))

