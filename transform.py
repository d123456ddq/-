img=cv2.imread('photo.jpg')
rows,cols,channels = img.shape

#转换hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#腐蚀膨胀
erode=cv2.erode(mask,None,iterations=1)
dilate=cv2.dilate(erode,None,iterations=1)

#遍历替换
for i in range(rows):
 for j in range(cols):
  if dilate[i,j]==255:
   img[i,j]=(255,255,255)#此处替换颜色，为BGR通道
cv2.imwrite('res.jpg',img)
