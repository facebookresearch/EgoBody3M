# EgoBody3M

Accurate tracking of a user's body pose while wearing a virtual reality (VR), augmented reality (AR) or mixed reality (MR) headset is a prerequisite for authentic self-expression, natural social presence, and intuitive user interfaces through body parts in VR/AR.
Existing body tracking approaches on VR/AR devices are either under-constrained, e.g., attempting to infer full body pose from only headset and controller pose, or require impractical hardware setups that place cameras far from a user's face to improve body visibility.
In this paper, we present the first controller-less egocentric body tracking solution that runs on an actual VR device using the same cameras used for SLAM tracking. We propose a novel egocentric tracking architecture that models the temporal history of body motion using multi-view latent features.
Furthermore, we release the first large-scale real-image dataset for egocentric body tracking, EgoBody3M, with a realistic VR headset configuration and diverse subjects and motions. Benchmarks on the dataset shows that our approach outperforms other state-of-the-art methods in both accuracy and smoothness of the resulting motion.  We perform ablation studies on our model choices and demonstrate the method running in realtime on a VR headset. Our dataset with more than 30 hours of recordings and 3 million frames will be made publically available.

# Dataset

The EgoBody3M dataset is released under a [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) license.

# Dataset format

The dataset consists of a set of .zip files, one for each sequence.  Each sequence is given a unique numeric ID, such as 1235456789.

The images are stored in `123456789.images.zip` and the metadata (ground truth, headset tracking) is stored in `123456789.metadata.zip`.

Each zip file unzips into a folder with the same name:

     % unzip 123456789.images.zip
     % unzip 123456789.metadata.zip
     % ls 123456789/

     123456789/frame0000_cam0.jpg
     123456789/frame0000_cam1.jpg
     123456789/frame0000_cam2.jpg
     123456789/frame0000_cam3.jpg
     123456789/frame0000.json
     123456789/frame0001_cam0.jpg
     123456789/frame0001_cam1.jpg
     123456789/frame0001_cam2.jpg
     123456789/frame0001_cam3.jpg
     123456789/frame0001.json

# Metadata format

The metadata is stored in the associated json file, `frame0000.json`.

    {
      "frame_index": 0,
      "world_from_headset_xf_cm": [
        [  -0.022884521633386612, ... ]]
      "annotation_level": 1,
      "joint_positions_world_cm": [
          [-10.3025, 149.20840, -35.62801],
          ...
      ],
      "projected_joint_positions_cam0_px": [
          [151.7043, -3.3641, -4.8595],
          ...
      ],
      "projected_joint_positions_cam1_px": [
          [283.632, 638.773, -10.2060],
          ...
      ],
      ...
    }

### frame_index

The index of the frame in the original sequence, can be used to index against the image files.

### world_frame_headset_xf_cm

Transform going from world-space to headset-local space (tracked using motion capture or inside-out head tracking).  Units are centimeters.

### joint_positions_world_cm

Positions of the 26 tracked joints, in world-space.  To transform them to headset-local space, use the inverse of the headset-to-world transform.

### projected_joint_positions_cam0_px

The joints projected into the first/second/nth camera.  This can be used to supervise e.g. heatmap losses without needing to implement the full fisheye camera model.  Note that if the z value is negative, the point is _behind_ the camera.

# Body joints

We use the [momentum body model](https://github.com/facebookincubator/momentum).
In the GT and training workflows, we use the following 26 body joints.

| Index | Joint name           | body part          |
| ----- | -------------------- | ------------------ |
| 0     | b_head               | Base of skull      |
| 1     | b_l_shoulder         | Scapula            |
| 2     | b_l_arm              | Glenohumeral       |
| 3     | b_l_forearm          | Elbow              |
| 4     | b_l_wrist            | Wrist              |
| 5     | b_r_shoulder         | Scapula            |
| 6     | b_r_arm              | Glenohumeral       |
| 7     | b_r_forearm          | Elbow              |
| 8     | b_r_wrist            | Wrist              |
| 9     | b_neck0              | Cervical           |
| 10    | b_spine0             | Sacrum             |
| 11    | b_spine1             | Top of lumbar      |
| 12    | b_spine2             | Mid-thoracic       |
| 13    | b_spine3             | Top of thoracic    |
| 14    | b_r_upleg            | Hip                |
| 15    | b_r_leg              | Knee               |
| 16    | b_r_foot_twist       | Ankle              |
| 17    | b_r_talocrural       | Ankle              |
| 18    | b_r_subtalar         | Heel               |
| 19    | b_r_transversetarsal | Midfoot            |
| 20    | b_l_upleg            | Hip                |
| 21    | b_l_leg              | Knee               |
| 22    | b_l_foot_twist       | Ankle              |
| 23    | b_l_talocrural       | Ankle              |
| 24    | b_l_subtalar         | Heel               |
| 25    | b_l_transversetarsal | Midfoot            |
