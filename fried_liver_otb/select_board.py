import cv2
import numpy as np
import copy

def transform_board(full_img):
    """Take an image including a chess board
    Then the user selects the corners of A1, H1, H8 and A8
    The the function returns an img of just the chess board."""
    
    copy_img = copy.deepcopy(full_img)
    points=[]

    def click_event(event, x, y, flags, params): 
        
        if event == cv2.EVENT_LBUTTONDOWN: 
            points.append((x, y))
            cv2.circle(copy_img,(x,y),5,(0,0,255),-1)
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(copy_img,str(x)+','+str(y),(x,y), font,1,(255, 0, 0),2) 
            cv2.imshow('image', copy_img) 

    cv2.imshow('image', copy_img) 
    cv2.setMouseCallback('image', click_event) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pts_1 = np.float32(points)
    pts_2 = np.float32(((0,400), (400,400), (400, 0), (0, 0)))

    transformer = cv2.getPerspectiveTransform(pts_1, pts_2)

    new_img = cv2.warpPerspective(full_img, transformer, (400,400))
    
    return(new_img)