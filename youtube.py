from pytube import YouTube

SAVE_PATH = '/home/mine/Desktop/'
print("Current Path Desktop.")

link = input("Enter Link : ")

try:
	print("Connecting..........")
	yt = YouTube(link)
except Exception as e:
	print("Connection Error ! \n" + e)

title = yt.title
print("Title : " + title)

res = {'720p':22,'360p':18,'240p':36,'144p':17,'audio':140}
print(res)

itag = input("Enter resolution number : ")
d_video = yt.streams.get_by_itag(itag)

while (d_video==None):
	itag = input("Enter resolution number : ")
	d_video = yt.streams.get_by_itag(itag)

print(d_video)

try:
	filesize = (d_video.filesize)/(1024*1024)
	print("Filesize : " + str(filesize) + " MB.")
	ans = input("Want to download : (Y/N)")
	if(ans == 'Y' or ans == 'y'):
		print("Downloading.........")
		d_video.download(SAVE_PATH)
		print("Downloaded into Desktop.")
except Exception as e:
	print("Some Error ! \n" + e)

print("Task completed.")
