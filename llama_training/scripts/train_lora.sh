#!/bin/bash
#SBATCH --job-name=llava-pretrain
#SBATCH --partition=spgpu
#SBATCH --account=chaijy2
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --time=64:00:00
#SBATCH --mem=160G
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:4
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --output="/gpfs/accounts/chaijy_root/chaijy0/owenhji/llama_log/slurm-%A.out"

MODEL_VERSION=Vicuna

CUDA_VISIBLE_DEVICES=0,1,2,3 deepspeed fastchat/train/train_lora.py \
    --model_name_or_path /nfs/turbo/coe-chaijy/pre-trained-weights/vicuna/vicuna-7b-v1.1  \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --data_path /gpfs/accounts/chaijy_root/chaijy0/owenhji/FastChat/data/data.json \
    --bf16 True \
    --output_dir ./checkpoints_train \
    --num_train_epochs 20.0 \
    --per_device_train_batch_size 5 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1200 \
    --save_total_limit 100 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 1024 \
    --q_lora True \
    --lazy_preprocess True\
    --deepspeed playground/deepspeed_config_s2.json \
    --flash_attn True \
