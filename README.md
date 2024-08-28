1. set your image data
   
               helmet/
            ├── with_helmet/
            │   ├── image1.jpg
            │   ├── image2.jpg
            │   ├── ...
            ├── without_helmet/
                ├── image1.jpg
                ├── image2.jpg
                ├── ...
   
2. Launch chap1.py file. A folder called 'datahelmet' is created, with subfolders named 'train' and 'valid', and the images in 'withhelmet' and 'withouthelmet' are divided into each folder at a each certain percentage.
3. Launch chap2.py file. chap2.py is file that train image file in /datahelmet/train and save trained model's parameter in Helmetv3.keras
4. Launch mt3.py file. mt3.py have capture part, image save part, predict part, control part. When each part get started, theme sound get started together.
           mt3.py's work flow
           1) take_photo
           2) save_photo
           3) predict_photo
           4) if it predict "with_helmet", Solenoid will open
           5) if it predict "without_helmet", Solenoid close and add 1 count on fail_count. system recall take_photo
           6) if faile_count get 5 count, system stops for 1 minute
           7) after 1minute, system recall take_photo
