from PIL import Image
import os
import random
import json
import piexif
from piexif import helper
import numpy as np

layers_folder = os.path.join(os.getcwd(), 'generative-art-node', 'layers')
LAYER_ORDER = ['background', 'ball', 'eye color',
    'iris', 'shine', 'shine', 'bottom lid', 'top lid']
RARITIES = ['_r', '_sr']
RARITIES_LONG = {'_r': 'rare', '_sr': 'super_rare'}

def sum_dict_values(initial_dict, dict_to_add):
    for k, v in dict_to_add.items():
        if not k in initial_dict.keys():
            initial_dict.update({k: v})
        else:
            initial_dict[k] = initial_dict.get(k) + dict_to_add.get(k)
    return initial_dict

def multiply_dict_values(initial_dict, dict_to_multiply):
    for k, v in dict_to_multiply.items():
        if not k in initial_dict.keys():
            initial_dict.update({k: v})
        else:
            initial_dict[k] = initial_dict.get(k) * dict_to_multiply.get(k)
    return initial_dict

def set_weights(folder, amount_of_separation=1.6):
    file_names = os.listdir(folder)
    file_count = len(os.listdir(folder))
    extension = '.' + file_names[0].split('.')[1]
    base_probability = file_count/100
    rarity_counts = {'': 0}
    rarity_probabilities = {}
    total_rare_items = 0
    for rarity in RARITIES:
        for file_name in file_names:
            if file_name.endswith(f'{rarity}{extension}'): 
                sum_dict_values(rarity_counts, {rarity: 1.0})
                total_rare_items += 1
    total_common_items = file_count-total_rare_items
    rarity_counts.update({'': float(total_common_items)})
    most_recent_probability = base_probability
    amount_to_subtract = 0
    for k, v in rarity_counts.items():
        new_probability = most_recent_probability/amount_of_separation
        print(new_probability)
        rarity_probabilities.update({k: new_probability})
        amount_to_subtract += v*new_probability
        most_recent_probability = new_probability
    adjusted_total_probability = 100 - amount_to_subtract
    base_probability = adjusted_total_probability/total_common_items
    rarity_probabilities.update({'': base_probability})
    rarity_total = 0
    for k, v in rarity_probabilities.items():
        rarity_total += rarity_counts[k]*v
    print(f'probabilities: {rarity_probabilities}')
    print(f"total prob: {rarity_total}")
    return rarity_probabilities

def add_image_layer(folder, final_image=None):
    folder_path = os.path.join(layers_folder, folder)
    folder_files = os.listdir(folder_path)
    random_index = random.randrange(len(folder_files))
    with Image.open(os.path.join(folder_path, folder_files[random_index])) as im:
        im = im.convert('RGBA')
        if final_image is None: final_image = im
        else: final_image = Image.alpha_composite(final_image, im)
    return final_image, folder_files[random_index]

def parse_suffixes(**kwargs):
    suffixes = []
    try: [suffixes.append(val) for val in kwargs['rare_elements'].values()]
    finally:
        try: [suffixes.append(val) for val in kwargs['super_rare_elements'].values()]
        except ValueError: pass
    if len(suffixes) == 0: return ''
    elif len(suffixes) == 1: suffixes = suffixes[0]
    elif len(suffixes) == 2: suffixes = f'{suffixes[0]} and {suffixes[1]}'
    else: 
        suffixes_str = ','.join(suffixes[:-1])
        suffixes_str += f' and {suffixes[-1]}'
        suffixes = suffixes_str
    return suffixes
        

def generate_image_name(index, art_subject, qualifier, file_format='jpg', **kwargs):
    '''
    Create an image title from generated metadata. The name format will be:
    #{index} - {qualifier} {art_subject} (optionally stop here) with {rare items}, {super rare items}
    '''
    if len(kwargs['rare_elements']) == 0 and len(kwargs['super_rare_elements']) == 0: return f"#{index} - {qualifier} {art_subject}.{file_format}"
    else: suffixes = parse_suffixes(**kwargs)
    return f"#{index} - {qualifier} {art_subject} with {suffixes}.{file_format}"

def generate_random_image(folders):
    final_image = None
    metadata = {}
    characteristics = {}
    rare_elements = {}
    super_rare_elements = {}
    for folder in folders:
        ret = add_image_layer(folder, final_image)
        final_image = ret[0]
        image_name = ret[1].split('.')[0]
        if image_name[-2:] == '_r': 
            characteristics.update({folder: image_name[:-2]})
            rare_elements.update({folder: image_name[:-2]})
        elif image_name[-3:] == '_sr': 
            characteristics.update({folder: image_name[:-3]})
            super_rare_elements.update({folder: image_name[:-3]})
        else: characteristics.update({folder: image_name})
    metadata.update({'Authors': 'Trashgang NFTs'})
    metadata.update({'characteristics': characteristics})
    metadata.update({'rare_elements': rare_elements})
    metadata.update({'super_rare_elements': super_rare_elements})
    return final_image, metadata

def convert_to_jpg(image):
    return image.convert('RGB')

def encode_user_comment(file_name, comment):
    metadata = json.dumps(comment)
    exif_dict = piexif.load(file_name)
    exif_dict['Exif'][piexif.ExifIFD.UserComment] = helper.UserComment.dump(
        metadata, encoding='unicode'
    )
    piexif.insert(piexif.dump(exif_dict), file_name)

def write_corresponding_json(file_name, metadata):
    '''Option to write metadata to json file instead of encoding as comment'''
    write_target = f"{file_name.split('.')[0]}.json"
    with open(write_target, 'w') as f: f.write(json.dumps(metadata))

def create_sample_json():
    backgrounds = ["train station", "space", "dark alley"]
    bins = ["standard bin", "gold_bin_sr"]
    lids = ["cat box lid", "standard lid"]
    front_trashs = ["broken toy", "empty bottle", "air jordans"]
    left_trashs = ["old tv", "sex toys"]
    right_trashs = ["coathanger", "old clothes", "shoes"]
    sample_metadata = {
        "Authors": "Trashgang NFTs",
        "characteristics": {"background": random.choice(backgrounds), "bin": random.choice(bins), "front trash": random.choice(front_trashs), "left trash": random.choice(left_trashs), "right trash": random.choice(right_trashs), "lid": random.choice(lids)},
        "rare_elements": [],
        "super_rare_elements": ["gold_bin_sr"]
    }
    return sample_metadata

def main(write_to_json=False):
    img = generate_random_image(LAYER_ORDER)
    convert_to_jpg(img[0]).save('output/temp_file.jpg')
    output_filename = generate_image_name(420, img[1]['characteristics']['ball'], img[1]['characteristics']['eye color'], rare_elements=img[1]['rare_elements'], super_rare_elements=img[1]['super_rare_elements'])
    os.rename(os.path.join(os.getcwd(), 'output/temp_file.jpg'), os.path.join(os.getcwd(), f'output/{output_filename}'))
    encode_user_comment(f'output/{output_filename}', img[1])

if __name__ == '__main__':
    main()