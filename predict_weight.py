
import numpy as np

import joblib
from mmpose.apis import (inference_top_down_pose_model, init_pose_model,
                         vis_pose_result, process_mmdet_results)
from mmdet.apis import inference_detector, init_detector
from mmseg.apis import init_segmentor, inference_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette



def predict(rear_fname, side_fname):

    seg_config_file = 'models/v1/seg/deeplabv3plus_r101-d8_512x512_40k_voc12aug.py'
    seg_checkpoint_file = 'models/v1/seg/deeplabv3plus_r101-d8_512x512_40k_voc12aug/iter_40000.pth'

    rear_pose_config = 'models/v1/rear_pose/res152_animalpose_256x256.py'
    rear_pose_checkpoint = 'models/v1/rear_pose/epoch_210.pth'
    side_pose_config = 'models/v1/side_pose/res152_animalpose_256x256.py'
    side_pose_checkpoint = 'models/v1/side_pose/epoch_210.pth'
    det_config = 'models/v1/det/faster_rcnn_r50_fpn_coco.py'
    det_checkpoint = 'https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    weight_filename = "weight_joblib/alpha_model_april_2022.joblib"
    # initialize seg & pose model
    # build the model from a config file and a checkpoint file
    model = init_segmentor(seg_config_file, seg_checkpoint_file, device='cuda:0')

    rear_pose_model = init_pose_model(rear_pose_config, rear_pose_checkpoint)
    side_pose_model = init_pose_model(side_pose_config, side_pose_checkpoint)

    # initialize detector
    rear_det_model = init_detector(det_config, det_checkpoint)
    side_det_model = init_detector(det_config, det_checkpoint)

    rear_img = rear_fname
    side_img = side_fname

    # inference detection
    rear_mmdet_results = inference_detector(rear_det_model, rear_img)
    side_mmdet_results = inference_detector(side_det_model, side_img)

    # extract person (COCO_ID=1) bounding boxes from the detection results
    rear_person_results = process_mmdet_results(rear_mmdet_results, cat_id=20)
    side_person_results = process_mmdet_results(side_mmdet_results, cat_id=20)

    # inference Segmentation
    seg_result = inference_segmentor(model, side_img)


    seg = np.asarray(seg_result)
    sticker = cattle = bg = 0


    sticker = (seg == 0).sum()

    cattle = (seg == 1).sum()

    bg =( seg == 2).sum()


    # inference pose
    rear_pose_results, rear_returned_outputs = inference_top_down_pose_model(rear_pose_model,
                                                                rear_img,
                                                                rear_person_results,
                                                                bbox_thr=0.3,
                                                                format='xyxy',
                                                                dataset=rear_pose_model.cfg.data.test.type)
    side_pose_results, side_returned_outputs = inference_top_down_pose_model(side_pose_model,
                                                                side_img,
                                                                side_person_results,
                                                                bbox_thr=0.3,
                                                                format='xyxy',
                                                                dataset=side_pose_model.cfg.data.test.type)

    # KPT rear and side
    rear_kpt = rear_pose_results[0]["keypoints"][:,0:2]
    side_kpt = side_pose_results[0]["keypoints"][:,0:2]

    rearKptID=rearx0=reary0=rearx1=reary1=rearx2=reary2=rearx3=reary3=0
    sideKptID=sidex0=sidey0=sidex1=sidey1=sidex5=sidey5=sidex2=sidey2=sidex4=sidey4=sidex3=sidey3=0

    for kptx,kpty in rear_kpt:
        if rearKptID == 0:
            rearx0 = kptx
            reary0 = kpty
        elif rearKptID == 1:
            rearx1 = kptx
            reary1 = kpty
        elif rearKptID == 2:
            rearx2 = kptx
            reary2 = kpty
        elif rearKptID == 3:
            rearx3 = kptx
            reary3 = kpty
    
        rearKptID+=1

    for kptx,kpty in side_kpt:

        if sideKptID == 0:
            sidex0 = kptx
            sidey0 = kpty
        elif sideKptID == 1:
            sidex1 = kptx
            sidey1 = kpty
        elif sideKptID == 2:
            sidex5 = kptx
            sidey5 = kpty
        elif sideKptID == 3:
            sidex2 = kptx
            sidey2 = kpty
        elif sideKptID == 4:
            sidex4 = kptx
            sidey4 = kpty
        elif sideKptID == 5:
            sidex3 = kptx
            sidey3 = kpty   

        sideKptID+=1

    side_Length = round(((sidey1-sidey0)**2+(sidex1-sidex0)**2)**0.5)
    side_F_Girth = round(((sidey3-sidey2)**2+(sidex3-sidex2)**2)**0.5)
    side_R_Girth = round(((sidey5-sidey4)**2+(sidex5-sidex4)**2)**0.5)
    rear_width = round(((reary1-reary0)**2+(rearx1-rearx0)**2)**0.5)
    rear_height = round(((reary3-reary2)**2+(rearx3-rearx2)**2)**0.5)


    print(f'side_Length = {side_Length}, side_F_Girth = {side_F_Girth}, side_R_Girth = {side_R_Girth}, rear_Width = {rear_width}, rear_Height = {rear_height}')


    # Weight prediction

    loaded_model = joblib.load(weight_filename)
    predicted_cattle_weight = loaded_model.predict([[side_Length,	side_F_Girth,	side_R_Girth,	rear_width,	sticker,	cattle]])
    return predicted_cattle_weight


print(predict('tests/data/cow/6.0_r_96_5.0_M.jpg','tests/data/cow/6.0_s_96_5.0_M.jpg'))
