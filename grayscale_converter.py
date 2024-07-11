import os, cv2, shutil

import pdb

def convert_to_grayscale(img_path, save_path):
    img     = cv2.imread(img_path)
    gray    = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(save_path, gray)


# target_dir  = '/home/saa4743/cygnus_test_datasets/images/cygnus_journal_paper1'
# save_dir    = '/home/saa4743/cygnus_test_datasets/images/cygnus_journal_paper1_gray_no_meta_mask'
# image_pref  = 'image_'

# target_dir  = '/home/saa4743/KeypointRCNN_trainer/vicon_imagery/assorted_imagery'
# save_dir    = '/home/saa4743/KeypointRCNN_trainer/vicon_imagery/assorted_imagery_gray'
# image_pref  = 'camio_'


# target_dir  = '/home/saa4743/ext_research_repos/cycleGAN/datasets/syn2lab/trainA'
# save_dir    = '/home/saa4743/ext_research_repos/cycleGAN/datasets/syn2lab_gray/trainA'
# image_pref  = 'image_'

# target_dir  = '/home/saa4743/ext_research_repos/cycleGAN/datasets/syn2lab/trainB'
# save_dir    = '/home/saa4743/ext_research_repos/cycleGAN/datasets/syn2lab_gray/trainB'
# image_pref  = 'camio_'

target_dir  = '/home/saa4743/ext_research_repos/cycleGAN/datasets/syn2lab/testA'
save_dir    = '/home/saa4743/ext_research_repos/cycleGAN/datasets/syn2lab_gray/testA'
image_pref  = 'image_'



imgs_exts   = ['.jpg', '.jpeg', '.png']

if os.path.exists(save_dir):
    shutil.rmtree(save_dir)
os.makedirs(save_dir)
target_files = os.listdir(target_dir)
target_imgs = sorted( [os.path.join(target_dir,f) for f in target_files if f.startswith(image_pref) and f.endswith(tuple(imgs_exts))] )

for img_path in target_imgs:
    img_fn      = os.path.basename(img_path)
    ext         = '.' + img_fn.split('.')[-1]
    save_fn     = img_fn.replace(ext, '_gray' + ext)
    save_path   = os.path.join(save_dir, save_fn)
    convert_to_grayscale(os.path.join(target_dir, img_path), save_path)
