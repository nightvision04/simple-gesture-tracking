import cv2,time
import Features
import pandas as pd
import db

def check_video_frame_data():
    video=cv2.VideoCapture(0)
    check,frame = video.read()
    print(check)
    print(frame)
    video.release()
    return

# def watch_video_stream_data(encode_feature=False):
#     video=cv2.VideoCapture(0)
#
#     df = pd.DataFrame()
#     df['img_gray'] = []
#     df['time'] = []
#     df['frame'] = []
#     df['label'] = []
#
#     t1 = time.time()
#
#     a = 0
#     while True:
#         a+=1
#         check,frame = video.read()
#         # print(check)
#         # print(frame)
#         # Convert to grayscale
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('Capturing',gray)
#
#         if encode_feature==True:
#             f = Features.Collector()
#             label = f.get_key()
#             time_ = time.time()
#             df = df.append({'img_gray': [x for x in gray.ravel()],
#                             'label':label,
#                             'time': time_,
#                             'frame':frame}, ignore_index=True)
#
#         # Play stream
#         key = cv2.waitKey(1)
#         if key== ord('q'):
#             break
#
#         if ( time.time() - t1 ) > 15:
#             break
#
#     video.release()
#     cv2.destroyAllWindows
#     return df

def get_features():

    f = Features.Collector()
    df = f.get_key()
    return df

def capture_review_submit_labels():
    df = get_features()
    print('Length',len(df))
    resp=input('Enter Y to submit')
    if resp.lower() == 'y':
        db.send_df_to_table(df,'test',operation='append')
    else:
        df.to_csv('Rejected.csv')

    return
