import os
import random

class NFTDatabase():
    def __init__(self, folder):
        self.folder = folder
        unique_files = []
        used_images = []
        nft_dict = {}
        for file_name in os.listdir(self.folder):
            if not file_name.split('.')[0] in unique_files: unique_files.append(file_name.split('.')[0])
        for unique_file in unique_files:
            file_name = os.path.join(self.folder, unique_file)
            nft_dict.update({f"{file_name}.jpg": f"{file_name}.json"})
        self.nft_dict = nft_dict
        self.nfts_available = True

    def update_nfts_avaiable(self):
        if len(self.nft_dict) > 0: self.nfts_available = True
        else: self.nfts_available = False

    def get_random_nft_paths(self):
        items_list = list(self.nft_dict.items())
        rand_index = random.randrange(0, len(items_list))
        print(f"items left {len(items_list)}")
        print(f"THE INDEX IS {rand_index} the key is {items_list[rand_index]}")
        paths = (items_list[rand_index][0], self.nft_dict.pop(items_list[rand_index][0]))
        return paths


if __name__ == '__main__':
    folder = 'trashgang-site/src/Sample NFTs'
    nft_db = NFTDatabase(folder)
    paths = nft_db.get_random_nft_paths()