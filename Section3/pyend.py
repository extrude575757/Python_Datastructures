How Do I Decode/Encode A Video To A Text File and then Back To Video?
Asked 2 years, 5 months ago
Active 2 years, 5 months ago
Viewed 4k times

3


1
I want to take a video - take the video contents - and turn it into base64. Then, I want to take that text file - decode it from base64 - and then turn it back into a video.

Currently, I have been able to turn the video into a text file, but when I try to convert it back into a video I get an empty text file instead of a video file.

How do I fix this?

import base64



with open("al.mp4", "rb") as videoFile:
    text = base64.b64encode(videoFile.read())
    print(text)
    file = open("textTest.txt", "wb") 
    file.write(text)
    file.close()

    fh = open("video.mp4", "wb")
    fh.write(base64.b64decode(str))
    fh.close()
python
Share
Improve this question
Follow
edited May 22 '19 at 2:49
asked May 22 '19 at 2:36

Jackson Ennis
30522 silver badges77 bronze badges
You are not writing anything to the mp4 file. str is an empty string here. – 
nullptr
 May 22 '19 at 2:47
Using names of built-in Python functions or types like str is not recommended. – 
Michael Butscher
 May 22 '19 at 2:49 
Sorry, I've updated it @nullptr - same error though – 
Jackson Ennis
 May 22 '19 at 2:49 
Now str is the builtin string type. It can't be written to a file. – 
Michael Butscher
 May 22 '19 at 2:50 
Can you explain that? I don't quite understand what it is, or how to fix it – 
Jackson Ennis
 May 22 '19 at 2:51
Show 2 more comments
1 Answer

3

import base64



with open("al.mp4", "rb") as videoFile:
    text = base64.b64encode(videoFile.read())
    print(text)
    file = open("textTest.txt", "wb") 
    file.write(text)
    file.close()

    fh = open("video.mp4", "wb")
    fh.write(base64.b64decode(text))
    fh.close()
This is the code that works.
You were trying to write str to the file. Now str in python is the name of the string class. You can do something like str = "assda" but that is not recommended. And furthermore, str is not the stuff you just read from the file. That is text. Just write text and you're good.