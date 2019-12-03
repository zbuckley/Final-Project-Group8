from KaggleDataset import KaggleDataset
from training_common_utils import image_preprocessing
import torch
from torchvision.models import densenet121
from torch.utils.data import DataLoader

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def predict_on_test_data(test_data_loader):
    # Load model
    model_state_dict = torch.load("../Models/model_team8_uzeros.pt")

    model = densenet121(num_classes=14).to(device)

    model.load_state_dict(model_state_dict)

    # Classify inputs
    for images, labels in test_data_loader:
        local_images, local_labels = images.to(device, dtype=torch.float), labels.to(device, dtype=torch.float)
        preds = model(local_images)
        print(preds)


# Test on Kaggle
kaggle_data = KaggleDataset(
    csv_file="../Data/sample/sample_labels.csv",
    root_dir="../Data/sample/images",
    image_transform=image_preprocessing
)

kaggle_data_loader = DataLoader(kaggle_data)

predict_on_test_data(kaggle_data_loader)
