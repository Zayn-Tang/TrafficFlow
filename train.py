from util.setup import *

if __name__ == '__main__':
    args = load_args()
    trainer = load_trainer(args)
    trainer.compose_loader()
    trainer.setup_model()
    trainer.train()



# STGCN
# python train.py --model STGCN --ddir ./datasets/PEMSD7 --dname PEMSD7