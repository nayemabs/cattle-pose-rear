dataset_info = dict(
    dataset_name='animalpose',
    paper_info=dict(
        author='Cao, Jinkun and Tang, Hongyang and Fang, Hao-Shu and '
        'Shen, Xiaoyong and Lu, Cewu and Tai, Yu-Wing',
        title='Cross-Domain Adaptation for Animal Pose Estimation',
        container='The IEEE International Conference on '
        'Computer Vision (ICCV)',
        year='2019',
        homepage='https://sites.google.com/view/animal-pose/',
    ),
    keypoint_info={
        0:
        dict(
            name='Rear-Height-top', id=0, color=[255, 0, 255], 
            type='upper', 
            swap=''),
        1:
        dict(
            name='Rear-Height-bottom',
            id=1,
            color=[128, 128, 128],
            type='lower',
            swap=''),
        2:
        dict(
            name='Rear-Left',
            id=2,
            color=[255, 0, 0],
            type='upper',
            swap='Rear-Right'),
        3:
        dict(
            name='Rear-Right',
            id=3,
            color=[128, 128, 0],
            type='upper',
            swap='Rear-Left'),
       
            },


    skeleton_info={
        0: dict(link=('Rear-Height-top', 'Rear-Height-bottom'), id=0, color=[51, 153, 255]),
        1: dict(link=('Rear-Left', 'Rear-Right'), id=1, color=[0, 255, 0]),


        # 9: dict(link=('', 'L_F_Knee'), id=9, color=[0, 255, 0]),
        # 10: dict(link=('L_F_Knee', 'L_F_Paw'), id=10, color=[0, 255, 0]),
        # 11: dict(link=('Throat', 'R_F_Elbow'), id=11, color=[255, 128, 0]),
        # 12: dict(link=('R_F_Elbow', 'R_F_Knee'), id=12, color=[255, 128, 0]),
        # 13: dict(link=('R_F_Knee', 'R_F_Paw'), id=13, color=[255, 128, 0]),
        # 14: dict(link=('TailBase', 'L_B_Elbow'), id=14, color=[0, 255, 0]),
        # 15: dict(link=('L_B_Elbow', 'L_B_Knee'), id=15, color=[0, 255, 0]),
        # 16: dict(link=('L_B_Knee', 'L_B_Paw'), id=16, color=[0, 255, 0]),
        # 17: dict(link=('TailBase', 'R_B_Elbow'), id=17, color=[255, 128, 0]),
        # 18: dict(link=('R_B_Elbow', 'R_B_Knee'), id=18, color=[255, 128, 0]),
        # 19: dict(link=('R_B_Knee', 'R_B_Paw'), id=19, color=[255, 128, 0])
    },
    joint_weights=[
        1., 1., 1., 1.
    ],

    # Note: The original paper did not provide enough information about
    # the sigmas. We modified from 'https://github.com/cocodataset/'
    # 'cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py#L523'
    sigmas=[
       0.089, 0.089, 0.089 , 0.89
    ])
