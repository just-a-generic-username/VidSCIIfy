# VidSCIIfy
A python script which converts an input video its ASCII equivalent

## Preview
ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers. Our goal is to use ASCII for videos and images instead!

An example of what we plan to do, frame by frame: 
<table>
  <tr>
    <td><img src="frame362.jpg" width=300 height=500></td>
    <td><img src="ASCIIframe362.jpg" width=300 height=500></td>
  </tr>
 </table>

## Running the project
To run the project, follow the given steps:
```
git clone https://github.com/just-a-generic-username/VidSCIIfy.git
```
Install the required packages:
```
pip install requirements.txt
```
#### To ASCIIfy videos
* In line 35 of the `ASCIIfyVideo.py` file, put in the path of your desired video as a parameter. It should be of the `.mp4` format.
* In line 42 of the `ASCIIfyVideo.py` file, change the first parameter to what you want to name the output video file. It will be in the `.avi` format.
* Run the `ASCIIfyVideo.py` file.

Voila! Your ASCIIfyed video is now ready and you can find it in the directory of your cloned project.

#### To ASCIIfy images
* In line 34 of the `ASCIIfyImages.py` file, put in the path of your desired image as a parameter.
* In line 92 of the `ASCIIfyImages.py` file, change the first parameter to what you want to name the output video file. It will be in the `.avi` format.
* Run the `ASCIIfyVideo.py` file.

Voila! Your ASCIIfyed image is now ready and you can find it in the directory of your cloned project.
