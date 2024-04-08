#from pydub import AudioSegment
import os
import glob
import librosa
import soundfile as sf
import numpy as np
new_samplerate=8000
path2="train-clean-100/"
path3="dev-clean/"
path4="test-clean/"
#path1="../skdata/"+path2+"LibriSpeech/"+path2
out_path="../skdata/"+path2+f"data{new_samplerate}/"
#in_path=path1
fragment_mum=2
#path3="mixjoint/mix_84_121123_174_50561"
def joint_s(input_folder1,input_folder2,output_folder):
    # 获取文件夹中的所有flac文件
    flac_files1 = [f for f in os.listdir(input_folder1) if f.endswith('.flac')][:fragment_mum]
    flac_files2 = [f for f in os.listdir(input_folder2) if f.endswith('.flac')][:fragment_mum]
    if len(flac_files1)<fragment_mum or len(flac_files2)<fragment_mum:
        print("s音频不足")
        os.rmdir(output_folder)
        return 1
    # 存储处理后的音频数据
    processed_audio1 = []
    processed_audio2 = []
    # 处理每个flac文件
    for file in flac_files1:
        audio_data, sample_rate = sf.read(os.path.join(input_folder1, file))
        if sample_rate!=new_samplerate:
            audio_data = librosa.resample(y=audio_data, orig_sr=sample_rate, target_sr=new_samplerate)
            sample_rate=new_samplerate
        # 截取前5秒并进行静音补齐
        target_length = sample_rate * 5
        if len(audio_data) < target_length:
            audio_data = np.concatenate((audio_data, np.zeros(target_length - len(audio_data))))
        else:
            audio_data = audio_data[:target_length]
        audio_data = np.concatenate((audio_data, np.zeros(target_length)))
        processed_audio1.append(audio_data)
    # 处理每个flac文件
    for file in flac_files2:
        audio_data, sample_rate = sf.read(os.path.join(input_folder2, file))
        if sample_rate!=new_samplerate:
            audio_data = librosa.resample(y=audio_data, orig_sr=sample_rate, target_sr=new_samplerate)
            sample_rate=new_samplerate
        # 截取前5秒并进行静音补齐
        target_length = sample_rate * 5
        if len(audio_data) < target_length:
            audio_data = np.concatenate((audio_data, np.zeros(target_length - len(audio_data))))
        else:
            audio_data = audio_data[:target_length]
        audio_data = np.concatenate((np.zeros(target_length),audio_data))
        processed_audio2.append(audio_data)
    # 拼接音频数据
    output_audio_sk1 = np.concatenate(processed_audio1)
    output_audio_sk2 = np.concatenate(processed_audio2)
    output_audio_mix = output_audio_sk1 + output_audio_sk2
    # 输出拼接后的音频数据到WAV文件
    sf.write(output_folder+"sk1.wav", output_audio_sk1, sample_rate, format='WAV')  # 指定输出为WAV格式
    sf.write(output_folder+"sk2.wav", output_audio_sk2, sample_rate, format='WAV')  # 指定输出为WAV格式
    sf.write(output_folder+"mix.wav", output_audio_mix, sample_rate, format='WAV')  # 指定输出为WAV格式

    print("拼接完成，输出文件为:", output_folder)
def joint_c(input_folder1,input_folder2,output_folder):
    # 获取文件夹中的所有flac文件
    flac_files1 = [f for f in os.listdir(input_folder1) if f.endswith('.flac')][:fragment_mum*2]
    flac_files2 = [f for f in os.listdir(input_folder2) if f.endswith('.flac')][:fragment_mum*2]
    if len(flac_files1)<fragment_mum*2 or len(flac_files2)<fragment_mum*2:
        print("c音频不足")
        os.rmdir(output_folder)
        return 1
    # 存储处理后的音频数据
    processed_audio1 = []
    processed_audio2 = []
    # 处理每个flac文件
    for file in flac_files1:
        audio_data, sample_rate = sf.read(os.path.join(input_folder1, file))
        if sample_rate!=new_samplerate:
            audio_data = librosa.resample(y=audio_data, orig_sr=sample_rate, target_sr=new_samplerate)
            sample_rate=new_samplerate
        # 截取前5秒并进行静音补齐
        target_length = sample_rate * 5
        if len(audio_data) < target_length:
            audio_data = np.concatenate((audio_data, np.zeros(target_length - len(audio_data))))
        else:
            audio_data = audio_data[:target_length]
        #audio_data = np.concatenate((audio_data, np.zeros(target_length)))
        processed_audio1.append(audio_data)
    # 处理每个flac文件
    for file in flac_files2:
        audio_data, sample_rate = sf.read(os.path.join(input_folder2, file))
        if sample_rate!=new_samplerate:
            audio_data = librosa.resample(y=audio_data, orig_sr=sample_rate, target_sr=new_samplerate)
            sample_rate=new_samplerate
        # 截取前5秒并进行静音补齐
        target_length = sample_rate * 5
        if len(audio_data) < target_length:
            audio_data = np.concatenate((audio_data, np.zeros(target_length - len(audio_data))))
        else:
            audio_data = audio_data[:target_length]
        #audio_data = np.concatenate((np.zeros(target_length),audio_data))
        processed_audio2.append(audio_data)
    # 拼接音频数据
    output_audio_sk1 = np.concatenate(processed_audio1)
    output_audio_sk2 = np.concatenate(processed_audio2)
        # 输出拼接后的音频数据到WAV文件
    sf.write(output_folder+"sk1.wav", output_audio_sk1, sample_rate, format='WAV')  # 指定输出为WAV格式
    sf.write(output_folder+"sk2.wav", output_audio_sk2, sample_rate, format='WAV')  # 指定输出为WAV格式
    try:
        output_audio_mix = output_audio_sk1 + output_audio_sk2
    except ValueError as e:
        print("长度错误",e)
    else:
        sf.write(output_folder+"mix.wav", output_audio_mix, sample_rate, format='WAV')  # 指定输出为WAV格式

    print("拼接完成，输出文件为:", output_folder)
    return 0
def get_path(folder_path):
    # 指定文件夹路径
    # 获取文件夹中所有子文件夹
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    # 获取每个子文件夹的第一个子文件夹
    first_subfolders = []
    for folder in subfolders:
        sub_subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
        if len(sub_subfolders) > 0:
            first_subfolder = sub_subfolders[0]
            first_subfolders.append(first_subfolder)
    return first_subfolders
def joint_d(path_x):
    in_path="../skdata/"+path_x+"LibriSpeech/"+path_x
    out_path="../skdata/"+path2+f"data{new_samplerate}/"
    path_list=get_path(in_path)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    i=0
    while i<len(path_list)-1:
        out_path_s=out_path+"s/"+str(i)+"/"
        if not os.path.exists(out_path_s):
            os.makedirs(out_path_s)
        out_path_c=out_path+"c/"+str(i)+"/"
        if not os.path.exists(out_path_c):
            os.makedirs(out_path_c)
        #print(path_list[i])
        #print(path_list[i+1])
        joint_s(path_list[i],path_list[i+1],out_path_s)
        joint_c(path_list[i],path_list[i+1],out_path_c)
        i+=1
joint_d(path2)
joint_d(path3)
joint_d(path4)