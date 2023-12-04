import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Mercury",
            (200, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Venus",
            (400, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Earth",
            (600, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Mars",
            (800, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Jupiter",
            (1000, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Saturn",
            (1200, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Uranus",
            (1400, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Neptune",
            (1600, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.imwrite("solar-system.jpg",img)
cv2.imshow("output",img)
cv2.waitKey(0)

