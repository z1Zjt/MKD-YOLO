# MKD-YOLO: Multi-Scale and Knowledge-Distilling YOLO for Efficient PPE Compliance Detection
MKD-YOLO is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. 


<details>
  <summary>
  <font size="+1">Abstract</font>
  </summary>
YOLO-based models are widely used for personal protective equipment (PPE) compliance detection due to their excellent detection performance and efficiency. However, most YOLO models are not competent for detection tasks in complex industrial scenarios such as remote surveillance and extremely small targets. In addition, there is a lack of effective model lightweighting and knowledge transfer approaches for industrial deployment. To this end, this paper proposes a Multi-scale and Knowledge-Distilling YOLO (MKD-YOLO) based on YOLOv8n for efficient PPE compliance detection. Specifically, in backbone stage, we design an Efficient Multi-Scale Enhanced Convolution (C2f-EMSEC) module and Large Spatial Pyramid Pooling-Fast (LSPPF) module for multi-scale and global-contextual feature learning as well as reducing model complexity. Then, in neck stage, a refined Bidirectional feature Pyramid Network (BPNet) is designated to capture fine-grained details for extremely small object detection. Moreover, we apply channel-wise knowledge distillation to facilitate model lightweighting and domain-specific knowledge transfer learning. Experiments on our proposed dataset and public datasets show that the proposed MKD-YOLO achieves a new state-of-the-art (SOTA) detection performance and efficiency for practical PPE compliance detection tasks. Codes and the dataset are available at [https://github.com/z1Zjt/MKD-YOLO](https://github.com/z1Zjt/MKD-YOLO). [kaylorchen](https://github.com/kaylorchen) 
</details>
