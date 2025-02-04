from ultralytics import YOLO
import argparse
if __name__ == '__main__':

    #parse arg for image input
    parser = argparse.ArgumentParser(description='Inference on image')
    parser.add_argument('--image_path', type=str, help='path to image')
    args = parser.parse_args()


    model = YOLO('./training_outputs/weights/best.pt')

    # Inference
    results = model(args.image_path)

    
    result = results[0]
    output_path = "inference_output.jpg"
    print(f"Saving output to {output_path}")
    result.save(filename=output_path)
    

