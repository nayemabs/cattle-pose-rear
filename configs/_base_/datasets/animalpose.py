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
            name='Nose', id=0, color=[128, 128, 128], type='upper', swap=''),
        1:
        dict(
            name='Neck',
            id=1,
            color=[128, 128, 128],
            type='upper',
            swap=''),
        2:
        dict(
            name='Shoulderbone',
            id=2,
            color=[255, 0, 0],
            type='upper',
            swap=''),
        3:
        dict(
            name='Wither',
            id=3,
            color=[128, 128, 0],
            type='upper',
            swap=''),
        4:
        dict(name='Pinbone', id=4, color=[0, 0, 255], type='upper', swap=''),
        5:
        dict(name='Front-Girth-Upper', id=5, color=[128, 0, 128], type='upper', swap=''),
        6:
        dict(
            name='Front-Girth-Lower', id=6, color=[128, 128, 0], type='lower',
            swap=''),
        7:
        dict(
            name='Rear-Girth-Upper', id=7, color=[100, 120, 100], type='upper', swap=''),
        8:
        dict(
            name='Rear-Girth-Lower',
            id=8,
            color=[120, 100, 100],
            type='upper',
            swap=''),
        9:
        dict(
            name='Front-Left-Shoulder',
            id=9,
            color=[255, 128, 0],
            type='lower',
            swap='Front-Right-Shoulder'),
        10:
        dict(
            name='Front-Left-Knee',
            id=10,
            color=[0, 255, 0],
            type='lower',
            swap='Front-Right-Knee'),
        11:
        dict(
            name='Front-Left-Hoof',
            id=11,
            color=[255, 128, 0],
            type='lower',
            swap='Front-Right-Hoof'),
        12:
        dict(
            name='Front-Right-Shoulder',
            id=12,
            color=[0, 255, 0],
            type='lower',
            swap='Front-Left-Shoulder'),
        13:
        dict(
            name='Front-Right-Knee',
            id=13,
            color=[255, 128, 0],
            type='lower',
            swap='Front-Left-Knee'),
        14:
        dict(
            name='Front-Right-Hoof',
            id=14,
            color=[0, 255, 0],
            type='lower',
            swap='Front-Left-Hoof'),
        15:
        dict(
            name='Rear-Left-Shoulder',
            id=15,
            color=[255, 128, 0],
            type='lower',
            swap='Rear-Right-Shoulder'),
        16:
        dict(
            name='Rear-Left-Knee',
            id=16,
            color=[0, 255, 0],
            type='lower',
            swap='Rear-Right-Knee'),
        17:
        dict(
            name='Rear-Left-Hoof',
            id=17,
            color=[255, 128, 0],
            type='lower',
            swap='Rear-Right-Hoof'),
        18:
        dict(
            name='Rear-Right-Shoulder',
            id=18,
            color=[0, 255, 0],
            type='lower',
            swap='Rear-Left-Shoulder'),
        19:
        dict(
            name='Rear-Right-Knee',
            id=19,
            color=[255, 128, 0],
            type='lower',
            swap='Rear-Left-Knee'),
            
        20:
        dict(
            name='Rear-Right-Hoof',
            id=20,
            color=[255, 128, 0],
            type='lower',
            swap='Rear-Left-Hoof'),
          
        21:
        dict(
            name='Side-Height-Upper',
            id=21,
            color=[255, 128, 0],
            type='lower',
            swap=''),
            

        22:
        dict(
            name='Side-Height-Lower',
            id=22,
            color=[255, 128, 0],
            type='lower',
            swap='')
            },


    skeleton_info={
        0: dict(link=('Nose', 'Neck'), id=0, color=[51, 153, 255]),
        1: dict(link=('Shoulderbone', 'Pinbone'), id=1, color=[0, 255, 0]),
        2: dict(link=('Pinbone', 'Wither'), id=2, color=[255, 128, 0]),
        3: dict(link=('Front-Girth-Upper', 'Front-Girth-Lower'), id=3, color=[0, 255, 0]),
        4: dict(link=('Rear-Girth-Upper', 'Rear-Girth-Lower'), id=4, color=[255, 128, 0]),
        5: dict(link=('Front-Left-Shoulder', 'Front-Left-Knee'), id=5, color=[51, 153, 255]),
        6: dict(link=('Front-Left-Knee', 'Front-Left-Hoof'), id=6, color=[51, 153, 255]),
        7: dict(link=('Front-Right-Shoulder', 'Front-Right-Knee'), id=7, color=[51, 153, 255]),
        8: dict(link=('Front-Right-Knee', 'Front-Right-Hoof'), id=8, color=[0, 255, 0]),
        9: dict(link=('Side-Height-Upper', 'Side-Height-Lower'), id=8, color=[0, 255, 0]),

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
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.2, 1.2, 1.2, 1.2,
        1.5, 1.5, 1.5, 1.5,1.5,1.5,1.5
    ],

    # Note: The original paper did not provide enough information about
    # the sigmas. We modified from 'https://github.com/cocodataset/'
    # 'cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py#L523'
    sigmas=[
        0.025, 0.025, 0.026, 0.035, 0.035, 0.10, 0.10, 0.10, 0.107, 0.107,
        0.107, 0.107, 0.087, 0.087, 0.087, 0.087, 0.089, 0.089, 0.089, 0.089, 0.089, 0.089 , 0.89
    ])
