# Personal Notes

## Training CLI 
e.g.:
```
python3 train.py --dataroot ./datasets/large_earthb_syn2lab/ --name leb_lowlab_syn2lab --model cycle_gan --display_id -1
python3 train.py --dataroot ./datasets/close_syn2_lab/ --name no_lab_background_syn2lab --model cycle_gan --display_id -1 --n_epochs 50 --n_epochs_decay 25
```

## Testing CLI
e.g.,:
```
cp ./checkpoints/zoomed_syn2lab/latest_net_G_A.pth ./checkpoints/zoomed_syn2lab/latest_net_G.pth
python3 test.py --dataroot datasets/close_syn2_lab/testA/ --name zoomed_syn2lab --model test --no_dropout
```