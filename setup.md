# Personal Notes

## Training CLI 
e.g.:
```
python3 train.py --dataroot ./datasets/large_earthb_syn2lab/ --name leb_lowlab_syn2lab --model cycle_gan --display_id -1
python3 train.py --dataroot ./datasets/close_syn2_lab/ --name no_lab_background_syn2lab --model cycle_gan --display_id -1 --n_epochs 50 --n_epochs_decay 25\
python3 train.py --dataroot ./datasets/more_lab/ --name more_data_syn2lab --model cycle_gan --display_id -1 
```

## Testing CLI
e.g.,:
```
cp ./checkpoints/zoomed_syn2lab/latest_net_G_A.pth ./checkpoints/zoomed_syn2lab/latest_net_G.pth
python3 test.py --dataroot datasets/close_syn2_lab/testA/ --name zoomed_syn2lab --model test --no_dropout
```

## Local Setup for `more_lab`

```
cp ~/all_vicon_imgs_resized/* trainB/
cp ~/ext_research_repos/Dataset/cygnus/cyg_nm_norm_4k/*image*.png ~/ext_research_repos/cycleGAN/datasets/more_lab/trainA/
cp ~/ext_research_repos/Dataset/cygnus/cyg_nm_re_g_4k/*image*.png ~/ext_research_repos/cycleGAN/datasets/more_lab/trainA/
cp ~/ext_research_repos/Dataset/cygnus/cyg_nm_re_o_2k/*image*.png ~/ext_research_repos/cycleGAN/datasets/more_lab/trainA/
python3 train.py --dataroot ./datasets/more_lab/ --name more_data_syn2lab --model cycle_gan --display_id -1 --n_epochs 50 --n_epochs_decay 25  --batch_size 8
```

## Count number of files in a folder
```
ls trainA/ -1 | wc -l
```