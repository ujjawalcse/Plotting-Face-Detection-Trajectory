# Plotting-Face-Detection-Trajectory
In this repository i cloned the "Faced" repository to detect human faces.
You can read the read.md file in Faced folder where you can get aal the details about that repository.

###But my purpose of cloning this repository is not just detecting faces in an image or video.
I wanted to try many extra things that is very interesting and funny.

###I made many changes in the default face detection code provided by the "Faced" that you can see in the "face_dectection.py"

##I just used the bboxes and stored x_centre, y_centre in two separate lists.
since frame rate of my first video input( "input/video1.mp3") is 30 frames per second i.e. one frame takes 1/30 seconds,
that's why i created another list of size len(x_centre) or len(y_centre) and stored values as 0,1/30,2/30,3/30.......upto ##len(x_centre)

###In "face_detection.py" Plotting code lines are commented beacause i have saved the plot after executing once. 
###Therefore it will not consume time while processing further code lines.

##Third step is very interesting and little bit funny also.
##I took a face image ("input\human_face.jpg") and try to move it on the above detected trajectory.
###What i did for that ?
##loop over len(x_centre)
  ##i simply took an empty image( white image)
  ##then clip the human_face image to i'th x_centre and y_centre
  ##showing the image each time
  
##It seems like a video is playing in which human_face is moving.
##Notice that the human_face moves always on the same trajectory on which the person in the video1 moves.
##Then saved that video at "output\vid1.avi"
  
