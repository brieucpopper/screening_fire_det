## For more information read the PDF report.pdf in the root of the GitHub Repository !

## Organization of this repo :

- explore_dataset.ipynb is a Python Notebook to visualize the dataset and the bounding boxes, with some basic statistics.

- train_YOLO11.ipynb is a python notebook (designed to use in google Colab) to train my model. The hyperparameters there are the latest I used for my best-performing model. It generates some files found in ./training_outputs

- val_YOLO11.ipynb : validation of the trained model. It generates a whole directory of plots etc at validation_outputs. We achieve a mAP@0.5 of 0.531 which is not great but not too bad. Using a bigger YOLO11 model size, as well as using the full training set to train (and more time fine-tuning hyperparams) would lead to slightly better performance. This requires having ultralytics installed.

- Inference script (With CLI) : use the following command (in a python environment that has ultralytics installed)



```
python local_inference.py --image_path ./sample_img/example.jpg
```

Of course you can replace the example image with any image you'd like !