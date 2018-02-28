# object_classification_with_MNIST-fashion
Item Classification with MNIST fashion dataset. Images are of size 28 * 28 size. <br/>
Download dataset from here : https://www.kaggle.com/zalando-research/fashionmnist<br/>
Items are namely : <br/>

| ID | Item Name  |
| -- | ---------- |
| 0  | T-shirt/top|
| 1  | Trouser    |
| 2  | Pullover   |
| 3  | Dress      |
| 4  | Coat       |
| 5  | Sandal     |
| 6  | Shirt      |
| 7  | Sneaker    |
| 8  | Bag        |
| 9  | Ankle boot |

Here is image of showing full dataset in a glance. <br/>
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/fashion-mnist-sprite.png)
## Requirements
1. Tensorflow-gpu v1.3.0
2. Keras v2.1.3
3. Pandas
4. Numpy v1.14.0
5. sklearn v0.19.1
6. matplotlib
7. PIL (python image library) v4.2.1
8. OpenCV (cv2) v3.3.0


## Before usage
Neural network only give best results when we give similar images on which it is trained in testing phase.<br/> 
So, I am showing some images on which it is trained.<br/>
You should use this model with "<b>similar</b>" images. Not on completly different images.
1. T-shirt/top : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/T-shirt-top.jpg)

2. Trouser : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Trouser1.jpg)

3. Pullover : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/pullover1.jpg)

4. Dress : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Dressp.jpg)

5. Coat : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Coat1.jpg)

6. Sandal : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Sandal1.jpg)

7. Shirt : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Shirt1.jpg)

8. Bag : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Bag1.jpg)

9. Ankle Boot : 
![alt text](https://github.com/prashant-kikani/object_classification_with_MNIST-fashion/blob/master/sample_images/Ankle_boot1.jpg)

## Usage

Run command <br/>
```
python test.py ImagePath
```
<br/>
In short give path of test image as command line argument.

